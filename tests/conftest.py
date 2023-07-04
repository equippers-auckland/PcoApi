#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""
This is a configuration file for pytest containing customizations and fixtures.

In VSCode, Code Coverage is recorded in config.xml. Delete this file to reset reporting.
"""

from __future__ import annotations

import json
from os import environ
from typing import Generator, TypedDict

from _pytest.nodes import Item
import pytest

from pcoapi.api import PcoApi
from pcoapi import JSONDict

from dotenv import load_dotenv

load_dotenv()


def pytest_collection_modifyitems(items: list[Item]) -> None:
    for item in items:
        if "spark" in item.nodeid:
            item.add_marker(pytest.mark.spark)
        elif "_int_" in item.nodeid:
            item.add_marker(pytest.mark.integration)


@pytest.fixture
def unit_test_mocks(monkeypatch: None) -> None:
    """Include Mocks here to execute all commands offline and fast."""
    pass


@pytest.fixture
def setup_real_api() -> PcoApi:
    yield PcoApi(application_id=environ["PCO_USER"], secret=environ["PCO_PASSWD"])


@pytest.fixture
def load_test_data(path: str) -> Generator[JSONDict, None, None]:
    with open(path, "r") as file:
        data = file.read()
    yield json.loads(data)
