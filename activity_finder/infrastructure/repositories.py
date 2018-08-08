# -*- coding: utf-8 -*-

import json

class LoadFromFileActivityRepository(object):

    def __init__(self, file_path):
        with open(file_path) as f:
            self._data = json.load(f)

    def find_by(self, filter=None):
        if filter is None:
            return self._data
        return self._filter_activities(filter)

    def _filter_activities(self, search_filter):
        return [ activity for activity in self._data if self._match_filter(activity, search_filter)]

    def _match_filter(self, activity, search_filter):
        for field in search_filter.keys():
            if activity[field] != search_filter[field]:
                return False
        return True
