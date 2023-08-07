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
from unittest.mock import patch

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
def setup_mocked_api() -> Generator[PcoApi, None, None]:
    with patch("pcoapi.pypco_wrapper.pypco.PCO", autospec=True) as mock_pypco_pco:
        pcoapi_instance = PcoApi(application_id="1234", secret="5678")
        pcoapi_instance.api = mock_pypco_pco.return_value
    yield pcoapi_instance


@pytest.fixture
def load_test_data() -> Callable[[Path], JsonObjectType]:
    def open_dest_data(path: Path) -> JsonObjectType:
        # if current folder is tests, then go up one level
        if Path.cwd().name == "tests":
            path = Path.cwd().parent / path
        with Path(path).open() as f:
            data = json.load(f)
        return data  # type: ignore

    return open_dest_data
