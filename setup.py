from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hikka",
    version="0.0.2",
    author="Lorg0n",
    author_email="lorgon.kv@gmail.com",
    description="The library helps to interact with the open API from hikka.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        "requests",
    ]
)