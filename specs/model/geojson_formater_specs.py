# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

from activity_finder.model.geojson import GeoJsonFormater


class FakeEntity(object):

    def __init__(self, coordinates, properties):
        self._coordinates = coordinates
        self._properties = properties

    @property
    def lat(self):
        return self._coordinates[0]

    @property
    def long(self):
        return self._coordinates[1]

    @property
    def properties(self):
        return self._properties



with describe('geojson formater specs'):
    with before.each:
        self.formater = GeoJsonFormater()

    with context('when formating to a feature collection'):
        with it('returns a geoJson format feature collection'):

            geoJson_result = self.formater.to_feature_collection([])

            expect(geoJson_result).to(have_keys(type='FeatureCollection'))

        with context('when formating a list of entities'):
            with it('returns formated feature collection with entities as feature'):
                entity_list = [FakeEntity(coordinates=[1, 2], properties={'foo': 'var'})]

                geoJson_result = self.formater.to_feature_collection(entity_list)

                expect(geoJson_result.get('features')).to(contain_only(have_keys(type='Feature',
                                                                                 geometry=have_keys(type='Point', coordinates=contain_exactly(1, 2)),
                                                                                 properties=equal({'foo':'var'}))))

    with context('when formating to a feature'):
        with it('returns a geoJson format feature'):

            geoJson_result = self.formater.to_feature(FakeEntity(coordinates=[1, 2], properties={'foo': 'var'}))

            expect(geoJson_result).to(have_keys(type='Feature'))

        with it('returns formated entity feature'):
            geoJson_result = self.formater.to_feature(FakeEntity(coordinates=[1, 2], properties={'foo': 'var'}))

            expect(geoJson_result).to(have_keys(type='Feature',
                                                geometry=have_keys(type='Point', coordinates=contain_exactly(1, 2)),
                                                properties=equal({'foo':'var'})))
