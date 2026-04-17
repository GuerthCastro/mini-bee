import sqlite3
from datetime import datetime
from pathlib import Path

from src.models.fuel_refill import FuelRefill
from src.models.vehicle import Vehicle


class VehicleRepository:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_all(self) -> list[Vehicle]:
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM Vehicle").fetchall()
            return [self._map_vehicle(conn, row) for row in rows]

    def get_by_id(self, vehicle_id: int) -> Vehicle | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM Vehicle WHERE Id = ?", (vehicle_id,)
            ).fetchone()
            if row is None:
                return None
            return self._map_vehicle(conn, row)

    def insert(self, vehicle: Vehicle) -> int:
        with self._connect() as conn:
            cursor = conn.execute(
                """INSERT INTO Vehicle
                (Brand, Model, Year, InitialCount, LicensePlate, IsMiles, IsGallons, FuelType, TankSize)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    vehicle.brand,
                    vehicle.model,
                    vehicle.year,
                    vehicle.initial_count,
                    vehicle.license_plate,
                    vehicle.is_miles,
                    vehicle.is_gallons,
                    vehicle.fuel_type,
                    vehicle.tank_size,
                ),
            )
            return cursor.lastrowid or 0

    def delete(self, vehicle_id: int) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM Vehicle WHERE Id = ?", (vehicle_id,))

    def _map_vehicle(self, conn: sqlite3.Connection, row: sqlite3.Row) -> Vehicle:
        refills = conn.execute(
            "SELECT * FROM FuelRefill WHERE VehicleId = ? ORDER BY Date",
            (row["Id"],),
        ).fetchall()
        return Vehicle(
            id=row["Id"],
            brand=row["Brand"],
            model=row["Model"],
            year=row["Year"],
            initial_count=row["InitialCount"],
            license_plate=row["LicensePlate"],
            is_miles=bool(row["IsMiles"]),
            is_gallons=bool(row["IsGallons"]),
            fuel_type=row["FuelType"],
            tank_size=row["TankSize"],
            fuel_refills=[self._map_refill(r) for r in refills],
        )

    def _map_refill(self, row: sqlite3.Row) -> FuelRefill:
        return FuelRefill(
            id=row["Id"],
            vehicle_id=row["VehicleId"],
            date=datetime.fromisoformat(row["Date"]),
            distance=row["Distance"],
            liters=row["Liters"],
            price=row["Price"],
            station=row["Station"] or "",
        )
