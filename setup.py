# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gmapapi',
    version='0.1.0',
    description='python geocoding script using google map api',
    long_description=readme,
    author='Yui Miyahara',
    author_email='yui.miyahara@accenture.com',
    url='',
    install_requires=['requests', 'pytest'],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

