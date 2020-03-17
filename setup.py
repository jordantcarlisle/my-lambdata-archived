# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="dspt4_unit3_package",
    version="1.0",
    author="Jordan Carlisle",
    author_email="jordantcarlisle@gmail.com",
    description="My first python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/jordantcarlisle/my-lambdata",
    # keywords="",
    packages=find_packages()  # ["dspt4_unit3_package"]
)
