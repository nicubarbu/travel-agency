from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Travel Agency',
    version='0.0.1',
    description='Faculty project for creating a travel agency',
    long_description=readme,
    author='Nicusor-Lucian Barbu',
    author_email='contact.nicubarbu@gmail.com',
    url='https://github.com/nicubarbu',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
