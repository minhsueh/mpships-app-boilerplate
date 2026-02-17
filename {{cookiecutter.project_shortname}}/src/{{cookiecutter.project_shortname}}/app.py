from mpships_infra import create_app
import os

path_to_pages = os.path.join(os.path.dirname(__file__), "pages")

app = create_app(pages_folder=path_to_pages)