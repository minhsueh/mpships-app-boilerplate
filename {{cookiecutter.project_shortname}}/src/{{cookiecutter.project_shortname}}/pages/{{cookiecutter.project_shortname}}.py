import dash # Required for MPShips functionality — do not remove
from mpships_infra import get_rester, MPShipsApp # Required for MPShips functionality — do not remove

from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate

# Use `get_rester()` for retrieving data from MPRester
# Example:
# get_rester().materials.summary.search(
#        chemsys=["Au"], fields=["material_id", "has_props"]
#    )
# See more information at: https://docs.materialsproject.org/downloading-data/using-the-api/getting-started


class {{cookiecutter.project_appname}}(MPShipsApp): # Required for MPShips functionality — do not remove
    # Optional — remove if your app needs no setup, will be called in __init__
    def ships_setup(self, *args, **kwargs):
        # Example code — replace with your own layout
        # Exampled code
        self.my_name = "Pilot"
    
    # Required — defines what renders. Omitting this will raise an error on load.
    def ships_layout(self):
        """The layout of the main content.

        Returns:
            html.Div: The Dash layout for this app.
        """
        # Example code — replace with your own layout
        # Exampled code
        return html.Div(
            [
                html.H1("Hello {{cookiecutter.author_name}}! Welcome to {{cookiecutter.project_name}}"),
                html.H4(f"My name is {self.my_name}", id="name-div", style={"textAlign": "center"}),
                html.H4("You can find example app via '{{cookiecutter.project_shortname}}/src/{{cookiecutter.project_shortname}}/example_pages/'"),
                dcc.Dropdown(
                    id="name-align-dropdown",
                        options=[
                            {"label": "Left", "value": "left"},
                            {"label": "Center", "value": "center"},
                            {"label": "Right", "value": "right"},
                        ],
                        value="center",
                        clearable=False,
                        style={"width": "200px", "margin": "0 auto"},
                ),

            ],
            style={"textAlign": "center"}
        )
    

    # Optional — remove if your app has no callbacks
    def ships_callbacks(self, app, cache):
        # Example code — replace with your own layout
        # Exampled code
        @app.callback(
            Output("name-div", "style"),
            Input("name-align-dropdown", "value"),
        )
        def update_name_alignment(align_value):
            return {"textAlign": align_value}