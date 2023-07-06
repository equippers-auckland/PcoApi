#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains the PcoApi People class. """

from __future__ import annotations

from pcoapi.models import PcoAttendanceTypesModel, PcoEventsModel, PcoEventTimesModel
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
        return [PcoEventTimesModel(**single_event) for single_event in response["data"]]

    def get_by_id(self, event_time_id: int) -> PcoEventTimesModel:
        response = self.api.get(f"/check-ins/v2/event_times/{event_time_id}")
        return PcoEventTimesModel(**response["data"])


class Events:
    def __init__(self, pcoapi: PyPcoWrapper) -> None:
        self.api = pcoapi

    def get_by_id(self, event_id: int) -> PcoEventsModel:
        response = self.api.get(f"/check-ins/v2/events/{event_id}")
        return PcoEventsModel(**response["data"])

    def get_attendance_types(self, event_id: int) -> list[PcoAttendanceTypesModel]:
        response = self.api.get(f"/check-ins/v2/events/{event_id}/attendance_types")
        response_data = response["data"]
        return_list_object: list[PcoAttendanceTypesModel] = []
        for single_attendance_type in response_data:
            return_list_object.append(PcoAttendanceTypesModel(**single_attendance_type))
        return return_list_object
