#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains all data classes. """

from __future__ import annotations

import json
from typing import Any


class PcoModel(object):

    def __init__(self, **kwargs) -> None:
        self.param_defaults: dict[str, int | bool | str | None] = {}

    @classmethod
    def new_from_json_dict(cls, json_dict: dict[str, object], **kwargs) -> PcoModel:
        json_data = json_dict.copy()
        if kwargs:
            for key, value in kwargs.items():
                json_data[key] = value
        if json_data["data"]["id"]:
            json_data["id"] = json_data["data"]["id"]

        if json_data["data"]["attributes"]:
            for key, value in json_data["data"]["attributes"].items():
                json_data[key] = value
        c: cls = cls(**json_data)
        c.__json = json_dict
        return c


class PcoList(PcoModel):
    def __init__(self, **kwargs):
        self.param_defaults = {
            "id": None,
            "auto_refresh": None,
            "automations_active": None,
            "automations_count": None,
            "batch_completed_at": None,
            "created_at": None,
            "description": None,
            "has_inactive_results": None,
            "include_inactive": None,
            "invalid": None,
            "name": None,
            "name_or_description": None,
            "paused_automations_count": None,
            "recently_viewed": None,
            "refreshed_at": None,
            "return_original_if_none": None,
            "returns": None,
            "starred": None,
            "status": None,
            "subset": None,
            "total_people": None,
            "updated_at": None
        }
        self.id: str | None = None
        self.auto_refresh: bool | None = None
        self.automations_active: bool | None = None
        self.automations_count: int | None = None
        self.batch_completed_at: str | None = None
        self.created_at: str | None = None
        self.description: str | None = None
        self.has_inactive_results: bool | None = None
        self.include_inactive: bool | None = None
        self.invalid: bool | None = None
        self.name: str | None = None
        self.name_or_description: str | None = None
        self.paused_automations_count: int | None = None
        self.recently_viewed: bool | None = None
        self.refreshed_at: str | None = None
        self.return_original_if_none: bool | None = None
        self.returns: str | None = None
        self.starred: bool | None = None
        self.status: str | None = None
        self.subset: str | None = None
        self.total_people: int | None = None
        self.updated_at: str | None = None

        for (param, default) in self.__dict__.items():
            setattr(self, param, kwargs.get(param, default))
