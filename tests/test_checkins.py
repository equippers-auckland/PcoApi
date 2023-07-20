#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""Here all models will be tested."""
from __future__ import annotations

from unittest.mock import patch

from pcoapi.api import PcoApi
from pcoapi.helpers import GeneratorJsonType


class TestEventTimes:
    def test_get_by_id(self, load_test_data: GeneratorJsonType, setup_mocked_api: PcoApi) -> None:
        fake_response = load_test_data("tests/test_data/get_eventtime.json")
        api = setup_mocked_api
        with patch("pcoapi.pypco_wrapper.PyPcoWrapper.get") as mock_get:
            mock_get.return_value = fake_response
            event_time = api.checkins.event_times.get_by_id(1234)
            assert event_time.id == "1234"
            assert event_time.type == "EventTime"
            assert event_time.attributes.name == "My EventTime"

    def test_get_headcount_by_id(
        self, load_test_data: GeneratorJsonType, setup_mocked_api: PcoApi
    ) -> None:
        fake_response = load_test_data("tests/test_data/get_eventtime_headcounts.json")
        api = setup_mocked_api
        with patch("pcoapi.pypco_wrapper.PyPcoWrapper.get") as mock_get:
            mock_get.return_value = fake_response
            headcounts = api.checkins.event_times.get_headcounts_by_id(1234)
            assert headcounts[0].id == "6841882"
            assert headcounts[0].attributes.total == 3


class TestEvents:
    def test_get_by_id(self, load_test_data: GeneratorJsonType, setup_mocked_api: PcoApi) -> None:
        fake_response = load_test_data("tests/test_data/get_event.json")
        api = setup_mocked_api
        with patch("pcoapi.pypco_wrapper.PyPcoWrapper.get") as mock_get:
            mock_get.return_value = fake_response
            event = api.checkins.events.get_by_id(1234)
            assert event.id == "1234"
            assert event.type == "Event"
            assert event.attributes.name == ".North Shore Sunday"

    def test_get_attendance_types(
        self, load_test_data: GeneratorJsonType, setup_mocked_api: PcoApi
    ) -> None:
        fake_response = load_test_data("tests/test_data/get_event_attendance_types.json")
        api = setup_mocked_api
        with patch("pcoapi.pypco_wrapper.PyPcoWrapper.get") as mock_get:
            mock_get.return_value = fake_response
            attendance_types = api.checkins.events.get_attendance_types(1234)
            assert attendance_types[0].id == "17349"
            assert attendance_types[0].attributes.name == "(4) Prayer"
