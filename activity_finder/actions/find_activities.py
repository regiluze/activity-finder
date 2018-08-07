# -*- coding: utf-8 -*-


class FindActivitiesAction(object):

    def __init__(self, activities_service, geoJsonFormater):
        self._activities_service = activities_service
        self._geoJsonFormater = geoJsonFormater

    def execute(self, filter=None):
        available_activities = self._activities_service.find_by(filter)
        return self._geoJsonFormater.to_feature_collection(available_activities)

