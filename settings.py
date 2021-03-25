import pathlib
import os
if os.path.isfile('env.py'):
    import env

ATMOSPHERE_COLOR = '#009fe3'
OCEAN_COLOR = '#00909e'
TERRESTRIAL_COLOR = '#f39200'

ATMOSPHERE_BG_COLOR = '#e6f5fc'
OCEAN_BG_COLOR = '#e6f3f5'
TERRESTRIAL_BG_COLOR = '#fef4e6'

TIMESERIES_COLOR_PRIMARY = "#00a4ae"
TIMESERIES_COLOR_SECONDARY = "#E1AF00"

STATION_COLORS = {
    'Buoy': '#e69800',
    'Synoptic': '#ff0000',
    'Rainfall': '#ffff00',
    'Climate': '#004da8',
    'WaveRide/SmartBayObsCenter': '#ffff00',
    'MI_Survey': '#ff0000',
    'EPA': '#002673'
}

CHART_FONT = dict(
    color="#7f7f7f")

TIMESERIES_LAYOUT = dict(
    xaxis=dict(showgrid=False),
    height=450,
    margin={"t": 0, "b": 0, "r": 0, "l": 0, },
    plot_bgcolor='#f7fbfd',
    paper_bgcolor='rgba(0,0,0,0)',
    font=CHART_FONT,
    hovermode='closest',
    legend=dict(
            orientation='h',
            bgcolor='rgba(0,0,0,0)',
            itemclick=False,
            itemdoubleclick=False,
        ), 
)




