#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__updated__ = "2015-12-28"
__author__ = "Aurélien Moreau"
__copyright__ = "Copyright 2015, Angus.ai"
__credits__ = ["Aurélien Moreau", "Gwennaël Gâté"]
__status__ = "Production"

setup(name='angus-service-dummy',
      version="0.0.1",
      description='Angus Dummy Service',
      author=__author__,
      author_email='aurelien.moreau@angus.ai',
      url='http://www.angus.ai/',
      install_requires=[
          "angus-framework",
      ],
      packages=find_packages(),
      )
