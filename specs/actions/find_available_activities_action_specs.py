# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.actions.find_activities import FindActivitiesAction


FAKE_ACTIVITY_LIST_SAMPLE = ['irrelevant-activity']
FAKE_GEOJSON_RESULT = 'irrelevant-result'

with describe('find available activities action specs'):
    with before.each:
         pass
    with context('when no filter is provided'):
        with it('returns all available activities in geoJson format'):
            activities_service_stub = Stub()
            when(activities_service_stub).find_by(ANY_ARG).returns(FAKE_ACTIVITY_LIST_SAMPLE)
            geoJson_formater = Stub()
            when(geoJson_formater).to_feature_collection(FAKE_ACTIVITY_LIST_SAMPLE).returns(FAKE_GEOJSON_RESULT)
            find_activities_action = FindActivitiesAction(activities_service_stub, geoJson_formater)

            all_available_activities = find_activities_action.execute()

            expect(all_available_activities).to(equal(FAKE_GEOJSON_RESULT))

    with context('when filter is provided'):
        with it('returns filtered available activities in geoJson format'):
            filter = {}
            activities_service_stub = Stub()
            when(activities_service_stub).find_by(filter).returns(FAKE_ACTIVITY_LIST_SAMPLE)
            geoJson_formater = Stub()
            when(geoJson_formater).to_feature_collection(FAKE_ACTIVITY_LIST_SAMPLE).returns(FAKE_GEOJSON_RESULT)
            find_activities_action = FindActivitiesAction(activities_service_stub, geoJson_formater)

            all_available_activities = find_activities_action.execute(filter)

            expect(all_available_activities).to(equal(FAKE_GEOJSON_RESULT))
