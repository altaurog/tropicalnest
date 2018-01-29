from setuptools import setup, find_packages

setup(
    name='tropicalnest',
    version=0.1,
    description='Extension for troposphere cloudformation library',
    author='Aryeh Leib Taurog',
    author_email='python@aryehleib.com',
    license=['BSD'],
    packages=['tropicalnest'],
    zip_safe=False,
    install_requires=['boto3', 'troposphere'],
    entry_points={
        'console_scripts': [
            # 'commandname=module.path:function'
        ],
    },
)
