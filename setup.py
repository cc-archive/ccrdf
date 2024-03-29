## Copyright (c) 2006 Nathan R. Yergler, Creative Commons

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the "Software"),
## to deal in the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name = "ccrdf",
    version = "0.6a4",
    packages = ['ccrdf'],

    install_requires = ['setuptools',
                        'rdflib',
                        ],
    include_package_data = True,
    zip_safe = True,

    entry_points = """
        [ccrdf.extract_text]
        null = ccrdf.rdfextract:null_extractor
        string = ccrdf.rdfextract:string_extractor
        regex = ccrdf.rdfextract:regex_extractor
        link = ccrdf.rdfextract:link_extractor
    """,

    author = 'Nathan R. Yergler',
    author_email = 'nathan@creativecommons.org',
    description = 'XXX.',
    long_description=(
         read('README')
         + '\n' +
         read('CHANGES')
         + '\n' +
         'Download\n'
         '********\n'
         ),
    license = 'MIT',
    url = 'http://wiki.creativecommons.org/CcRdf',

    )
