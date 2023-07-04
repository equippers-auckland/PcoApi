#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from .pypco_wrapper import PyPcoWrapper
from .models import PcoList


class People:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi
        self.lists = Lists(self.api)


class Lists:
    """All methods for the PCO API Lists endpoint"""

    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_most_recent(self) -> object:
        """
        Requests the 25 most recently updated lists from the PCO API
        """
        data = self.api.get("/people/v2/lists?order=-updated_at")
        return [PcoList.new_from_json_dict(item) for item in data["data"]]

    def get_by_id(self, list_id: int) -> object:
        """
        Requests a list from the PCO API
        """
        return self.api.get(f"/people/v2/lists/{list_id}")

    def get_people_by_id(self, list_id: int) -> object:
        """
        Requests the people in a list from the PCO API
        """
        return self.api.get(f"/people/v2/lists/{list_id}/people")
