from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rfid_integration/__init__.py
from rfid_integration import __version__ as version

setup(
	name="rfid_integration",
	version=version,
	description="simple Rfid Integration",
	author="Jide Olayinka",
	author_email="olajamesjide@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
