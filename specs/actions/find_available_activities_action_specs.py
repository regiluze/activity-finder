# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.actions.find_activities import FindActivitiesAction


FAKE_ACTIVITY_LIST_SAMPLE = ['irrelevant-activity']
FAKE_GEOJSON_RESULT = 'irrelevant-result'

with describe('find available activities action specs'):
    with before.each:
        self.activities_service_stub = Stub()
        self.geoJson_formater = Stub()
        self.find_activities_action = FindActivitiesAction(self.activities_service_stub, self.geoJson_formater)

    with context('when no filter is provided'):
        with it('returns all available activities in geoJson format'):
            when(self.activities_service_stub).find_by(ANY_ARG).returns(FAKE_ACTIVITY_LIST_SAMPLE)
            when(self.geoJson_formater).to_feature_collection(FAKE_ACTIVITY_LIST_SAMPLE).returns(FAKE_GEOJSON_RESULT)

            all_available_activities = self.find_activities_action.execute()

            expect(all_available_activities).to(equal(FAKE_GEOJSON_RESULT))

    with context('when filter is provided'):
        with it('returns filtered available activities in geoJson format'):
            filter = {}
            when(self.activities_service_stub).find_by(filter).returns(FAKE_ACTIVITY_LIST_SAMPLE)
            when(self.geoJson_formater).to_feature_collection(FAKE_ACTIVITY_LIST_SAMPLE).returns(FAKE_GEOJSON_RESULT)

            all_available_activities = self.find_activities_action.execute(filter)

            expect(all_available_activities).to(equal(FAKE_GEOJSON_RESULT))
