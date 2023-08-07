from __future__ import annotations

from typing import Union

from pcoapi.models.base_models import (
    PcoBaseAttributesModel,
    PcoBaseDataModel,
    PcoBaseLinksModel,
    PcoBaseModel,
    PcoBaseRelationshipsDataModel,
    PcoBaseRelationshipsModel,
)


class PcoEventsAttributesModel(PcoBaseAttributesModel):
    archived_at: Union[str, None]
    created_at: str
    enable_services_integration: bool
    frequency: str
    integration_key: Union[str, None]
    location_times_enabled: bool
    name: str
    pre_select_enabled: bool
    updated_at: str


class PcoEventsLinksModel(PcoBaseLinksModel):
    self: str
    html: str
    attendance_types: str
    check_ins: str
    current_event_times: str
    event_labels: str
    event_periods: str
    locations: str
    person_events: str


class PcoEventsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoEventsAttributesModel
    links: PcoEventsLinksModel


class PcoEventDataLinkModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoEventAttendanceTypesDataLinkModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoEventPeriodsDataLinkModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoEventPeriodsAttributesModel(PcoBaseAttributesModel):
    created_at: str
    ends_at: str
    guest_count: int
    note: Union[str, None]
    regular_count: int
    starts_at: str
    updated_at: str
    volunteer_count: int


class PcoEventPeriodsRelationshipsModel(PcoBaseRelationshipsModel):
    event: PcoEventDataLinkModel


class PcoEventPeriodsLinksModel(PcoBaseLinksModel):
    self: str


class PcoEventPeriodsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoEventPeriodsAttributesModel
    relationships: PcoEventPeriodsRelationshipsModel
    links: PcoEventPeriodsLinksModel


class PcoEventPeriodRelationshipsModel(PcoBaseRelationshipsModel):
    event: PcoEventDataLinkModel


class PcoEventTimesAttributesModel(PcoBaseAttributesModel):
    created_at: str
    day_of_week: int
    guest_count: int
    hides_at: str
    hour: int
    minute: int
    name: Union[str, None]
    regular_count: int
    shows_at: str
    starts_at: str
    total_count: int
    updated_at: str
    volunteer_count: int


class PcoEventTimesRelationshipsModel(PcoBaseRelationshipsModel):
    event: PcoEventDataLinkModel
    event_period: PcoEventPeriodsDataLinkModel


class PcoEventTimesLinksModel(PcoBaseLinksModel):
    self: str


class PcoEventTimesModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoEventTimesAttributesModel
    relationships: PcoEventTimesRelationshipsModel
    links: PcoEventTimesLinksModel


class PcoEventTimesHeadcountAttrModel(PcoBaseAttributesModel):
    created_at: str
    total: int
    updated_at: str


class PcoEventTimesHeadcountRelModel(PcoBaseRelationshipsModel):
    event_time: PcoEventDataLinkModel
    attendance_type: PcoEventAttendanceTypesDataLinkModel


class PcoEventTimesHeadcountLinksModel(PcoBaseLinksModel):
    self: str


class PcoEventTimesHeadcountModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoEventTimesHeadcountAttrModel
    relationships: PcoEventTimesHeadcountRelModel
    links: PcoEventTimesHeadcountLinksModel


class PcoAttendanceTypeAttributesModel(PcoBaseAttributesModel):
    color: str
    created_at: str
    limit: Union[int, None]
    name: str
    updated_at: str


class PcoAttendanceTypeRelationshipsModel(PcoBaseRelationshipsModel):
    event: PcoEventDataLinkModel


class PcoAttendanceTypeLinksModel(PcoBaseLinksModel):
    self: str


class PcoAttendanceTypesModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoAttendanceTypeAttributesModel
    relationships: PcoAttendanceTypeRelationshipsModel
    links: PcoAttendanceTypeLinksModel


class PcoEventPeriodCheckInsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoEventPeriodCheckInsAttrModel
    relationships: PcoEventPeriodCheckInsRelModel
    links: PcoBaseLinksModel


class PcoEventPeriodCheckInsAttrModel(PcoBaseAttributesModel):
    checked_out_at: Union[str, None]
    confirmed_at: Union[str, None]
    created_at: str
    emergency_contact_name: Union[str, None]
    emergency_contact_phone_number: Union[str, None]
    first_name: str
    last_name: str
    kind: str
    medical_notes: Union[str, None]
    number: Union[int, None]
    one_time_guest: bool
    security_code: Union[str, None]
    updated_at: str


class PcoEventPeriodCheckInsRelModel(PcoBaseRelationshipsModel):
    event_period: PcoEventPeriodsDataLinkModel
    person: PcoBaseRelationshipsDataModel
