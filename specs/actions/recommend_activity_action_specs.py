# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.actions.recommend_activity import RecommendActivityAction
from activity_finder.model.activity import ActivitiesService
from activity_finder.model.geojson import GeoJsonFormater


FAKE_ACTIVITY_LIST_SAMPLE = ['irrelevant-activity']
FAKE_GEOJSON_RESULT = 'irrelevant-result'

with describe('recommend activity action specs'):
    with before.each:
        self.activities_service_stub = Stub(ActivitiesService)
        self.geoJson_formater = Stub(GeoJsonFormater)
        self.recommend_activity_action = RecommendActivityAction(self.activities_service_stub, self.geoJson_formater)

    with context('when asking a recommendation'):
        with it('returns recommended activity in geoJson format'):
            when(self.activities_service_stub).find_by({'category':'irrelevant'}).returns(FAKE_ACTIVITY_LIST_SAMPLE)
            when(self.geoJson_formater).to_feature(FAKE_ACTIVITY_LIST_SAMPLE).returns(FAKE_GEOJSON_RESULT)

            recommended_activity = self.recommend_activity_action.execute({'date':'09/08/2018', 'category':'irrelevant'})

            expect(recommended_activity).to(equal(FAKE_GEOJSON_RESULT))

