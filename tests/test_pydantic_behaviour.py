#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module checks all helper functions. """
from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ValidationError
import pytest

from pcoapi.helpers import JsonObjectType


class AddressModel(PydanticBaseModel):
    street: str
    number: int


class NestedModel(PydanticBaseModel):
    name: str
    id: int
    address: AddressModel


class TestIsPydanticModelEqualToJson:
    @staticmethod
    def test_empty_json() -> None:
        empty_json: JsonObjectType = {}

        class EmptyModel(PydanticBaseModel):
            pass

        result = EmptyModel(**empty_json)
        assert len(result.model_fields) == 0

    @staticmethod
    def test_basic_json() -> None:
        basic_json: JsonObjectType = {"name": "Hans", "id": 1}

        class BasicModel(PydanticBaseModel):
            name: str
            id: int

        result = BasicModel(**basic_json)
        assert result.name == "Hans"
        assert result.id == 1

    @staticmethod
    def test_nested_json() -> None:
        nested_json: JsonObjectType = {
            "name": "Hans",
            "id": 1,
            "address": {"street": "Main Street", "number": 1},
        }

        result = NestedModel(**nested_json)
        assert result.name == "Hans"
        assert result.id == 1
        assert result.address.street == "Main Street"
        assert result.address.number == 1

    @staticmethod
    def test_bigger_json_than_class() -> None:
        bigger_json: JsonObjectType = {
            "name": "Hans",
            "id": 1,
            "address": {"street": "Main Street", "number": 1},
            "extra": "extra",
        }

        result = NestedModel(**bigger_json)
        assert result.name == "Hans"
        assert result.id == 1
        assert result.address.street == "Main Street"
        assert result.address.number == 1
        with pytest.raises(AttributeError):
            assert result.extra == "extra"  # type: ignore

    @staticmethod
    def test_smaller_json_than_class() -> None:
        smaller_json: JsonObjectType = {
            "name": "Hans",
            "id": 1,
        }
        with pytest.raises(ValidationError):
            NestedModel(**smaller_json)

    @staticmethod
    def test_smaller_nested_json_than_class() -> None:
        smaller_nested_json: JsonObjectType = {
            "name": "Hans",
            "id": 1,
            "address": {"street": "Main Street"},
        }
        with pytest.raises(ValidationError):
            NestedModel(**smaller_nested_json)

    @staticmethod
    def test_wrong_type_in_json() -> None:
        wrong_type_json: JsonObjectType = {
            "name": "Hans",
            "id": "1",
        }
        with pytest.raises(ValidationError):
            NestedModel(**wrong_type_json)

    @staticmethod
    def test_wrong_type_in_nested_json() -> None:
        wrong_type_nested_json: JsonObjectType = {
            "name": "Hans",
            "id": 1,
            "address": {"street": 1.12, "number": "1"},
        }
        with pytest.raises(ValidationError):
            NestedModel(**wrong_type_nested_json)
