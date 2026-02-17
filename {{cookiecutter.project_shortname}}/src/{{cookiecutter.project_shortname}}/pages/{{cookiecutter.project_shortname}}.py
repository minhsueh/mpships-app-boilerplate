import dash
from dash import html, dcc, callback, Output, Input
from dash.exceptions import PreventUpdate

from mpships_infra import get_mp_rester

# Register this page at the endpoint: {{cookiecutter.project_shortname}}
dash.register_page(__name__, path="/{{cookiecutter.project_shortname}}/")

# Use `mpr` for retrieving data from MPRester
# Example:
# mpr.materials.summary.search(
#        chemsys=["Au"], fields=["material_id", "has_props"]
#    )
# See more information at: https://docs.materialsproject.org/downloading-data/using-the-api/getting-started
mpr = get_mp_rester()

# Define your app layout here
layout = html.Div(
    [
        html.H2("{{cookiecutter.project_name}}", style={"textAlign": "center"}),
        html.Button(
            "Change Color", 
            id="color-button", 
            n_clicks=0,
        ),
    ],
    id="project-div",
    style={
        "padding": "40px", 
        "textAlign": "center", 
        "border": "1px solid #ccc",
        "transition": "background-color 0.5s ease"
    }
)

# Callbacks in Dash Pages use the global @callback decorator
@callback(
    Output("project-div", "style"),
    Input("color-button", "n_clicks"),
    prevent_initial_call=True
)
def update_background(n_clicks):
    # Base style
    style = {
        "padding": "40px", 
        "textAlign": "center", 
        "border": "1px solid #ccc",
        "transition": "background-color 0.5s ease"
    }

    # Toggle logic
    if n_clicks % 2 == 1:
        style["backgroundColor"] = "#3273dc"
        style["color"] = "white"
    else:
        style["backgroundColor"] = "transparent"
        style["color"] = "black"

    return style