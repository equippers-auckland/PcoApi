#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""Here all models will be tested."""
from __future__ import annotations

from typing import Callable

from pcoapi.helpers import JsonObjectType
from pcoapi.models import PcoListModel, PcoPersonModel


def test_list_model(load_test_data: Callable[[str], JsonObjectType]) -> None:
    test_json = load_test_data("tests/test_data/get_list.json")["data"]
    test_model = PcoListModel(**test_json)  # type: ignore[arg-type]
    assert test_model.id == "1234"


def test_person_model(load_test_data: Callable[[str], JsonObjectType]) -> None:
    test_json = load_test_data("tests/test_data/get_person.json")["data"]
    test_model = PcoPersonModel(**test_json)  # type: ignore[arg-type]
    assert test_model.id == "1234"
