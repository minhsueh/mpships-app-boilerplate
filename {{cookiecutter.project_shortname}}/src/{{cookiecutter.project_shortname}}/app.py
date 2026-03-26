"""
CRITICAL: DO NOT EDIT. Manual changes may cause system instability.
"""

from mpships_infra import create_app
import os

url = "/{{cookiecutter.project_shortname}}/"
path_to_pages = os.path.join(os.path.dirname(__file__), "pages")

app = create_app(url=url, pages_folder=path_to_pages)