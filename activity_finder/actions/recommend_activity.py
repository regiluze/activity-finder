# -*- coding: utf-8 -*-


class RecommendActivityAction(object):

    def __init__(self, activities_service, geoJsonFormater):
        self._activities_service = activities_service
        self._geoJsonFormater = geoJsonFormater

    def execute(self, data):
        available_activities = self._activities_service.recommend_activity(filter=data)
        return self._geoJsonFormater.to_feature(available_activities)
