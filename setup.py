from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in coatserve/__init__.py
from coatserve import __version__ as version

setup(
	name="coatserve",
	version=version,
	description="coarserve customaization",
	author="ashuar",
	author_email="ashuarchughtai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
