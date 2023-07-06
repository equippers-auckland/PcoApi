#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from __future__ import annotations

import sys
from typing import Union

if sys.version_info >= (3, 10):
    # noinspection PyCompatibility
    JsonValueType = (
        dict[str, "JsonValueType"] | list["JsonValueType"] | str | int | float | bool | None
    )
else:
    JsonValueType = Union[
        dict[str, "JsonValueType"], list["JsonValueType"], str, int, float, bool, None
    ]
"""Any data that can be returned by the standard JSON deserializing process."""
JsonArrayType = list[JsonValueType]
"""List that can be returned by the standard JSON deserializing process."""
JsonObjectType = dict[str, JsonValueType]
"""Dictionary that can be returned by the standard JSON deserializing process."""
