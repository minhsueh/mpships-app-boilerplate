from mpships_infra import create_app
import os

url = "/{{cookiecutter.project_shortname}}/"

app = create_app(url=url)