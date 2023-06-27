"""
This implements all required enpdoints for the PCO API
"""
from __future__ import annotations
from typing import Optional, List
from PcoApi.pypco_wrapper import PyPcoWrapper
from datetime import datetime
from dataclasses import dataclass


class PcoApi(PyPcoWrapper):
    """
    This class implements all required endpoints for the PCO API
    """

    def __init__(
        self,
        application_id: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        secret: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        token: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        cc_name: Optional[str] = None,  # pylint: disable=unsubscriptable-object
        api_base: str = "https://api.planningcenteronline.com",
        timeout: int = 60,
        upload_url: str = "https://upload.planningcenteronline.com/v2/files",
        upload_timeout: int = 300,
        timeout_retries: int = 3,
    ):
        super().__init__(
            application_id=application_id,
            secret=secret,
            token=token,
            cc_name=cc_name,
            api_base=api_base,
            timeout=timeout,
            upload_url=upload_url,
            upload_timeout=upload_timeout,
            timeout_retries=timeout_retries,
        )


@dataclass
class AttendanceType:
    """
    This is an Attendance Type, eg. "Sparks", "Theatre"
    """

    id: int
    name: str


@dataclass
class Headcount:
    """
    This represents a Headcount
    """

    id: int
    attendance_type: AttendanceType
    count: int


class Event:
    """
    This is an Event, eg. Auckland Sunday. It can be a recurring event.
    """

    def __init__(self, id: int, name: str, api: PcoApi):
        self.id = id
        self.name = name
        self.api = api

    def get_attendance_types(self) -> dict:
        """
        Get the attendance types for an event
        """
        response = self.api.get(f"/check-ins/v2/events/{self.id}/attendance_types")
        attendance_types = {}
        for attendance_type in response["data"]:
            type_id = attendance_type["id"]
            name = attendance_type["attributes"]["name"]
            attendance_types[type_id] = AttendanceType(type_id, name)
        return attendance_types

    def get_event_periods(self) -> list[EventPeriod]:
        """
        Get the event periods for an event
        """
        response = self.api.get(f"/check-ins/v2/events/{self.id}/event_periods?order=-starts-at")
        event_periods = []
        for event_period in response["data"]:
            start_date = datetime.fromisoformat(event_period["attributes"]["starts_at"])
            end_date = datetime.fromisoformat(event_period["attributes"]["ends_at"])
            event_periods.append(
                EventPeriod(
                    event_period["id"],
                    start_date,
                    end_date,
                    event_period["attributes"]["guest_count"],
                    event_period["attributes"]["regular_count"],
                    event_period["attributes"]["volunteer_count"],
                    self,
                    self.api,
                )
            )
        return event_periods

    def get_event_period_by_date(self, date: datetime) -> EventPeriod:
        """
        Get the event period for an event by date
        """
        event_periods = self.get_event_periods()
        for event_period in event_periods:
            if event_period.starts_at.date() == date.date():
                return event_period
        raise ValueError(f"No event period found for date {date.date()}")


class EventPeriod:
    """
    This is an single Event Period or Instance of an reacurring event.
    """

    def __init__(
        self,
        id: int,
        starts_at: datetime,
        ends_at: datetime,
        guest_count: int,
        regular_count: int,
        volunteer_count: int,
        event: Event,
        api: PcoApi,
    ):
        self.id = id
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.guest_count = guest_count
        self.regular_count = regular_count
        self.volunteer_count = volunteer_count
        self.event = event
        self.api = api

    def get_event_times(self) -> list:
        response = self.api.get(f"/check-ins/v2/events/{self.event.id}/event_periods/{self.id}/event_times")
        event_times = []
        for event_time in response["data"]:
            event_times.append(
                EventTime(
                    event_time["id"],
                    event_time["attributes"]["starts_at"],
                    self,
                    self.api,
                )
            )
        return event_times


class EventTime:
    """
    This is the excapt Time of an Event Period
    """

    def __init__(self, id: int, starts_at: datetime, event_period: EventPeriod, api: PcoApi):
        self.id = id
        self.starts_at = starts_at
        self.event_period = event_period
        self.api = api

    def get_headcounts(self) -> dict:
        """
        Get the headcounts for an event time
        """
        response = self.api.get(f"/check-ins/v2/event_times/{self.id}?include=headcounts")
        fetched_headcounts = response["included"]
        attendance_types = self.event_period.event.get_attendance_types()
        headcounts = {}

        for headcount in fetched_headcounts:
            attendance_type_id = headcount["relationships"]["attendance_type"]["data"]["id"]
            attendance_type = attendance_types[attendance_type_id]
            count = headcount["attributes"]["total"]
            headcount = Headcount(id, attendance_type, count)
            headcounts[attendance_type.id] = headcount

        return headcounts
