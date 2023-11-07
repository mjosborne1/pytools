# -*- coding: utf-8 -*-

# Original: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pytools',
    version='0.1.0',
    description='Python based tools library - primarily using pathling see: https://pathling.csiro.au/docs)',
    long_description=readme,
    author='Michael Osborne',
    author_email='mjosborne1@gmail.com',
    url='https://github.com/mjosborne1/pytools.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

