#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta

import pytest

from PcoApi.PcoApi import Event, PcoApi

LOGGER = logging.getLogger(__name__)


def test_request_test(setup_real_api: PcoApi):
    last_sunday_date = datetime.fromisoformat("2023-06-24T22:00:00Z")
    api = setup_real_api
    sunday_auckland_event = Event(73626, "Sunday Auckland", api)
    last_sunday_auckland_event_periods = sunday_auckland_event.get_event_period_by_date(last_sunday_date)
    last_sunday_auckland_event_times = last_sunday_auckland_event_periods.get_event_times()
    morning_service_headcount = last_sunday_auckland_event_times[0].get_headcounts()
    evening_service_headcount = last_sunday_auckland_event_times[1].get_headcounts()
    print(f"Morning Service: {morning_service_headcount}")
    print(f"Evening Service: {evening_service_headcount}")


def hello_test():
    """
    This defines the expected usage, which can then be used in various test cases.
    Pytest will not execute this code directly, since the function does not contain the suffex "test"
    """
    pass


def test_hello(unit_test_mocks: None):
    """
    This is a simple test, which can use a mock to override online functionality.
    unit_test_mocks: Fixture located in conftest.py, implicitly imported via pytest.
    """
    hello_test()


def test_int_hello():
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    hello_test()


@pytest.mark.integration
def test_integrtion():
    """
    This is an integration test
    """
    pass
