# -*- coding: utf-8 -*-

from infcommon import Factory

from activity_finder.model.activity import ActivitiesService
from activity_finder.model.geojson import GeoJsonFormater
from activity_finder.infrastructure import factory as infrastructure_factory

def activities_service():
    return Factory.instance('activities_service',
            lambda: ActivitiesService(infrastructure_factory.activity_repository())
            )


def geojson_formater():
    return Factory.instance('geojson_formater',
            lambda: GeoJsonFormater()
            )
