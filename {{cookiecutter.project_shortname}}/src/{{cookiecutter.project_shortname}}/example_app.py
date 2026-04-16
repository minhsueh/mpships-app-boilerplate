"""
CRITICAL: DO NOT EDIT. Manual changes may cause system instability.
"""

from mpships_infra import create_app
import os

url = "/dielectric_function/"
path_to_pages = os.path.join(os.path.dirname(__file__), "example_pages")

example_app = create_app(url=url, pages_folder=path_to_pages)