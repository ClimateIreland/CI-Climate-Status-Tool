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
    _2_2_SurfaceWindSpeedAndDirection,
    _2_5_Precipitation,
    _2_10_CarbonDioxide,
    _2_11_Methane,
    _2_12_OtherGreenhouseGases,

    _3_1a_SeaSurfaceTemperature,
    _3_1b_SeaSubsurfaceTemperature,
    _3_4_SeaLevel,
    _3_6_InorganicCarbon,
    _3_7_DissolvedOxygen,

    _4_1_RiverDischarge,
    _4_6_LandCover,
    _4_7_FAPAR,
    _4_11_Fire,
    _4_14_AnthropogenicGreenhouseGasEmissions,
)

app = dash.Dash(
    __name__,
    url_base_pathname="/dash/",
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
    
    if pathname == "/dash/":
        return index.create_layout(app)
    elif "_2_1_SurfaceAirTemperature" in pathname:
        return _2_1_SurfaceTemperature.create_layout(app)
    elif "_2_2_SurfaceWindSpeedAndDirection" in pathname:
        return _2_2_SurfaceWindSpeedAndDirection.create_layout(app)
    elif "_2_5_Precipitation" in pathname:
        return _2_5_Precipitation.create_layout(app)
    elif "_2_10_CarbonDioxide" in pathname:
        return _2_10_CarbonDioxide.create_layout(app)
    elif "_2_11_Methane" in pathname:
        return _2_11_Methane.create_layout(app)
    elif "_2_12_OtherGreenhouseGases" in pathname:
        return _2_12_OtherGreenhouseGases.create_layout(app)
    elif "_3_1a_SeaSurfaceTemperature" in pathname:
        return _3_1a_SeaSurfaceTemperature.create_layout(app)
    elif "_3_1b_SeaSubsurfaceTemperature" in pathname:
        return _3_1b_SeaSubsurfaceTemperature.create_layout(app)
    elif "_3_4_SeaLevel" in pathname:
        return _3_4_SeaLevel.create_layout(app)
    elif "_3_6_InorganicCarbon" in pathname:
        return _3_6_InorganicCarbon.create_layout(app)
    elif "_3_7_DissolvedOxygen" in pathname:
        return _3_7_DissolvedOxygen.create_layout(app)
    elif "_4_1_RiverDischarge" in pathname:
        return _4_1_RiverDischarge.create_layout(app)
    elif "_4_6_LandCover" in pathname:
        return _4_6_LandCover.create_layout(app)
    elif "_4_7_FAPAR" in pathname:
        return _4_7_FAPAR.create_layout(app)
    elif "_4_11_Fire" in pathname:
        return _4_11_Fire.create_layout(app)
    elif "_4_14_AnthropogenicGreenhouseGasEmissions" in pathname:
        return _4_14_AnthropogenicGreenhouseGasEmissions.create_layout(app)
    # else:
    #     return dcc.Location(pathname="/StatusReport", id='any')
    else:
        # pathname = "/dash/"
        return dcc.Location(pathname="/dash", id="someid_doesnt_matter")
        # return index.create_layout(app)

if __name__ == '__main__':
    app.run_server(debug='True')
       
    
    
