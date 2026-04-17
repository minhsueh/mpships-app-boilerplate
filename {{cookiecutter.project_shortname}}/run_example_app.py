"""
CRITICAL: DO NOT EDIT. For MPShips users: Manual changes may cause system instability.
"""

import os
from src.{{cookiecutter.project_shortname}}.example_app import example_app

server = example_app.server

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8051
    home_path = "/dielectric_function/"

    print(f"Your app is running on http://{host}:{port}{home_path}")

    example_app.run(debug=True, host=host, port=port)