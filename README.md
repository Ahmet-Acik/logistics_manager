# Logistics Manager

A Python project for managing logistics and shipping operations, including shipments, warehouses, routes, tracking, and customers. Uses SQLAlchemy for ORM and MySQL as the database backend.

## Features
- Manage customers, warehouses, shipments, routes, and tracking
- SQLAlchemy ORM models for all entities
- MySQL database integration
- Easily extensible for more business logic

## Requirements
- Python 3.8+
- MySQL server
- pip (Python package manager)

## Setup
1. Clone this repository or copy the project files.
2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure your MySQL connection in `config.py`.
5. Run the database migration script to create tables.

## Usage
- Add your business logic in the `app/` directory.
- Use the provided models to interact with the database.

## License
MIT
