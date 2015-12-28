#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os

import angus.service

PORT = os.environ.get('PORT', 9000)

LOGGER = logging.getLogger('dummy')


def compute(resource, data):
    if 'echo' in data:
        resource['echo'] = data['echo']
    else:
        resource['echo'] = "echo"


def main():
    logging.basicConfig(level=logging.DEBUG)

    service = angus.service.Service(
        'dummy', 1,
        PORT,
        compute,
        resource_storage=dict(), threads=1
    )
    service.start()


if __name__ == '__main__':
    main()
