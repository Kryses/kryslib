from setuptools import setup, find_packages

setup(
    name="kryslib",
    version="0.1.0",
    description="A library for the Krys project",
    author="Chad Provencher",
    author_email="kryses@kryses.com",
    packages=find_packages(),
    install_requires=[
        "asttokens==2.4.1",
        "colorama==0.4.6",
        "executing==2.0.1",
        "icecream==2.1.3",
        "iniconfig==2.0.0",
        "packaging==23.2",
        "pluggy==1.3.0",
        "Pygments==2.17.2",
        "pytest==7.4.3",
        "six==1.16.0",
    ],
)
