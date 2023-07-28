from __future__ import annotations

from typing import Union

from pcoapi.models.base_models import (
    PcoBaseAttributesModel,
    PcoBaseDataModel,
    PcoBaseLinksModel,
    PcoBaseModel,
    PcoBaseRelationshipsModel,
)


class PcoListAttributesModelModel(PcoBaseAttributesModel):
    auto_refresh: bool
    automations_active: bool
    automations_count: int
    batch_completed_at: Union[str, None]
    created_at: str
    description: str
    has_inactive_results: bool
    include_inactive: bool
    invalid: bool
    name: str
    name_or_description: str
    paused_automations_count: int
    recently_viewed: bool
    refreshed_at: Union[str, None]
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
    anniversary: Union[str, None]
    avatar: str
    birthdate: Union[str, None]
    can_create_forms: bool
    can_email_lists: bool
    child: bool
    created_at: str
    demographic_avatar_url: str
    directory_status: str
    first_name: str
    gender: Union[str, None]
    given_name: Union[str, None]
    grade: Union[int, None]
    graduation_year: Union[int, None]
    inactivated_at: Union[str, None]
    last_name: str
    medical_notes: Union[str, None]
    membership: Union[str, None]
    middle_name: Union[str, None]
    name: str
    nickname: Union[str, None]
    passed_background_check: bool
    people_permissions: Union[str, None]
    remote_id: Union[str, None]
    school_type: Union[str, None]
    site_administrator: bool
    status: str
    updated_at: str


class PcoPrimaryCampusModel(PcoBaseModel):
    data: Union[PcoBaseDataModel, None]


class PcoGenderModel(PcoBaseModel):
    data: Union[PcoBaseDataModel, None]


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
