from setuptools import setup, find_packages

setup(
	name = "datawrangler",
	version = "0.0.1",
	install_requires=["pandas"]
	packages=find_packages(exclude=['contrib', 'docs', 'tests]),
)