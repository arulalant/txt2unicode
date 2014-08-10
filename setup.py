#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# (C) 2014-2015 Arulalan.T
# txt2unicode project

from distutils.core import setup
from codecs import open

setup(name='txt2unicode',
      version='v3.0',
      description='Tamil language text encode to unicode converters and vice versa tool',
      author='Arulalan.T',
      author_email='arulalant@gmail.com',
      url='https://github.com/arulalant/txt2unicode',
      packages=['txt2unicode'],
      license='GPLv3',
      platforms='PC,Linux,Mac',
      classifiers='Natural Language :: Tamil',
      long_description=open('README.md','r','UTF-8').read(),
      download_url='https://github.com/arulalant/txt2unicode/archive/latest.zip',#pip
      )
