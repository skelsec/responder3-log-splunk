from setuptools import setup

setup(
	# Application name:
	name="Responder3 Log Extension for Splunk",

	# Version number (initial):
	version="0.0.1",

	# Application author details:
	author="Tamas Jos",
	author_email="responder3@skelsec.com",

	# Packages
	packages=["responder3_log_splunk"],

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/skelsec/responder3-log-splunk",

	zip_safe = True,
	#
	# license="LICENSE.txt",
	description="Responder3 Log Extension for Splunk logging",

	# long_description=open("README.txt").read(),

	#Dependent packages (distributions)
	install_requires=[
	],

	python_requires='>=3.7',
)
