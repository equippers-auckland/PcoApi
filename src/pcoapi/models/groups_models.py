from __future__ import annotations

from typing import Optional, Union

from pcoapi.models.base_models import (
    PcoBaseAttributesModel,
    PcoBaseDataModel,
    PcoBaseLinksModel,
    PcoBaseModel,
    PcoBaseRelationshipsModel,
)


class PcoGroupsEventAttributesModel(PcoBaseAttributesModel):
    attendance_requests_enabled: bool
    automated_reminder_enabled: bool
    canceled: bool
    canceled_at: Union[str, None]
    description: Union[str, None]
    ends_at: Union[str, None]
    location_type_preference: Union[str, None]
    multi_day: bool
    name: str
    reminders_sent: bool
    reminders_sent_at: Union[str, None]
    repeating: bool
    starts_at: Union[str, None]
    virtual_location_url: Union[str, None]
    visitors_count: Union[int, None]


class PcoGroupsEventRelationshipsModel(PcoBaseRelationshipsModel):
    attendance_submitter: PcoBaseModel
    group: PcoBaseModel
    location: PcoBaseModel
    repeating_event: PcoBaseModel


class PcoGroupsEventLinksModel(PcoBaseLinksModel):
    attendance_recording: Union[str, None] = None
    attendances: Union[str, None] = None
    group: Union[str, None] = None
    location: Union[str, None] = None
    notes: Union[str, None] = None
    self: str


class PcoGroupsEventModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupsEventAttributesModel
    relationships: PcoGroupsEventRelationshipsModel
    links: PcoGroupsEventLinksModel


class PcoGroupsEventAttendanceTotalsModel(PcoBaseModel):
    member: int
    leader: int
    visitor: int
    applicant: int


class PcoGroupsEventAttendanceRecordingAttrModel(PcoBaseAttributesModel):
    committed_at: Union[str, None]
    state: str
    attendance_totals: PcoGroupsEventAttendanceTotalsModel


class PcoGroupsEventAttendanceRecordingModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupsEventAttendanceRecordingAttrModel


class PcoGroupsAttributesModel(PcoBaseAttributesModel):
    archived_at: Union[str, None]
    contact_email: Union[str, None]
    created_at: str
    description: Union[str, None]
    events_visibility: str
    location_type_preference: Union[str, None]
    name: str
    memberships_count: int
    public_church_center_web_url: Union[str, None]
    schedule: Union[str, None]
    virtual_location_url: Union[str, None]


class PcoGroupsRelationshipsModel(PcoBaseRelationshipsModel):
    group_type: PcoBaseModel
    location: PcoBaseModel


class PcoGroupsLinksModel(PcoBaseLinksModel):
    self: str
    enrollment: Union[str, None] = None
    events: Union[str, None] = None
    group_type: Union[str, None] = None
    location: Union[str, None] = None
    memberships: Union[str, None] = None
    people: Union[str, None] = None
    resources: Union[str, None] = None
    tags: Union[str, None] = None
    html: Union[str, None] = None


class PcoGroupsMembershipAttributesModel(PcoBaseAttributesModel):
    joined_at: str
    role: str


class PcoGroupsMembershipModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupsMembershipAttributesModel
    links: PcoBaseLinksModel


class PcoGroupsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupsAttributesModel
    relationships: PcoGroupsRelationshipsModel
    links: PcoGroupsLinksModel


class PcoGroupTypesAttributesModel(PcoBaseAttributesModel):
    church_center_map_visible: bool
    church_center_visible: bool
    color: str
    description: Union[str, None]
    name: str
    position: int


class PcoGroupTypesLinksModel(PcoBaseLinksModel):
    self: str


class PcoGroupTypesModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupTypesAttributesModel
    links: PcoGroupTypesLinksModel


class PcoGroupTagsAttributesModel(PcoBaseAttributesModel):
    display_publicly: Union[bool, None] = None
    multiple_options_enabled: Union[bool, None] = None
    name: str
    position: int


class PcoGroupTagsLinksModel(PcoBaseModel):
    tags: Optional[str] = None
    self: str


class PcoGroupsTagsRelModel(PcoBaseRelationshipsModel):
    tag_group: PcoGroupsTagGroupDataModel


class PcoGroupsTagGroupDataModel(PcoBaseModel):
    data: PcoBaseDataModel


class PcoGroupTagsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupTagsAttributesModel
    links: PcoGroupTagsLinksModel
    relationships: PcoGroupsTagsRelModel
