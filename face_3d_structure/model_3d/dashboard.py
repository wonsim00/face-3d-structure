"""Instantiate a Dash app."""
import numpy as np
import plotly.graph_objects as go
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc

from .data import data


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/',
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        #     'https://fonts.googleapis.com/css?family=Lato'
        # ]
    )

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id = 'model-3d',
                figure = get_figure()
            ),
        ],
        id='dash-container'
    )
    return dash_app.server


def get_figure():
    fig = go.Figure(data = data)

    fig.update_layout(
        title = 'sphere', 
        autosize = False,
        width = 1000, height = 1000,
        margin = dict(l = 65, r = 50, b = 65, t = 90),
    )

    fig.update_scenes(
        camera = dict(
            eye = dict(x = 0, y = -2, z = 0),
            projection_type = "orthographic",
        )
    )

    return fig
