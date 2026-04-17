"""
CRITICAL: DO NOT EDIT. For MPShips users: Manual changes may cause system instability.
"""

import os
from src.{{cookiecutter.project_shortname}}.app import app

server = app.server

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8050
    home_path = "/{{cookiecutter.project_shortname}}/"

    print(f"Your app is running on http://{host}:{port}{home_path}")

    app.run(debug=True, host=host, port=port)