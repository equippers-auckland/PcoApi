#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from pcoapi.helpers import convert_response_data_to_list_of_model, convert_response_data_to_model
from pcoapi.models.checkins_models import (
    PcoAttendanceTypesModel,
    PcoEventsModel,
    PcoEventTimesHeadcountModel,
    PcoEventTimesModel,
)
from pcoapi.pypco_wrapper import PyPcoWrapper


class CheckIns:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi
        self.events = Events(self.api)
        self.event_times = EventTimes(self.api)


class EventTimes:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_most_recent(self) -> list[PcoEventTimesModel]:
        """
        Requests the 25 most recent Event_times from the PCO API
        """
        response = self.api.get("/check-ins/v2/event_times?order=-starts_at")
        filled_data_model = convert_response_data_to_list_of_model(response, PcoEventTimesModel)
        return filled_data_model

    def get_by_id(self, event_time_id: int) -> PcoEventTimesModel:
        response = self.api.get(f"/check-ins/v2/event_times/{event_time_id}")
        filled_data_model = convert_response_data_to_model(response, PcoEventTimesModel)
        return filled_data_model

    def get_headcounts_by_id(self, event_time_id: int) -> list[PcoEventTimesHeadcountModel]:
        response = self.api.get(f"/check-ins/v2/event_times/{event_time_id}/headcounts")
        filled_data_model = convert_response_data_to_list_of_model(
            response, PcoEventTimesHeadcountModel
        )
        return filled_data_model


class Events:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, event_id: int) -> PcoEventsModel:
        response = self.api.get(f"/check-ins/v2/events/{event_id}")
        filled_data_model = convert_response_data_to_model(response, PcoEventsModel)
        return filled_data_model

    def get_attendance_types(self, event_id: int) -> list[PcoAttendanceTypesModel]:
        response = self.api.get(f"/check-ins/v2/events/{event_id}/attendance_types")
        filled_data_model = convert_response_data_to_list_of_model(
            response, PcoAttendanceTypesModel
        )
        return filled_data_model
