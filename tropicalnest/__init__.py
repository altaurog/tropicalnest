import io
import os
import pathlib
import troposphere
from troposphere import cloudformation
import boto3


class TemplateStack:
    def __init__(self, name, template, kwargs=None, validate=False):
        self.name = name
        self.template = template
        self.should_validate = validate
        self.kwargs = kwargs or {}
        self.template_stacks = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_template(self, name, template=None, **kwargs):
        if isinstance(name, TemplateStack):
            template_stack = name
        else:
            if not isinstance(name, str):
                raise ValueError("Template name must be a string: {}".format(name))
            if not isinstance(template, troposphere.Template):
                raise ValueError("Not a valid template type: {}".format(template))
            template_stack = TemplateStack(name, template, kwargs, validate=True)
        self.template_stacks.append(template_stack)
        return template_stack

    def upload(self, base_path):
        # use unbound method so each instance can "bind" itself
        self.materialize(base_path, TemplateStack._s3)

    def save(self, base_path):
        self.materialize(base_path, TemplateStack._local)

    def materialize(self, base_path, output_method):
        self.validate()
        path = pathlib.PurePosixPath(base_path)
        for template_stack in self.template_stacks:
            stack = template_stack.materialize(path / self.name, output_method)
            self.template.add_resource(stack)
        output_method(self, path)  # output_method is unbound
        url = self.template_url(path)
        return self.stack(url)

    def _s3(self, path):
        bucket = path.parts[0]
        key = self.filepath(path).relative_to(bucket)
        fileobj = io.BytesIO(self.template.to_json().encode('utf-8'))
        client = boto3.client('s3')
        client.upload_fileobj(fileobj, bucket, key)
        return key

    def _local(self, path):
        filepath = self.filepath(path)
        os.makedirs(filepath.parent, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(self.template.to_json())
        return filepath

    def validate(self):
        if not self.should_validate:
            return
        parameters = list(self.template.parameters.values())
        inputs = self.kwargs.get('Parameters', {})
        for parameter in parameters:
            self.validate_parameter(parameter, inputs.get(parameter.title))
        unknown = set(inputs) - set(p.title for p in parameters)
        if unknown:
            message = "Unknown parameters specified on nested stack {}: {}"
            raise ValueError(message.format(self.name, unknown))

    def validate_parameter(self, parameter, parameter_input):
        parameter_default = parameter.properties.get('Default')
        if parameter_input is None:
            if parameter_default is None:
                message = "No value specified for parameter {} on nested stack {}"
                raise ValueError(message.format(parameter.title, self.name))
        # should validate parameter types here also

    def stack(self, url):
        self.kwargs['TemplateURL'] = url
        return cloudformation.Stack(self.name, **self.kwargs)

    def template_url(self, parent_path):
        filepath = self.filepath(parent_path)
        return 'https://s3.amazonaws.com/' + str(filepath)

    def filepath(self, parent_path):
        filename = self.name.lower() + '.json'
        return parent_path / filename
