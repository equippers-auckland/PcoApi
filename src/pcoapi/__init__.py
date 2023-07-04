from __future__ import annotations

__version__ = "0.0.2"

import sys
from typing import Dict, List, Union

if sys.version_info >= (3, 10):
    JsonValueType = (
        dict[str, "JsonValueType"] | list["JsonValueType"] | str | int | float | bool | None
    )
    JSONDict = dict[str, JsonValueType]
else:
    JSONDict = dict[str, object]
