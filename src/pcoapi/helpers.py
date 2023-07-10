#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from __future__ import annotations

import sys
from typing import Dict, List, TypedDict, TypeVar, Union

from pcoapi.models import PcoBaseModel

if sys.version_info >= (3, 10):
    # noinspection PyCompatibility
    JsonValueType = (
        Dict[str, "JsonValueType"] | List["JsonValueType"] | str | int | float | bool | None
    )
else:
    JsonValueType = Union[
        Dict[str, "JsonValueType"], List["JsonValueType"], str, int, float, bool, None
    ]
"""Any data that can be returned by the standard JSON deserializing process."""
JsonArrayType = List[JsonValueType]
"""List that can be returned by the standard JSON deserializing process."""
JsonObjectType = Dict[str, JsonValueType]
"""Dictionary that can be returned by the standard JSON deserializing process."""


class PcoDataType(TypedDict):
    type: str
    id: str
    attributes: dict[str, object]
    links: dict[str, str]


class PcoMetaType(TypedDict):
    total_count: int
    count: int
    next: dict[str, str | int]
    can_order_by: list[str]
    can_query_by: list[str]
    can_include: list[str]
    parent: dict[str, str]


class PcoResponseType(TypedDict):
    links: dict[str, str]
    data: list[PcoDataType] | PcoDataType
    included: list[PcoDataType]
    meta: PcoMetaType


T_Model = TypeVar("T_Model", bound=PcoBaseModel)


def convert_response_data_to_list_of_model(
    response: PcoResponseType, model_class: type[T_Model]
) -> list[T_Model]:
    if "data" not in response.keys():
        raise ValueError("Response does not contain data.")
    assert isinstance(response["data"], list)
    return [model_class(**item) for item in response["data"]]


def convert_response_data_to_model(
    response: PcoResponseType, model_class: type[T_Model]
) -> T_Model:
    if "data" not in response.keys():
        raise ValueError("Response does not contain data.")
    assert isinstance(response["data"], dict)
    return model_class(**response["data"])
