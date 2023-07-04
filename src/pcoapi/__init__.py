from __future__ import annotations

__version__ = "0.0.2"

from typing import Dict, List, TypeAlias, Union

from .api import PcoApi

JSONDict: TypeAlias = Union[Dict[str, "Json"], List["Json"], str, int, float, bool, None]
