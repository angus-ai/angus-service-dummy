#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__updated__ = "2016-12-09"
__author__ = "Aurélien Moreau"
__copyright__ = "Copyright 2015, Angus.ai"
__credits__ = ["Aurélien Moreau", "Gwennaël Gâté"]
__status__ = "Production"

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='angus-service-dummy',
      version="0.0.2",
      description='Angus Dummy Service',
      author=__author__,
      author_email='aurelien.moreau@angus.ai',
      url='http://www.angus.ai/',
      install_requires=requirements,
      packages=find_packages(),
      )
