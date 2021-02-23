# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from pages import (
    index,
    _2_1_SurfaceAirTemperature,
    _3_7_DissolvedOxygen,
    )

app = dash.Dash(
    __name__, 
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(
        className='sr-header text-center',
        children='Climate Ireland'
    ),
    html.Div(id='page-content'),
    html.Div(
        className='sr-footer',
        children='Climate Ireland'
    )
],
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/_2_1_SurfaceAirTemperature":
        return _2_1_SurfaceAirTemperature.create_layout(app)
    elif pathname == "/_3_7_DissolvedOxygen":
        return _3_7_DissolvedOxygen.create_layout(app)
    else:
        return index.create_layout(app)

if __name__ == '__main__':
    app.run_server(debug=True)