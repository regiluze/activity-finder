# -*- coding: utf-8 -*-

from geojson import Feature, Point, FeatureCollection

class GeoJsonFormater(object):

    def to_feature_collection(self, entities):
        features = [Feature(geometry=Point((entity.lat, entity.long)), properties=entity.properties) for entity in entities]
        return FeatureCollection(features)

