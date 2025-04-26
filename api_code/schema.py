from enum import Enum
from pydantic import BaseModel
from pydantic import validator
from typing import Optional
from datetime import date, datetime


class UserGetLoginUserQuery(BaseModel):
    password: Optional[str] = None
    username: Optional[str] = None


class PetGetFindPetsByStatusQuery(BaseModel):
    status: Optional[str] = None


class PetGetFindPetsByTagsQuery(BaseModel):
    tags: Optional[list] = None


class PetPostUpdatePetWithFormQuery(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None


class PetPostUploadFileQuery(BaseModel):
    additionalMetadata: Optional[str] = None


class OrderStatusEnum(Enum):
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"


class PetStatusEnum(Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class Order(BaseModel):
    id: Optional[int] = None
    petId: Optional[int] = None
    quantity: Optional[int] = None
    shipDate: Optional[datetime] = None
    status: Optional[OrderStatusEnum] = None
    complete: Optional[bool] = None

    @validator("id")
    def optional_id(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("id may not be None")

    @validator("petId")
    def optional_petId(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("petId may not be None")

    @validator("quantity")
    def optional_quantity(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("quantity may not be None")

    @validator("shipDate")
    def optional_shipDate(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("shipDate may not be None")

    @validator("status")
    def optional_status(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("status may not be None")

    @validator("complete")
    def optional_complete(cls, val: bool):
        if val is not None:
            return val
        else:
            raise ValueError("complete may not be None")


class Category(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    @validator("id")
    def optional_id(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("id may not be None")

    @validator("name")
    def optional_name(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("name may not be None")


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    userStatus: Optional[int] = None

    @validator("id")
    def optional_id(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("id may not be None")

    @validator("username")
    def optional_username(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("username may not be None")

    @validator("firstName")
    def optional_firstName(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("firstName may not be None")

    @validator("lastName")
    def optional_lastName(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("lastName may not be None")

    @validator("email")
    def optional_email(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("email may not be None")

    @validator("password")
    def optional_password(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("password may not be None")

    @validator("phone")
    def optional_phone(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("phone may not be None")

    @validator("userStatus")
    def optional_userStatus(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("userStatus may not be None")


class Tag(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    @validator("id")
    def optional_id(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("id may not be None")

    @validator("name")
    def optional_name(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("name may not be None")


class ApiResponse(BaseModel):
    code: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None

    @validator("code")
    def optional_code(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("code may not be None")

    @validator("type")
    def optional_type(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("type may not be None")

    @validator("message")
    def optional_message(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("message may not be None")


class Pet(BaseModel):
    id: Optional[int] = None
    name: str
    category: Optional[Category] = None
    photoUrls: list
    tags: Optional[list[Tag]] = None
    status: Optional[PetStatusEnum] = None

    @validator("id")
    def optional_id(cls, val: int):
        if val is not None:
            return val
        else:
            raise ValueError("id may not be None")

    @validator("category")
    def optional_category(cls, val: Category):
        if val is not None:
            return val
        else:
            raise ValueError("category may not be None")

    @validator("tags")
    def optional_tags(cls, val: list):
        if val is not None:
            return val
        else:
            raise ValueError("tags may not be None")

    @validator("status")
    def optional_status(cls, val: str):
        if val is not None:
            return val
        else:
            raise ValueError("status may not be None")
