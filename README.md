# Mini Bee 🐝

A cross-platform desktop application for vehicle fleet management, built with Python and Flet.

## About

Mini Bee is a lightweight desktop app that lets you track your vehicles and fuel refills.
It runs natively on Windows, Linux, and macOS without changing a single line of code.

This project was built as a learning exercise to explore Python desktop development using
real-world data from [Bumblebee](https://github.com/DragonflySourceCodes/dragonfly-bumblebee),
a Flutter mobile app for vehicle tracking.

## Features

- View and manage your vehicle fleet
- Track fuel refills per vehicle
- Add and delete vehicles
- SQLite database — no server required
- Cross-platform: Windows, Linux, macOS

## Tech Stack

- Python 3.13
- [Flet](https://flet.dev) — Flutter-powered UI for Python
- SQLite built-in

## Getting Started

Clone the repository:

    git clone https://github.com/GuerthCastro/mini-bee.git
    cd mini-bee

Create and activate virtual environment:

    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Run the app:

    python main.py

## Project Structure

    src/
    ├── models/         # Domain models
    ├── repositories/   # SQLite data access
    ├── services/       # Business logic
    └── ui/             # Flet screens

## License

MIT