CHAPTERS = [
    # Upper-air Atmoshere
    # {
    #  'id':'uaa-1',
    #  'title':'Lightning',
    #  'href':'',
    #  'icon-src':'ico-uaa-lightning.png',
    #  'icon-hover-src':'ico-uaa-lightning_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #     {
    #  'id':'uaa-2',
    #  'title':'Clouds',
    #  'href':'',
    #  'icon-src':'ico-uaa-cloud-properties.png',
    #  'icon-hover-src':'ico-uaa-cloud-properties_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-3',
    #  'title':'Earth Radiation Budget',
    #  'href':'',
    #  'icon-src':'ico-uaa-earth-radiation-budget.png',
    #  'icon-hover-src':'ico-uaa-earth-radiation-budget_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-4',
    #  'title':'Wind Speed',
    #  'href':'',
    #  'icon-src':'ico-uaa-lightning.png',
    #  'icon-hover-src':'ico-uaa-windspeed_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-5',
    #  'title':'Upper Air Atmosphere Temperature',
    #  'href':'',
    #  'icon-src':'ico-uaa-temperature.png',
    #  'icon-hover-src':'ico-uaa-temperature_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-6',
    #  'title':'Upper Air Atmosphere Water Vapour',
    #  'href':'',
    #  'icon-src':'ico-uaa-watervapour.png',
    #  'icon-hover-src':'ico-uaa-watervapour_hover.png',
    #  'domain':'Atmosphere',
    #         },

    # Surface Atmoshere
    {
        'chapter-num': '2.1',
        'id': 'sa-1',
        'title': 'Surface Temperature',
        'href': '/_2_1_SurfaceAirTemperature',
        'icon-lg-src': 'surface-temperature.png',
        'icon-src': 'ico-sa-temperature.png',
        'icon-hover-src': 'ico-sa-temperature_hover.png',
        'domain': 'Atmosphere',
        'subdomain': 'Surface',
        'scientific-area': 'Energy and Temperature',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Keith Lambkin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.5',
        'id': 'sa-2',
        'title': 'Precipitation',
        'href': '/_2_5_Precipitation',
        'icon-lg-src': 'precipitation.png',
        'icon-src': 'ico-sa-precipitation.png',
        'icon-hover-src': 'ico-sa-precipitation_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Keith Lambkin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.10',
        'id': 'ac-1',
        'title': 'Carbon Dioxide',
        'href': '/_2_10_CarbonDioxide',
        'icon-lg-src': 'greenhouse-gases.png',
        'icon-src': 'ico-ac-co2-ghgs.png',
        'icon-hover-src': 'ico-ac-co2-ghgs_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.11',
        'id': 'ac-2',
        'title': 'Methane',
        'href': '/_2_11_Methane',
        'icon-lg-src': 'precursors_0.png',
        'icon-src': 'ico-ac-precursors.png',
        'icon-hover-src': 'ico-ac-precursors_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.12',
        'id': 'ac-3',
        'title': 'Other Greenhouse Gases',
        'href': '/_2_12_OtherGreenhouseGases',
        'icon-lg-src': 'precursors_0.png',
        'icon-src': 'ico-ac-precursors.png',
        'icon-hover-src': 'ico-ac-precursors_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },

    # Ocean Biogeochemistry
    {
        'chapter-num': '3.1',
        'id': 'sop-1',
        # Both Surface and Sub-surface on same page
        'title': 'Surface Temperature',
        'href': '/_3_1_SurfaceSubsurfaceTemperature',
        'icon-lg-src': 'sea-surface-temperature.png',
        'icon-src': 'ico-sop-sea-surface-temp.png',
        'icon-hover-src': 'ico-sop-sea-surface-temp_hover.png',
        'domain': 'Ocean',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'chapter-num': '3.1',
        'id': 'ssop-1',
        'title': 'Sub-surface Temperature',
        # Both Surface and Sub-surface on same page
        'href': '/_3_1_SurfaceSubsurfaceTemperature',
        'icon-lg-src': 'subsurface-temperature_1.png',
        'icon-src': 'ico-ssop-subsurface-temp.png',
        'icon-hover-src': 'ico-ssop-subsurface-temp_hover.png',
        'domain': 'Ocean',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'chapter-num': '3.4',
        'id': 'sop-2',
        'title': 'Sea Level',
        'href': '/_3_4_SeaLevel',
        'icon-lg-src': 'sea-level_0.png',
        'icon-src': 'ico-sop-sea-level.png',
        'icon-hover-src': 'ico-sop-sea-level_hover.png',
        'domain': 'Ocean',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'chapter-num': '3.6',
        'id': 'obgc-1',
        'title': 'Inorganic Carbon',
        'href': '/_3_6_InorganicCarbon',
        'icon-lg-src': 'inorganic-carbon.png',
        'icon-src': 'ico-obgc-inorganic-carbon.png',
        'icon-hover-src': 'ico-obgc-inorganic-carbon_hover.png',
        'domain': 'Ocean',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'chapter-num': '3.7',
        'id': 'obgc-2',
        'title': 'Dissolved Oxygen',
        'href': '/_3_7_Oxygen',
        'icon-lg-src': 'oxygen.png',
        'icon-src': 'ico-obgc-oxygen.png',
        'icon-hover-src': 'ico-obgc-oxygen_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemistry',
        'scientific-area': 'Biosphere',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Robert Wilkes, Rob Thomas, Evin McGovern',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },

    # Biosphere

    {
        'chapter-num': '4.1',
        'id': 'hyd-1',
        'title': 'River Discharge',
        'href': '/_4_1_RiverDischarge',
        'icon-lg-src': 'river-discharge.png',
        'icon-src': 'ico-hyd-river-discharge.png',
        'icon-hover-src': 'ico-hyd-river-discharge_hover.png',
        'domain': 'Terrestrial',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'chapter-num': '4.6',
        'id': 'bio-1',
        'title': 'Land Cover',
        'href': '/_4_6_LandCover',
        'icon-lg-src': 'land-cover.png',
        'icon-src': 'ico-bio-land-cover.png',
        'icon-hover-src': 'ico-bio-land-cover_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': 'Biosphere',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'chapter-num': '4.7',
        'id': 'bio-2',
        'title': 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR)',
        'href': '/_4_7_FAPAR',
        'icon-lg-src': 'fapar.png',
        'icon-src': 'ico-bio-fapr.png',
        'icon-hover-src': 'ico-bio-fapr_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': 'Biosphere',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },

    {
        'chapter-num': '4.11',
        'id': 'bio-3',
        'title': 'Fire Disturbance',
        'href': '/_4_11_Fire',
        'icon-lg-src': 'fire_0.png',
        'icon-src': 'ico-bio-fire.png',
        'icon-hover-src': 'ico-bio-fire_hover.png',
        'domain': 'Terrestrial',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'chapter-num': '4.14',
        'id': 'ant-1',
        'title': 'Anthropogenic Greenhouse Gas Emissions ',
        'href': '/_4_14_AnthropogenicGreenhouseGasEmissions ',
        'icon-lg-src': 'anthropogenic-ghg-fluxes.png',
        'icon-src': 'ico-ant-ghg-fluxes.png',
        'icon-hover-src': 'ico-ant-ghg-fluxes_hover.png',
        'domain': 'Terrestrial',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },


]



MAP_LAYOUT = dict(
    legend=dict(title='<b>Station Type</b>',
                x=0.01),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    height=400,
    margin=dict(t=0, b=0, r=0, l=0),
    mapbox=dict(bearing=0,
                center=dict(
                    lat=53.4,
                    lon=352
                ),
                pitch=0,
                zoom=5,
                style="open-street-map"  # does not require token
                )
)


IMAGES_PATH = 'assets/images/'
# IMAGES_PATH='/Users/dan/ClimateIreland/Projects/CI-Status-Report-Dash/assets/images/'
# IMAGES_PATH='https://www.climateireland.ie/web_resource/images/'

PATH = pathlib.Path(__file__).parent
DATA_PATH = os.getenv("DATA_PATH")
# DATA_PATH='/home/dancasey/Status_Tool_Data/'
# DATA_PATH = '/Users/dan/OneDrive - University College Cork/Status_Tool/'
# HOST=os.getenv("IP",default='127.0.0.1')
# PORT=os.getenv("PORT",default='1850')
# DEBUG=os.getenv("DEBUG",default=True)
# HOST=os.getenv("IP",default='127.0.0.1')
# PORT=os.getenv("PORT",default='1850')
# DEBUG=os.getenv("DEBUG",default=True)
