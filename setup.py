
from setuptools import setup, find_packages

setup (
	name='dellve_hpl',
	version='0.0.1',
	packages=find_packages(),
	install_requires=['dellve', 'psutil'],
	entry_points='''
	[dellve.benchmarks]
	HPL=dellve_hpl:HPL
	'''
)
