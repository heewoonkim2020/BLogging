from setuptools import setup, find_packages

setup(
    name='blogging',
    version='0.1.0',
    packages=find_packages(),
    author='TheRealAndrew',
    description='Better Logging for Python',
    install_requires=[
        'colorama==0.4.6'
    ]
)