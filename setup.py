from setuptools import find_packages, setup

with open("requirements.txt", encoding="UTF8") as f:
    requirements = f.read().splitlines()

setup(
    name="mail-organizer",
    version="0.1",
    description="Module that organizes Gmail attachments in a private Google Drive. ",
    packages=find_packages(where=".", exclude=("tests", "tests.*", "data", "data.*")),
    package_dir={"mail-organizer": "mail_organizer"},
    install_requires=requirements,
)
