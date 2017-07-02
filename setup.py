from setuptools import setup, find_packages

setup(
    name='package-name',
    version=0.1,
    description='Description',
    author='your name here',
    author_email='your email here',
    license=['proprietary'],
    packages=[
        # list python paths of all packages and subpackages
        # (relative directory paths with . separator instead of /)
        # or use find_packages() instead of list--only works if
        # you touch __init__.py in all your code dirs
    ],
    zip_safe=False,
    install_requires=['falcon', 'requests'],
    entry_points={
        'console_scripts': [
            # 'commandname=module.path:function'
        ],
    },
)
