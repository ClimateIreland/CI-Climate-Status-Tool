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
    _2_3_WaterVapour,
    _2_4_AtmosphericPressure,
    _2_5_Precipitation,
    _2_6_SurfaceEarth_RadiationBudget,
    _2_7a_UpperAirTemperature,
    _2_7b_UpperAirWindSpeedAndDirection,
    _2_8_CloudProperties,
    _2_9_Lightning,
    _2_10_CarbonDioxide,
    _2_11_Methane,
    _2_12_OtherGreenhouseGases,
    _2_13_Ozone,
    _2_14_Aerosols,
    _2_15_PrecursorsAerosolsOzone,
    _3_1a_SeaSurfaceTemperature,
    _3_1b_SeaSubsurfaceTemperature,
    _3_2_OceanSurfaceSubsurfaceSalinity,
    _3_3_OceanSurfaceAndSubsurfaceCurrents,
    _3_4_SeaLevel,
    _3_5_SeaState,
    _3_6_InorganicCarbon,
    _3_7_DissolvedOxygen,
    _3_8_Nutrients,
    _3_9_OceanColour,
    _3_10_Plankton,
    _3_11_MarineHabitatProperties,
    _3_12a_TransientTracers,
    _3_12b_OceanSurfaceStress,
    _3_12c_OceanSurfaceHeatFlux,
    _3_12d_OceanicNitrousOxide,
    _4_1_RiverDischarge,
    _4_2_Groundwater,
    _4_3_Lakes,
    _4_4_SoilMoisture,
    _4_5_Albedo,
    _4_6_LandCover,
    _4_7_FAPAR,
    _4_8_LAI,
    _4_9_AboveGroundBiomass,
    _4_10_SoilCarbon,
    _4_11_Fire,
    _4_12_LandSurfaceTemperature,
    _4_13_WaterUse,
    _4_14_AnthropogenicGreenhouseGasEmissions,
)

