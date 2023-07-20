#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a sample python file for testing functions from the source code."""
from __future__ import annotations

from datetime import datetime
import logging

import pytest

from pcoapi.api import PcoApi

LOGGER = logging.getLogger(__name__)


@pytest.mark.skip
def test_request_test(setup_real_api: PcoApi) -> None:
    datetime.fromisoformat("2023-06-24T22:00:00Z")
    api = setup_real_api
    api.checkins.events.get_by_id(73626)


@pytest.mark.skip
def test_lists(setup_real_api: PcoApi) -> None:
    api = setup_real_api
    lists = api.people.lists.get_most_recent()
    print(lists)


def hello_test() -> None:
    """
    This defines the expected usage, which can then be used in various test cases. Pytest will
    not execute this code directly, since the function does not contain the suffix "test"
    """
    pass


def test_hello(unit_test_mocks: None) -> None:
    """
    This is a simple test, which can use a mock to override online functionality.
    unit_test_mocks: Fixture located in conftest.py, implicitly imported via pytest.
    """
    hello_test()


def test_int_hello() -> None:
    """
    This test is marked implicitly as an integration test because the name contains "_init_"
    https://docs.pytest.org/en/6.2.x/example/markers.html#automatically-adding-markers-based-on-test-names
    """
    hello_test()


@pytest.mark.integration
def test_integration() -> None:
    """
    This is an integration test
    """
    pass
