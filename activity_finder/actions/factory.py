# -*- coding: utf-8 -*-

from infcommon import Factory

from activity_finder.model import factory as model_factory

from activity_finder.actions.find_activities import FindActivitiesAction



def find_activities_action():
    return Factory.instance('find_activities_action',
            lambda: FindActivitiesAction(model_factory.activities_service(),
                                         model_factory.geojson_formater())
            )
