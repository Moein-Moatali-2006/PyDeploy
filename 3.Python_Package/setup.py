from setuptools import setup, find_packages

setup(
    name="MIGA",
    version="1.0.0",
    description="Geography of Iran using Python Turtle.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Moein Moatali",
    author_email="MoeinMoatali@gmail.com",
    packages=find_packages(include=["MIGA", "MIGA.*"]),
    include_package_data=True,
)
