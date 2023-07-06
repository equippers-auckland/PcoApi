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
from pathlib import Path
from typing import Callable, Generator

from _pytest.nodes import Item
from dotenv import load_dotenv
import pytest

from pcoapi.api import PcoApi
from pcoapi.helpers import JsonObjectType

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
def setup_real_api() -> Generator[PcoApi, None, None]:
    yield PcoApi(application_id=environ["PCO_USER"], secret=environ["PCO_PASSWD"])


@pytest.fixture
def load_test_data() -> Callable[[Path], JsonObjectType]:
    def open_dest_data(path: Path) -> JsonObjectType:
        with Path.open(path) as f:
            data = json.load(f)
        return data  # type: ignore

    return open_dest_data
