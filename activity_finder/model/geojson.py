# -*- coding: utf-8 -*-

from geojson import Feature, Point, FeatureCollection

class GeoJsonFormater(object):

    def to_feature_collection(self, entities):
        features = [self.to_feature(entity) for entity in entities]
        return FeatureCollection(features)

    def to_feature(self, entity):
        return Feature(geometry=Point((entity.long, entity.lat)), properties=entity.properties)

