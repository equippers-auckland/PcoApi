#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from pcoapi.helpers import convert_response_data_to_model
from pcoapi.models.groups_models import (
    PcoGroupsEventModel,
    PcoGroupsModel,
    PcoGroupTagsModel,
    PcoGroupTypesModel,
)
from pcoapi.pypco_wrapper import PyPcoWrapper


class TopLevelGroups:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi
        self.events = Events(self.api)
        self.groups = Groups(self.api)
        self.group_types = GroupTypes(self.api)
        self.tag_groups = TagGroups(self.api)


class Events:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, event_id: int) -> PcoGroupsEventModel:
        response = self.api.get(f"/groups/v2/events/{event_id}")
        filled_data_model = convert_response_data_to_model(response, PcoGroupsEventModel)
        return filled_data_model


class Groups:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, group_id: int) -> PcoGroupsModel:
        response = self.api.get(f"/groups/v2/groups/{group_id}")
        filled_data_model = convert_response_data_to_model(response, PcoGroupsModel)
        return filled_data_model


class GroupTypes:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, group_type_id: int) -> PcoGroupTypesModel:
        response = self.api.get(f"/groups/v2/group_types/{group_type_id}")
        filled_data_model = convert_response_data_to_model(response, PcoGroupTypesModel)
        return filled_data_model


class TagGroups:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, tag_group_id: int) -> PcoGroupTagsModel:
        response = self.api.get(f"/groups/v2/tag_groups/{tag_group_id}")
        filled_data_model = convert_response_data_to_model(response, PcoGroupTagsModel)
        return filled_data_model
