#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""Here all models will be tested."""
from __future__ import annotations

from typing import Callable

from pcoapi import JSONDict
from pcoapi.models import PcoList, PcoModel


def test_pcomodel() -> None:
    """Test the PCOModel class."""
    model = PcoModel()
    assert model is not None
    assert model.param_defaults == {}
    test_data = {"test": "data"}
    returned_test_data = model.new_from_json_dict(test_data)
    assert returned_test_data.param_defaults == {}
    assert returned_test_data.__class__ == PcoModel


def test_list_model(load_test_data: Callable[[str], JSONDict]) -> None:
    test_list = load_test_data("test_data/get_list.json")
    return_data: PcoList = PcoList.new_from_json_dict(test_list)
    assert return_data is not None
    assert return_data.id == test_list["data"]["id"]
    for key, value in test_list["data"]["attributes"].items():
        if key == "doesnt_exist":
            assert not hasattr(return_data, key)
        else:
            assert getattr(return_data, key) == value
