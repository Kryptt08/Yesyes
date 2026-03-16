from pydantic import BaseModel
from typing import Optional


class PetOut(BaseModel):
    id: int
    name: str
    rarity: str
    value: str
    shiny_value: Optional[str]
    image_url: Optional[str]
    note: Optional[str]
    updated_at: str


class PetCreate(BaseModel):
    name: str
    rarity: str
    value: str = "0"
    shiny_value: Optional[str] = None
    image_url: Optional[str] = None
    note: Optional[str] = None


class PetUpdate(BaseModel):
    value: str
    shiny_value: Optional[str] = None
    image_url: Optional[str] = None
    note: Optional[str] = None
    reason: Optional[str] = None


class HistoryOut(BaseModel):
    id: int
    pet_id: int
    pet_name: str
    old_value: str
    new_value: str
    old_shiny: Optional[str]
    new_shiny: Optional[str]
    changed_by: str
    reason: Optional[str]
    changed_at: str
