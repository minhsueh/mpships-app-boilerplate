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
        self.my_role = "Navigator"
    
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
                html.H1(
                    "Welcome to MPShips, Captain {{cookiecutter.author_name}}!",
                    className="title is-1"
                ),
                html.H4(
                    "Your ship, {{cookiecutter.project_appname}}, is now under construction."
                ),
                html.H4(
                    f"I am your {self.my_role}, and I'll help you get your ship ready to sail!",
                    id="name-div",
                    style={"textAlign": "center"},
                ),
                html.P(
                    [
                        "To get started, check out the example pages at ",
                        html.Code(
                            "{{cookiecutter.project_shortname}}/src/"
                            "{{cookiecutter.project_shortname}}/example_pages/"
                        ),
                    ]
                ),
                html.H4(
                    [
                        "Once your app is developed here (replacing this welcome page in ",
                        html.Code("ships_layout"),
                        " and ",
                        html.Code("ships_callbacks"),
                        "), submit it to the ",
                        html.A(
                            "MPShips registry",
                            href="https://github.com/materialsproject/MPShips",
                            target="_blank",
                        ),
                        " for review. Once approved, your ship will be cleared to set sail with the MPShips fleet!",
                    ]
                ),
                html.Br(),
                html.Label(
                    "Where is navigator?",
                    style={"display": "block", "marginBottom": "0.5rem"},
                ),
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