app = dash.Dash(
    __name__,
    url_base_pathname="/statusTool/",
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
    html.Div(id='page-content'),
],
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):

    if pathname == "/statusTool/":
        return index.create_layout(app)
    # Atmospheric
    elif "_2_1_SurfaceAirTemperature" in pathname:
        return _2_1_SurfaceTemperature.create_layout(app)
    elif "_2_2_SurfaceWindSpeedAndDirection" in pathname:
        return _2_2_SurfaceWindSpeedAndDirection.create_layout(app)
    elif "_2_3_WaterVapour" in pathname:
        return _2_3_WaterVapour.create_layout(app)
    elif "_2_4_AtmosphericPressure" in pathname:
        return _2_4_AtmosphericPressure.create_layout(app)
    elif "_2_5_Precipitation" in pathname:
        return _2_5_Precipitation.create_layout(app)
    elif "_2_6_SurfaceEarth_RadiationBudget" in pathname:
        return _2_6_SurfaceEarth_RadiationBudget.create_layout(app)
    elif "_2_7a_UpperAirTemperature" in pathname:
        return _2_7a_UpperAirTemperature.create_layout(app)
    elif "_2_7b_UpperAirWindSpeedAndDirection" in pathname:
        return _2_7b_UpperAirWindSpeedAndDirection.create_layout(app)
    elif "_2_8_CloudProperties" in pathname:
        return _2_8_CloudProperties.create_layout(app)
    elif "_2_9_Lightning" in pathname:
        return _2_9_Lightning.create_layout(app)
    elif "_2_10_CarbonDioxide" in pathname:
        return _2_10_CarbonDioxide.create_layout(app)
    elif "_2_11_Methane" in pathname:
        return _2_11_Methane.create_layout(app)
    elif "_2_13_Ozone" in pathname:
        return _2_13_Ozone.create_layout(app)
    elif "_2_12_OtherGreenhouseGases" in pathname:
        return _2_12_OtherGreenhouseGases.create_layout(app)
    elif "_2_14_Aerosols" in pathname:
        return _2_14_Aerosols.create_layout(app)    
    elif "_2_15_PrecursorsAerosolsOzone" in pathname:
        return _2_15_PrecursorsAerosolsOzone.create_layout(app)
        
    # Oceanic
    elif "_3_1a_SeaSurfaceTemperature" in pathname:
        return _3_1a_SeaSurfaceTemperature.create_layout(app)
    elif "_3_1b_SeaSubsurfaceTemperature" in pathname:
        return _3_1b_SeaSubsurfaceTemperature.create_layout(app)
    elif "_3_2_OceanSurfaceSubsurfaceSalinity" in pathname:
        return _3_2_OceanSurfaceSubsurfaceSalinity.create_layout(app)
    elif "_3_3_OceanSurfaceAndSubsurfaceCurrents" in pathname:
        return _3_3_OceanSurfaceAndSubsurfaceCurrents.create_layout(app)
    elif "_3_4_SeaLevel" in pathname:
        return _3_4_SeaLevel.create_layout(app)
    elif "_3_5_SeaState" in pathname:
        return _3_5_SeaState.create_layout(app)    
    elif "_3_6_InorganicCarbon" in pathname:
        return _3_6_InorganicCarbon.create_layout(app)
    elif "_3_7_DissolvedOxygen" in pathname:
        return _3_7_DissolvedOxygen.create_layout(app)
    elif "_3_8_Nutrients" in pathname:
        return _3_8_Nutrients.create_layout(app)
    elif "_3_9_OceanColour" in pathname:
        return _3_9_OceanColour.create_layout(app)
    elif "_3_10_Plankton" in pathname:
        return _3_10_Plankton.create_layout(app)
    elif "_3_11_MarineHabitatProperties" in pathname:
        return _3_11_MarineHabitatProperties.create_layout(app)
    elif "_3_12a_TransientTracers" in pathname:
        return _3_12a_TransientTracers.create_layout(app)
    elif "_3_12b_OceanSurfaceStress" in pathname:
        return _3_12b_OceanSurfaceStress.create_layout(app)
    elif "_3_12c_OceanSurfaceHeatFlux" in pathname:
        return _3_12c_OceanSurfaceHeatFlux.create_layout(app)
    elif "_3_12d_OceanicNitrousOxide" in pathname:
        return _3_12d_OceanicNitrousOxide.create_layout(app)

    # Terrestrial
    elif "_4_2_Groundwater" in pathname:
        return _4_2_Groundwater.create_layout(app)
    elif "_4_1_RiverDischarge" in pathname:
        return _4_1_RiverDischarge.create_layout(app)
    elif "_4_3_Lakes" in pathname:
        return _4_3_Lakes.create_layout(app)
    elif "_4_4_SoilMoisture" in pathname:
        return _4_4_SoilMoisture.create_layout(app)
    elif "_4_5_Albedo" in pathname:
        return _4_5_Albedo.create_layout(app)
    elif "_4_6_LandCover" in pathname:
        return _4_6_LandCover.create_layout(app)
    elif "_4_7_FAPAR" in pathname:
        return _4_7_FAPAR.create_layout(app)
    elif "_4_8_LAI" in pathname:
        return _4_8_LAI.create_layout(app)
    elif "_4_9_AboveGroundBiomass" in pathname:
        return _4_9_AboveGroundBiomass.create_layout(app)
    elif "_4_10_SoilCarbon" in pathname:
        return _4_10_SoilCarbon.create_layout(app)
    elif "_4_11_Fire" in pathname:
        return _4_11_Fire.create_layout(app)
    elif "_4_12_LandSurfaceTemperature" in pathname:
        return _4_12_LandSurfaceTemperature.create_layout(app)
    elif "_4_13_WaterUse" in pathname:
        return _4_13_WaterUse.create_layout(app) 
    elif "_4_14_AnthropogenicGreenhouseGasEmissions" in pathname:
        return _4_14_AnthropogenicGreenhouseGasEmissions.create_layout(app)
    else:
        return dcc.Location(pathname="/statusTool", id="someid_doesnt_matter")

if __name__ == '__main__':
    app.run_server(debug='True')
       
    
    
