import json
from datetime import datetime
from typing import List


class Item:
    description: str
    price: float

    def __init__(self, shortDescription: str, price: str):
        self.description = shortDescription.strip()
        self.price = float(price)


class Receipt:
    id: str
    retailer: str
    purchaseDate: datetime
    purchaseTime: datetime
    items: List[Item]
    total: float
    points: float

    def __init__(self, retailer: str, purchaseDate: str, purchaseTime: str, items: List[dict], total: str):
        self.retailer = retailer
        self.purchaseDate = datetime.strptime(purchaseDate, "%Y-%m-%d")
        self.purchaseTime = datetime.strptime(purchaseTime, "%H:%M")
        self.items = [Item(**item) for item in items]
        self.total = float(total)
        self.points = 0
        self.id = None
