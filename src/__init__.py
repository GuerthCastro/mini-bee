import flet as ft


def home_view(page: ft.Page) -> ft.View:
    return ft.View(
        route="/",
        controls=[
            ft.AppBar(title=ft.Text("Mini Bee")),
            ft.Text("Vehicle list goes here"),
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
    )
