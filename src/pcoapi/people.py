#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from pcoapi.helpers import convert_response_data_to_list_of_model, convert_response_data_to_model
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
        data_model = convert_response_data_to_list_of_model(response, PcoListModel)
        return data_model

    def get_by_id(self, list_id: int) -> PcoListModel:
        """
        Requests a list from the PCO API
        """
        response = self.api.get(f"/people/v2/lists/{list_id}")
        data_model = convert_response_data_to_model(response, PcoListModel)
        return data_model

    def get_people_by_id(self, list_id: int) -> list[PcoPersonModel]:
        """
        Requests the people in a list from the PCO API
        """
        response = self.api.get(f"/people/v2/lists/{list_id}/people")
        data_model = convert_response_data_to_list_of_model(response, PcoPersonModel)
        return data_model
