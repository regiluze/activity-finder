# -*- coding: utf-8 -*-

from doublex import *
from expects import *
from doublex_expects import *

import os
from activity_finder.infrastructure.repositories import LoadFromFileActivityRepository



BASE_PATH = os.path.abspath(os.path.dirname(__file__)) + '/test_resources'

with describe('Load data from file activity repository specs'):
    with before.each:
         pass
    with context('when finding all activities'):
        with it('returns three activities'):
            repository = LoadFromFileActivityRepository(file_path='{base_path}/test_activities_data.json'.format(base_path=BASE_PATH))

            activities = repository.find_by()

            expect(len(activities)).to(equal(3))

    with context('when filtering by category cultural'):
        with it('returns "Parque del Oeste" activity'):
            filter = {'category':'nature'}
            repository = LoadFromFileActivityRepository(file_path='{base_path}/test_activities_data.json'.format(base_path=BASE_PATH))

            activities = repository.find_by(filter)

            expect(len(activities)).to(equal(1))
            expect(activities[0]).to(have_keys(name='Parque del Oeste'))

    with context('when filtering by location indoors'):
        with it('returns "Museo Nacional del Prado" activity'):
            filter = {'location':'indoors'}
            repository = LoadFromFileActivityRepository(file_path='{base_path}/test_activities_data.json'.format(base_path=BASE_PATH))

            activities = repository.find_by(filter)

            expect(len(activities)).to(equal(1))
            expect(activities[0]).to(have_keys(name='Museo Nacional del Prado'))

    with context('when filtering by category "cultural" and district "Centro"'):
        with it('returns "Palacio Real" activity'):
            filter = {'category':'cultural', 'district':'Centro'}
            repository = LoadFromFileActivityRepository(file_path='{base_path}/test_activities_data.json'.format(base_path=BASE_PATH))

            activities = repository.find_by(filter)

            expect(len(activities)).to(equal(1))
            expect(activities[0]).to(have_keys(name='Palacio Real'))

