import json
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class Item(BaseModel):
    description: str = Field(default="", validation_alias='shortDescription', pattern=r'^[\\w\\s\\-]+$')
    price: float = Field(default=0.00, pattern="^\\d+\\.\\d{2}$")

    @validator('description', pre=True)
    def validate_description(cls, value):
        return value.strip()

    @validator('price', pre=True)
    def validate_price(cls, value):
        return float(value)

    class Config:
        allow_population_by_field_name = True


class Receipt(BaseModel):
    id: Optional[str]
    retailer: str = Field(default="", pattern="^[\\w\\s\\-&]+$")
    purchaseDate: datetime
    purchaseTime: datetime
    items: List[Item]
    total: float = Field(default=0.00, pattern="^\\d+\\.\\d{2}$")
    points: Optional[float]

    @validator('purchaseDate', pre=True)
    def validate_purchase_date(cls, value):
        return datetime.strptime(value, "%Y-%m-%d")

    @validator('purchaseTime', pre=True)
    def validate_purchase_time(cls, value):
        return datetime.strptime(value, "%H:%M")

    @validator('total', pre=True)
    def validate_total(cls, value):
        return float(value)

    @validator('items', pre=True)
    def validate_items(cls, value):
        return [Item(**item) for item in value]

    class Config:
        allow_population_by_field_name = True
