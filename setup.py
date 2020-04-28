"""
Install opa.

setup.py for the `opa` package.
"""

import os
from setuptools import setup
from setuptools.command.install import install
from opa import __version__

README = open(
    os.path.join(os.path.dirname(__file__), 'README.md')
) .read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='opa',
    version=__version__,
    packages=['opa'],
    include_package_data=True,
    license='BSD License',    # example license
    description='A RSS feed aggregator built on Django.',
    long_description=README,
    url='https://pramari.de/opa',
    author='Andreas.Neumeier',
    author_email='andreas@neumeier.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',    # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=3.0.0',
        'pyyaml',
    ],
    #setup_requires=['pytest-runner'],
    #tests_require=['py.test', ],
    # cmdclass={
    #    'install': InstallCommand,
    # },
)
