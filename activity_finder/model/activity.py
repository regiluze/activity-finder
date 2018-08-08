# -*- coding: utf-8 -*-

class Activity(object):

    def __init__(self, **kwargs):
        self._latlng = kwargs['latlng']
        del kwargs['latlng']
        self._properties = kwargs

    @property
    def lat(self):
        return self._latlng[0]

    @property
    def long(self):
        return self._latlng[1]

    @property
    def properties(self):
        return self._properties



class ActivitiesService(object):

    def __init__(self, activities_repository):
        self._activities_repository = activities_repository


    def find_by(self, filter=None):
        activities = self._activities_repository.find_by(filter)
        return [Activity(**activity) for activity in activities]
