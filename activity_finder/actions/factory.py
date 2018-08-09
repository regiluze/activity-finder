# -*- coding: utf-8 -*-

from infcommon import Factory

from activity_finder.model import factory as model_factory

from activity_finder.actions.find_activities import FindActivitiesAction
from activity_finder.actions.recommend_activity import RecommendActivityAction



def find_activities_action():
    return Factory.instance('find_activities_action',
            lambda: FindActivitiesAction(model_factory.activities_service(),
                                         model_factory.geojson_formater())
            )

def recommend_activity_action():
    return Factory.instance('recommend_activity_action',
            lambda: RecommendActivityAction(model_factory.activities_service(),
                                            model_factory.geojson_formater())
            )
