# -*- coding: utf-8 -*-

from geojson import Feature, Point, FeatureCollection

class GeoJsonFormater(object):

    def to_feature_collection(self, entities):
        features = [self.to_feature(entity) for entity in entities]
        return FeatureCollection(features)

    def to_feature(self, entity):
        if entity is not None:
            return Feature(geometry=Point((entity.lat, entity.long)), properties=entity.properties)

