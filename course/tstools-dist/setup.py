from setuptools import setup

setup(name='tstools',
      version='0.1',
      description='A package to analyse timeseries',
      author='Samvida S. Venkatesh',
      email='samvida.venkatesh@gmail.com',
      packages=['tstools'],
      install_requires = ["numpy", "matplotlib", "scipy"],
      license='GPLv3')