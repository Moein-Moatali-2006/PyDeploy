from setuptools import setup

def pre_install():
    # f = open("README.md")
    # text = f.read()
    text = "Describe"
    return text

setup(
    name="amoo_moein_lion",
    version="1.0.0",
    author="Moein Moatali",
    description="A test package for moein",
    long_description=pre_install(),
    requires=[],
    author_email="MoeinMoatali@gmail.com",
    packages=["amoo_moein_lion"]
)