from setuptools import setup

setup(
    name="kryslib",
    version="0.1.0",
    description="A library for the Krys project",
    author="Chad Provencher",
    author_email="kryses@kryses.com",
    packages=["kryslib", "kryslib.colors"],
    package_dir={"kryslib": "src/kryslib", "kryslib.colors": "src/kryslib/colors"},
)
