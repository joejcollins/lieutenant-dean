"""Pydantic Union Demo"""
from enum import IntEnum, Enum

from pydantic import BaseModel, validator, Field
from typing import Optional


class RestrictedCode(IntEnum):
    """Enum for codes."""

    code_1 = 1
    code_2 = 2
    code_3 = 3


class RestrictedDescription(Enum):
    """Enum for descriptions."""

    description_1 = "One"
    description_2 = "Two"
    description_3 = "Three"


# region In Bound Models
class InBoundModelCode(BaseModel):
    """Data in model only the code."""

    name: str
    status_code: RestrictedCode


class InBoundModelDescription(BaseModel):
    """Data in model only the description."""

    name: str
    status_description: RestrictedDescription


class InBoundModelCodeOrDescription(BaseModel):
    """Data in model one or the other set but not both."""

    name: str
    status_code: Optional[RestrictedCode]
    status_description: Optional[RestrictedDescription]

    @validator("status_code", "status_description")
    def one_or_the_other_not_both(cls, v, values):
        """Ensure that either the code or the description are set but not both."""
        if values["status_code"] is None and values["status_description"] is None:
            raise ValueError("You have to set one.")
        if (
            values["status_code"] is not None
            and values["status_description"] is not None
        ):
            raise ValueError("You can't set both")
        return v


# end region


class OutBoundModelCamel(BaseModel):
    """Data out model."""

    name: str
    status_number: int = Field(alias="include_path")
    status_description: str


class OutBoundModelDescription(BaseModel):
    """Data out model."""

    name: str
    status_description: str


class OutBoundModelTwo(BaseModel):
    """Data out model."""

    name: str
    status_code: int
    status_description: str


class StorageModel(BaseModel):
    """Data storage model."""

    name: str
    status_code: int


# FIRST = InBoundModel(name="alice", status_code="1")

# print(FIRST.dict(exclude_none=True))

# SECOND = InBoundModel(name="bob")

# print(SECOND.dict(exclude_none=True))

# THIRD = InBoundModel(name="carol", status_code=5)

# print(THIRD.dict(exclude_none=True))
