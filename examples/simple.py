from tropicalnest import TemplateStack
from troposphere import Parameter, Ref, Template
from troposphere.logs import LogGroup

master = Template("A test template with nested templates")

logs = Template("cloudwatch log groups")
log_group_name = Parameter("Name", Type="String")
log_group = LogGroup(
    "TestLogGroup",
    LogGroupName=Ref(log_group_name),
    RetentionInDays=30,
)
logs.add_parameter(log_group_name)
logs.add_resource(log_group)

ts = TemplateStack("master", master)
ts.add_template("Logs", logs, Parameters={'Name': 'test'})
ts.save('mybucket')
