from dataclasses import dataclass
from datetime import datetime


@dataclass
class FuelRefill:
    id: int
    vehicle_id: int
    date: datetime
    distance: float
    liters: float
    price: float
    station: str = ""
