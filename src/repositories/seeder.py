import json
import sqlite3
from pathlib import Path


def seed(db_path: Path, json_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        count = conn.execute("SELECT COUNT(*) FROM Vehicle").fetchone()[0]
        if count > 0:
            return

        data = json.loads(json_path.read_text(encoding="utf-8"))

        for vehicle in data:
            cursor = conn.execute(
                """INSERT INTO Vehicle
                (Brand, Model, Year, InitialCount, LicensePlate, IsMiles, IsGallons, FuelType, TankSize)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    vehicle["Brand"],
                    vehicle["Model"],
                    vehicle["Year"],
                    vehicle["InitialCount"],
                    vehicle["LicensePlate"],
                    vehicle["IsMiles"],
                    vehicle["IsGallons"],
                    vehicle["FuelType"],
                    vehicle["TankSize"],
                ),
            )
            vehicle_id = cursor.lastrowid

            for refill in vehicle.get("FuelRefillList", []):
                conn.execute(
                    """INSERT INTO FuelRefill
                    (VehicleId, Date, Distance, Liters, Price, Station)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (
                        vehicle_id,
                        refill["Date"],
                        refill["Distance"],
                        refill["Liters"],
                        refill["Price"],
                        refill.get("Station", ""),
                    ),
                )

        conn.commit()
