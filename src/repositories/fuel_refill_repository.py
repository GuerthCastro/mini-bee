import sqlite3
from datetime import datetime
from pathlib import Path

from src.models.fuel_refill import FuelRefill


class FuelRefillRepository:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_by_vehicle(self, vehicle_id: int) -> list[FuelRefill]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM FuelRefill WHERE VehicleId = ? ORDER BY Date",
                (vehicle_id,),
            ).fetchall()
            return [self._map(row) for row in rows]

    def insert(self, refill: FuelRefill) -> int:
        with self._connect() as conn:
            cursor = conn.execute(
                """INSERT INTO FuelRefill
                (VehicleId, Date, Distance, Liters, Price, Station)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    refill.vehicle_id,
                    refill.date.isoformat(),
                    refill.distance,
                    refill.liters,
                    refill.price,
                    refill.station,
                ),
            )
            return cursor.lastrowid or 0

    def delete(self, refill_id: int) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM FuelRefill WHERE Id = ?", (refill_id,))

    def _map(self, row: sqlite3.Row) -> FuelRefill:
        return FuelRefill(
            id=row["Id"],
            vehicle_id=row["VehicleId"],
            date=datetime.fromisoformat(row["Date"]),
            distance=row["Distance"],
            liters=row["Liters"],
            price=row["Price"],
            station=row["Station"] or "",
        )
