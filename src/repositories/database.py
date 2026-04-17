import sqlite3
from pathlib import Path


def initialize(db_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Vehicle (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Brand TEXT NOT NULL,
                Model TEXT NOT NULL,
                Year INTEGER NOT NULL,
                InitialCount REAL NOT NULL,
                LicensePlate TEXT NOT NULL,
                IsMiles INTEGER NOT NULL DEFAULT 0,
                IsGallons INTEGER NOT NULL DEFAULT 0,
                FuelType TEXT NOT NULL,
                TankSize REAL NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS FuelRefill (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                VehicleId INTEGER NOT NULL,
                Date TEXT NOT NULL,
                Distance REAL NOT NULL,
                Liters REAL NOT NULL,
                Price REAL NOT NULL,
                Station TEXT,
                FOREIGN KEY (VehicleId) REFERENCES Vehicle(Id) ON DELETE CASCADE
            )
        """)
        conn.commit()
