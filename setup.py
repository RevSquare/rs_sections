#! /usr/bin/env python
from distutils.core import setup
import sys
reload(sys).setdefaultencoding('Utf-8')


setup(
    name='rs-sections',
    version='0.1',
    author='Tomasz Roszko',
    author_email='tomaszroszko@revsquare.com',
    description='Base App for django cms from revsquare.',
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=['rs_sections'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0.1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Documentation',
        ],
    )
