# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import page_builder as pb
import dash_bootstrap_components as dbc
from settings import *

from pages import (
    index,
    _2_1_SurfaceTemperature,
    _2_5_Precipitation,
    _2_10_CarbonDioxide,
    _2_11_Methane,
    _2_12_OtherGreenhouseGases,

    _3_1a_SeaSurfaceTemperature,
    _3_1b_SeaSubsurfaceTemperature,
    _3_4_SeaLevel,
    _3_6_InorganicCarbon,
    _3_7_Oxygen,

    _4_1_RiverDischarge,
    _4_6_LandCover,
    _4_7_FAPAR,
    _4_11_Fire,
    _4_14_AnthropogenicGreenhouseGasEmissions,
)

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ],
)

server = app.server

app.title = 'Climate Status Report Ireland'
app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    # html.Div(
    #     className='sr-header text-center',
    #     children='Climate Ireland'
    # ),
    html.Div(id='page-content'),
    # html.Div(
    #     className='sr-footer',
    #     children='Climate Ireland'
    # )
],
)

# Update page


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/StatusReport":
        return index.create_layout(app)
    elif pathname == "/_2_1_SurfaceAirTemperature":
        return _2_1_SurfaceTemperature.create_layout(app)
    elif pathname == "/_2_1_SurfaceAirTemperature/chart":
        return _2_1_SurfaceTemperature.create_chart(app)
    elif pathname == "/_2_5_Precipitation":
        return _2_5_Precipitation.create_layout(app)
    elif pathname == "/_2_10_CarbonDioxide":
        return _2_10_CarbonDioxide.create_layout(app)
    elif pathname == "/_2_11_Methane":
        return _2_11_Methane.create_layout(app)
    elif pathname == "/_2_12_OtherGreenhouseGases":
        return _2_12_OtherGreenhouseGases.create_layout(app)
    elif pathname == "/_3_1a_SeaSurfaceTemperature":
        return _3_1a_SeaSurfaceTemperature.create_layout(app)
    elif pathname == "/_3_1b_SeaSubsurfaceTemperature":
        return _3_1b_SeaSubsurfaceTemperature.create_layout(app)
    elif pathname == "/_3_4_SeaLevel":
        return _3_4_SeaLevel.create_layout(app)
    elif pathname == "/_3_6_InorganicCarbon":
        return _3_6_InorganicCarbon.create_layout(app)
    elif pathname == "/_3_7_Oxygen":
        return _3_7_Oxygen.create_layout(app)
    elif pathname == "/_4_1_RiverDischarge":
        return _4_1_RiverDischarge.create_layout(app)
    elif pathname == "/_4_6_LandCover":
        return _4_6_LandCover.create_layout(app)
    elif pathname == "/_4_7_FAPAR":
        return _4_7_FAPAR.create_layout(app)
    elif pathname == "/_4_11_Fire":
        return _4_11_Fire.create_layout(app)
    elif pathname == "/_4_14_AnthropogenicGreenhouseGasEmissions":
        return _4_14_AnthropogenicGreenhouseGasEmissions.create_layout(app)
    # else:
    #     return dcc.Location(pathname="/StatusReport", id='any')
    else:
        return index.create_layout(app)

if __name__ == '__main__':
    app.run_server(debug='True')
       
    
    
