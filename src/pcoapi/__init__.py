from __future__ import annotations

__version__ = "0.0.2"

import sys
from typing import Union

if sys.version_info >= (3, 10):
    JSONDict = Union[dict[str, "JSONDict"], list["JSONDict"], str, int, float, bool, None]
else:
    JSONDict = dict[str, object]
