#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""Here all models will be tested."""
from __future__ import annotations

import pytest

from pcoapi.helpers import (
    PcoResponseType,
    convert_response_data_to_list_of_model,
    convert_response_data_to_model,
)
from pcoapi.models import PcoBaseDataModel

json_data: PcoResponseType = {
    "data": {"type": "Person", "id": "123456789", "this": "that"}
}  # type: ignore

json_without_data: PcoResponseType = {
    "type": "Person",
    "id": "123456789",
}  # type: ignore

json_as_list: PcoResponseType = {
    "data": [
        {"type": "Person", "id": "123456789", "this": "that"},
        {"type": "Person", "id": "987654321", "this": "that"},
    ]
}  # type: ignore


class TestModelConvert:
    def test_convert_response_data_to_model(self) -> None:
        model = convert_response_data_to_model(json_data, PcoBaseDataModel)
        assert model.id == "123456789"
        assert model.type == "Person"

    def test_convert_response_data_to_model_without_data(self) -> None:
        with pytest.raises(ValueError):
            convert_response_data_to_model(json_without_data, PcoBaseDataModel)

    def test_convert_response_data_to_list_of_model(self) -> None:
        model = convert_response_data_to_list_of_model(json_as_list, PcoBaseDataModel)
        assert model[0].id == "123456789"
        assert model[0].type == "Person"
        assert model[1].id == "987654321"
        assert model[1].type == "Person"

    def test_convert_response_data_to_list_of_model_without_data(self) -> None:
        with pytest.raises(ValueError):
            convert_response_data_to_list_of_model(json_without_data, PcoBaseDataModel)
