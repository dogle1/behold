from setuptools import setup, find_packages

# Read the contents of requirements.txt and split into a list
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name="behold",
    version="0.1",
    packages=find_packages(include=['src', 'src.config.*']),
    include_package_data=True,
    install_requires=[
        required_packages
    ],
    entry_points={
        "console_scripts": [
            "behold = src.main:main"
        ]
    },
)
