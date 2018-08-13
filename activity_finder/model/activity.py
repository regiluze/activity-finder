# -*- coding: utf-8 -*-

import datetime
import calendar

class Activity(object):

    def __init__(self, **kwargs):
        self._latlng = kwargs['latlng']
        del kwargs['latlng']
        self._properties = kwargs
        self._opening_hours = kwargs['opening_hours']
        self._hours_spent = kwargs['hours_spent']

    @property
    def lat(self):
        return self._latlng[0]

    @property
    def long(self):
        return self._latlng[1]

    @property
    def properties(self):
        return self._properties

    def is_open_at(self, weekday, start_time, finish_time):
        if self._is_open_on_weekday(weekday) and self._time_is_before_or_the_same(self._get_open_time_on_weekday(weekday), start_time) and self._time_is_before_or_the_same(finish_time, self._get_close_time_on_weekday(weekday)) and self._time_range_bigger_than_activity_hours(start_time, finish_time):
             return True
        return False

    def _is_open_on_weekday(self, weekday):
        return len(self._opening_hours[weekday.lower()[:2]]) > 0

    def _get_open_time_on_weekday(self, weekday):
        weekday_opening_hours = self._opening_hours[weekday.lower()[:2]]
        return weekday_opening_hours[0].split('-')[0]

    def _get_close_time_on_weekday(self, weekday):
        weekday_opening_hours = self._opening_hours[weekday.lower()[:2]]
        return weekday_opening_hours[0].split('-')[1]

    def _time_is_before_or_the_same(self, time1, time2):
        time_absolute_minutes_1 = self._get_time_in_absolute_minutes(time1)
        time_absolute_minutes_2 = self._get_time_in_absolute_minutes(time2)
        return time_absolute_minutes_1 <= time_absolute_minutes_2

    def _time_range_bigger_than_activity_hours(self, start_time, finish_time):
        start_time_absolute_minutes = self._get_time_in_absolute_minutes(start_time)
        finish_time_absolute_minutes = self._get_time_in_absolute_minutes(finish_time)
        activity_hours_spent_minutes = self._hours_spent*60
        return (finish_time_absolute_minutes - start_time_absolute_minutes) > activity_hours_spent_minutes

    def _get_time_in_absolute_minutes(self, time):
        return int(time.split(':')[0])*60 + int(time.split(':')[1])


class ActivitiesService(object):

    def __init__(self, activities_repository):
        self._activities_repository = activities_repository


    def find_by(self, filter=None):
        activities = self._activities_repository.find_by(filter)
        return [Activity(**activity) for activity in activities]

    def recommend_activity(self, filter):
        activities = self.find_by({'category':filter['category']})
        date = datetime.datetime.strptime(filter['date'], '%d/%m/%Y').date()
        weekday = calendar.day_name[date.weekday()]
        recommended_activities = [activity for activity in activities if activity.is_open_at(weekday, filter['start_time'], filter['finish_time'])]
        recommended_activities.sort(key=lambda x: x.properties['hours_spent'], reverse=True)
        if recommended_activities:
            return recommended_activities[0]
        else:
            raise NotFoundRecommendationError()


class NotFoundRecommendationError(Exception):
    pass
