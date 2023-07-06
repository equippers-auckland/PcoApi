#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from pcoapi.models import PcoListModel, PcoPersonModel
from pcoapi.pypco_wrapper import PyPcoWrapper


class People:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi
        self.lists = Lists(self.api)


class Lists:
    """All methods for the PCO API Lists endpoint"""

    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_most_recent(self) -> list[PcoListModel]:
        """
        Requests the 25 most recently updated lists from the PCO API
        """
        response = self.api.get("/people/v2/lists?order=-updated_at")
        return [PcoListModel(**single_list) for single_list in response["data"]]

    def get_by_id(self, list_id: int) -> PcoListModel:
        """
        Requests a list from the PCO API
        """
        response = self.api.get(f"/people/v2/lists/{list_id}")
        return PcoListModel(**response["data"])

    def get_people_by_id(self, list_id: int) -> list[PcoPersonModel]:
        """
        Requests the people in a list from the PCO API
        """
        response = self.api.get(f"/people/v2/lists/{list_id}/people")
        return [PcoPersonModel(**single_person) for single_person in response["data"]]
