# -*- coding: utf-8 -*-


from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.model.activity import Activity, ActivitiesService


LAT = 40.4992
LONG = -3.732343


with describe('Activity entity specs'):
    with before.each:
        self.activity = Activity(name='El Rastro',
                                 opening_hours={'mo': [], 'tu':[], 'we':[], 'th':[], 'fr': [], 'sa': [], 'su': ['09:00-15:00']},
                                 hours_spent=2.5,
                                 category='shopping',
                                 location='outdoors',
                                 district='Centro',
                                 latlng=[LAT, LONG])

    with context('implementing geoJsonFormater api'):
        with context('when creating a new Activity'):
            with it('returns the lat'):

                expect(self.activity.lat).to(equal(LAT))

            with it('returns the long'):

                expect(self.activity.long).to(equal(LONG))

            with it('returns the properties'):

                expect(self.activity.properties).to(have_keys(name='El Rastro',
                                                              hours_spent=2.5,
                                                              category='shopping',
                                                              location='outdoors',
                                                              district='Centro'))

ACTIVITY_1 = {
        "name": "El Rastro",
        "opening_hours": {
            "mo": [],
            "tu": [],
            "we": [],
            "th": [],
            "fr": [],
            "sa": [],
            "su": ["09:00-15:00"]
            },
        "hours_spent": 2.5,
        "category": "shopping",
        "location": "outdoors",
        "district": "Centro",
        "latlng": [LAT,LONG]
}

ACTIVITY_2 = {
        "name": "Palacio Real",
        "opening_hours": {
            "mo": ["10:00-20:00"],
            "tu": ["10:00-20:00"],
            "we": ["10:00-20:00"],
            "th": ["10:00-20:00"],
            "fr": ["10:00-20:00"],
            "sa": ["10:00-20:00"],
            "su": ["10:00-20:00"]
        },
        "hours_spent": 1.5,
        "category": "cultural",
        "location": "outdoors",
        "district": "Centro",
        "latlng": [40.4173423,-3.7144063]
}

with describe('Activities service specs'):
    with before.each:
        self.activity_collection = [ACTIVITY_1, ACTIVITY_2]

        self.activities_repository_stub = Stub()
        when(self.activities_repository_stub).find_by(ANY_ARG).returns(self.activity_collection)

        self.activities_service = ActivitiesService(self.activities_repository_stub)

    with context('when there are two activities'):
        with context('when finding all activities'):
            with it('returns Activity class collection'):
                available_activities = self.activities_service.find_by()

                expect(available_activities[0]).to(be_a(Activity))

            with it('returns two activities'):
                available_activities = self.activities_service.find_by()

                expect(len(available_activities)).to(equal(2))

            with it('returns transformed data'):
                available_activities = self.activities_service.find_by()

                expect(available_activities[0]).to(have_properties(lat=LAT,
                                                                   long=LONG,
                                                                   properties=have_keys(name='El Rastro')))

        with context('when filtering by category "cultural"'):
            with it('returns "Palacio Real" activity'):
                when(self.activities_repository_stub).find_by({'category':'cultural'}).returns([ACTIVITY_2])
                available_activities = self.activities_service.find_by({'category':'cultural'})

                expect(available_activities).to(contain_only(have_properties(properties=have_keys(name='Palacio Real'))))

