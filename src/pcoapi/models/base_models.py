from __future__ import annotations

from pydantic import BaseModel as PydanticBaseModel


class PcoBaseModel(PydanticBaseModel):
    pass


class PcoBaseDataModel(PcoBaseModel):
    type: str
    id: str


class PcoBaseAttributesModel(PydanticBaseModel):
    pass


class PcoBaseRelationshipsModel(PydanticBaseModel):
    pass


class PcoBaseLinksModel(PydanticBaseModel):
    self: str
