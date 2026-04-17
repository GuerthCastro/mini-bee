from pathlib import Path

import flet as ft

from src.models.vehicle import Vehicle
from src.repositories import VehicleRepository


def home_view(page: ft.Page, db_path: Path) -> ft.View:
    repo = VehicleRepository(db_path)
    vehicles = repo.get_all()

    def vehicle_card(vehicle: Vehicle) -> ft.Card:
        return ft.Card(
            content=ft.ListTile(
                title=ft.Text(f"{vehicle.brand} {vehicle.model}"),
                subtitle=ft.Text(f"{vehicle.year} · {vehicle.license_plate}"),
            )
        )

    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Mini Bee")),
            ft.Column(
                controls=[vehicle_card(v) for v in vehicles]
                if vehicles
                else [ft.Text("No vehicles yet.")],
            ),
        ],
    )
