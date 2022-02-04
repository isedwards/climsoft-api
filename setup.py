from setuptools import find_packages, setup

with open("requirements.txt", "r") as requirements_file:
    requirements = [r.strip("\n") for r in requirements_file.readlines()]

setup(
    name='climsoft_api',
    version='0.1.0',
    description='API to manage climsoft data.',
    author='OpenCDMS',
    author_email='info@opencdms.org',
    url='https://github.com/opencdms/climsoft-api',
    package_dir={
        "": "src"
    },
    packages=find_packages(where="./src"),
    install_requires=requirements
)