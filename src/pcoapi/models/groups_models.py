from __future__ import annotations

from typing import Optional

from pcoapi.models.base_models import (
    PcoBaseAttributesModel,
    PcoBaseLinksModel,
    PcoBaseModel,
    PcoBaseRelationshipsModel,
)


class PcoGroupsEventAttributesModel(PcoBaseAttributesModel):
    attendance_requests_enabled: bool
    automated_reminder_enabled: bool
    canceled: bool
    canceled_at: Optional[str]
    description: Optional[str]
    ends_at: Optional[str]
    location_type_preference: Optional[str]
    multi_day: bool
    name: str
    reminders_sent: bool
    reminders_sent_at: Optional[str]
    repeating: bool
    starts_at: Optional[str]
    virtual_location_url: Optional[str]
    visitors_count: int


class PcoGroupsEventRelationshipsModel(PcoBaseRelationshipsModel):
    attendance_submitter: PcoBaseModel
    group: PcoBaseModel
    location: PcoBaseModel
    repeating_event: PcoBaseModel


class PcoGroupsEventLinksModel(PcoBaseLinksModel):
    attendance_recording: Optional[str]
    attendances: str
    group: str
    location: str
    notes: str
    self: str


class PcoGroupsEventModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupsEventAttributesModel
    relationships: PcoGroupsEventRelationshipsModel
    links: PcoGroupsEventLinksModel


class PcoGroupsAttributesModel(PcoBaseAttributesModel):
    archived_at: Optional[str]
    contact_email: Optional[str]
    created_at: str
    description: Optional[str]
    events_visibility: str
    location_type_preference: Optional[str]
    name: str
    membership_count: int
    public_church_center_web_url: Optional[str]
    schedule: str
    virtual_location_url: Optional[str]


class PcoGroupsRelationshipsModel(PcoBaseRelationshipsModel):
    group_type: PcoBaseModel
    location: PcoBaseModel


class PcoGroupsLinksModel(PcoBaseLinksModel):
    enrollment: str
    events: str
    group_type: str
    location: str
    memberships: str
    people: str
    resources: str
    tags: str
    self: str
    html: str


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
    description: Optional[str]
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
    display_publicly: bool
    multiple_options_enabled: bool
    name: str
    position: int


class PcoGroupTagsLinksModel:
    tags: str
    self: str


class PcoGroupTagsModel(PcoBaseModel):
    type: str
    id: str
    attributes: PcoGroupTagsAttributesModel
    links: PcoGroupTagsLinksModel
