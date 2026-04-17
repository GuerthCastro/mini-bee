from pathlib import Path

import flet as ft

from src.repositories import initialize
from src.repositories.seeder import seed
from src.ui.home import home_view

DB_PATH = Path("mini_bee.db")
SEED_PATH = Path("src/raw_data/defaultvehicle.json")


def main(page: ft.Page) -> None:
    page.title = "Mini Bee"
    initialize(DB_PATH)
    seed(DB_PATH, SEED_PATH)
    view = home_view(page, DB_PATH)
    page.controls.extend(view.controls)
    page.update()


ft.run(main)  # type: ignore
