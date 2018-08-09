from setuptools import setup, find_packages

setup(
    name='activities-finder',
    version='0.0.1',
    author='regiluze',
    description='Simple tool to find fun activities',
    platforms='Linux',
    packages=find_packages(exclude=['specs', 'integration_specs'])
)
