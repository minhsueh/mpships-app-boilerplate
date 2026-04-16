import dash # Required for MPShips functionality — do not remove
from mpships_infra import get_rester, MPShipsApp # Required for MPShips functionality — do not remove

from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate

# Register this page at the endpoint: {{cookiecutter.project_shortname}}
# dash.register_page(__name__, path="/") # Required for MPShips functionality — do not remove

# Use `mpr` for retrieving data from MPRester
# Example:
# mpr.materials.summary.search(
#        chemsys=["Au"], fields=["material_id", "has_props"]
#    )
# See more information at: https://docs.materialsproject.org/downloading-data/using-the-api/getting-started
mpr = get_rester() # Required for retrieving data from the Materials Project — do not remove


class {{cookiecutter.project_appname}}(MPShipsApp): # Required for MPShips functionality — do not remove
    # Define your app layout here
    def get_layout(self, **kwargs): # Required for MPShips functionality — do not remove
        return html.Div(
            [
                html.H1("Hello {{cookiecutter.author_name}}! Welcome to {{cookiecutter.project_name}}"),
                html.H4("You can find example app via {{cookiecutter.project_name}}/src/{{cookiecutter.project_name}}/example_pages/")
            ],
            style={"textAlign": "center"}
        )

    # Callbacks in Dash Pages use the global @callback decorator
    def generate_callbacks(self, app, cache): # Required for MPShips functionality — do not remove
        super().generate_callbacks(app, cache) # Required for MPShips functionality — do not remove
        