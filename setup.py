#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path

from setuptools import setup

import pymisp

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='pymisp',
    version=pymisp.__version__,
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    maintainer='Raphaël Vinot',
    url='https://github.com/MISP/PyMISP',
    project_urls={
        'Documentation': 'http://pymisp.readthedocs.io',
        'Source': 'https://github.com/MISP/PyMISP',
        'Tracker': 'https://github.com/MISP/PyMISP/issues',
    },
    description='Python API for MISP.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pymisp', 'pymisp.tools'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet',
    ],
    install_requires=['six', 'requests', 'python-dateutil', 'jsonschema',
                      'python-dateutil', 'enum34;python_version<"3.4"',
                      'functools32;python_version<"3.0"', 'deprecated'],
    extras_require={'fileobjects': ['lief>=0.8,<0.10;python_version<"3.5"', 'lief>=0.10.0.dev0;python_version>"3.5"', 'python-magic', 'pydeep'],
                    'neo': ['py2neo'],
                    'openioc': ['beautifulsoup4'],
                    'virustotal': ['validators'],
                    'docs': ['sphinx-autodoc-typehints', 'recommonmark'],
                    'pdfexport': ['reportlab']},
    tests_require=[
        'jsonschema',
        'python-magic',
        'requests-mock'
    ],
    test_suite="tests.test_mispevent",
    include_package_data=True,
    package_data={'pymisp': ['data/*.json',
                             'data/misp-objects/schema_objects.json',
                             'data/misp-objects/schema_relationships.json',
                             'data/misp-objects/objects/*/definition.json',
                             'data/misp-objects/relationships/definition.json',
                             'tools/pdf_fonts/Noto_TTF/*']},
)
