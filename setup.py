try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
  
setup(
    name='pystash',
    version='0.0.14',
    author='Alexander Davydov',
    author_email='nyddle@gmail.com',
    packages=[ 'pystash' ],
    scripts=[ 'bin/stash' ],
    url='http://pypi.python.org/pypi/pystash/',
    license='LICENSE.txt',
    description='Save your code snippets in the cloud.',
    zip_safe=False,
    install_requires=[
        "args>=0.1.0",
        "clint>=0.3.3",
        "requests>=2.2.0",
        "wsgiref>=0.1.2",
        "xerox"
    ],
    tests_require=[
        "args>=0.1.0",
        "clint>=0.3.3",
        "requests>=2.2.0",
        "wsgiref>=0.1.2",
        "xerox"
    ],
)
