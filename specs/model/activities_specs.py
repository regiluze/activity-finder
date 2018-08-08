# -*- coding: utf-8 -*-


from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.model.activity import Activity


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

