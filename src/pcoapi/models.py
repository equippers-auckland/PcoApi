#   ---------------------------------------------------------------------------------
#   Copyright (c) Equippers Church. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
""" This module contains all data classes. """

from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel


class PcoBaseModel(PydanticBaseModel):
    pass


class PcoBaseDataModel(PydanticBaseModel):
    type: str
    id: str


class PcoBaseAttributesModel(PydanticBaseModel):
    pass


class PcoBaseRelationshipsModel(PydanticBaseModel):
    pass


class PcoBaseLinksModel(PydanticBaseModel):
    self: str


class PcoListAttributesModelModel(PcoBaseAttributesModel):
    auto_refresh: bool
    automations_active: bool
    automations_count: int
    batch_completed_at: str
    created_at: str
    description: str
    has_inactive_results: bool
    include_inactive: bool
    invalid: bool
    name: str
    name_or_description: str
    paused_automations_count: int
    recently_viewed: bool
    refreshed_at: str
    return_original_if_none: bool
    returns: str
    starred: bool
    status: str
    subset: str
    total_people: int
    updated_at: str


class PcoListModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoListAttributesModelModel
    links: PcoBaseLinksModel


class PcoPersonAttributesModel(PcoBaseAttributesModel):
    accounting_administrator: bool
    anniversary: bool | None
    avatar: str
    birthdate: str
    can_create_forms: bool
    can_email_lists: bool
    child: bool
    created_at: str
    demographic_avatar_url: str
    directory_status: str
    first_name: str
    gender: str
    given_name: str | None
    grade: str | None
    graduation_year: str | None
    inactivated_at: str | None
    last_name: str
    medical_notes: str | None
    membership: str
    middle_name: str | None
    name: str
    nickname: str | None
    passed_background_check: bool
    people_permissions: str | None
    remote_id: str | None
    school_type: str | None
    site_administrator: bool
    status: str
    updated_at: str


class PcoPrimaryCampusModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoGenderModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoPersonRelationshipsModel(PcoBaseRelationshipsModel):
    primary_campus: PcoPrimaryCampusModel
    gender: PcoGenderModel


class PcoPersonLinksModel(PcoBaseLinksModel):
    self: str
    html: str


class PcoPersonModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoPersonAttributesModel
    relationships: PcoPersonRelationshipsModel
    links: PcoPersonLinksModel


class PcoEventsAttributesModel(PcoBaseAttributesModel):
    archived_at: str | None
    created_at: str
    enable_services_integration: bool
    frequency: str
    integration_key: str | None
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


class PcoEventPeriodsDataLinkModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoEventPeriodsAttributesModel(PcoBaseAttributesModel):
    created_at: str
    ends_at: str
    guest_count: int
    notes: str | None
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
    name: str | None
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


class PcoAttendanceTypeAttributesModel(PcoBaseAttributesModel):
    color: str
    created_at: str
    limit: int | None
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
