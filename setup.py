from setuptools import find_packages, setup

with open("requirements.txt", encoding="UTF8") as f:
    requirements = f.read().splitlines()

setup(
    name="Name",
    version="0.1",
    description="Description",
    packages=find_packages(where=".", exclude=("tests", "tests.*", "data", "data.*")),
    package_dir={"module": "Module"},
    install_requires=requirements,
)
