# -*- coding: utf-8 -*-

import json
from flask import Flask, request

from activity_finder.actions import factory as actions_factory

app = Flask(__name__)

@app.route("/activity/find")
def find_activities():
    filter = build_filter_from_query_params(['category', 'location', 'district'])
    activities = actions_factory.find_activities_action().execute(filter)
    return json.dumps(activities)

@app.route("/activity/recommend")
def recommend_activity():
    filter = build_filter_from_query_params(['date', 'start_time', 'finish_time', 'category'])
    activities = actions_factory.recommend_activity_action().execute(filter)
    return json.dumps(activities)

def build_filter_from_query_params(expected_params_names):
    result_filter = {}
    for params_name in expected_params_names:
        params_value = request.args.get(params_name)
        if params_value is not None:
            result_filter[params_name] = params_value
    if result_filter.keys():
        return result_filter
