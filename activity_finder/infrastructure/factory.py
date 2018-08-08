# -*- coding: utf-8 -*-

import os
from infcommon import Factory

from activity_finder.infrastructure.repositories import LoadFromFileActivityRepository

BASE_PATH = os.path.abspath(os.path.dirname(__file__)) + '/data'
FILE_NAME = 'madrid.json'

def activity_repository():
    json_file_path = '{base_path}/{file_name}'.format(base_path=BASE_PATH, file_name=FILE_NAME)
    return Factory.instance('activity_repository',
            lambda: LoadFromFileActivityRepository(file_path=json_file_path)
            )
