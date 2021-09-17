from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in apt_services/__init__.py
from apt_services import __version__ as version

setup(
	name="apt_services",
	version=version,
	description="Services of compagnie",
	author="AptitudeTech",
	author_email="info@aptitutdetech.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
