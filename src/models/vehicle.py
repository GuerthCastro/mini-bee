from dataclasses import dataclass, field

from src.models.fuel_refill import FuelRefill


@dataclass
class Vehicle:
    id: int
    brand: str
    model: str
    year: int
    initial_count: float
    license_plate: str
    is_miles: bool
    is_gallons: bool
    fuel_type: str
    tank_size: float
    fuel_refills: list[FuelRefill] = field(default_factory=lambda: [])
