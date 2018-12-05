# make the package available as a script on the command line

from setuptools import setup

setup(
    name='python_cli',
    author='Subh Samal',
    version='0.0.1',
    packages=['python_cli'],
    entry_points={
        'console_scripts': [
            'python_cli = python_cli.__main__:main'
        ]
    })
