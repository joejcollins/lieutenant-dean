""" Setup as a package so that celery can access the packages.  Then
install with `requirements.txt` and `-e .`.  """
from setuptools import setup, find_packages
setup(name='captain-black', version='1.0', packages=find_packages())
