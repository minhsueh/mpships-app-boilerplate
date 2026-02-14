import os
from src.{{cookiecutter.project_shortname}}.app import app

server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8050)