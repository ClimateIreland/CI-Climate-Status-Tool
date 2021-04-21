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
    'Buoy': '#e69800', # orange
    'Synoptic': '#ff0000', # red
    'Rainfall': '#ffff00', # yellow
    'Climate': '#004da8', # blue
    'WaveRide/SmartBayObsCenter': '#ffff00', # yellow
    'MI_Survey': '#ff0000', # red
    'EPA': '#002673', # dark blue
    'NUIG': '#00734c', # dark green
    'TidbiT': '#004da8', # blue
    'ExtendedElletLineBuoy': '#00734c', # dark green
    'TideGauge': '#8400a8', # purple
    'Flow': 'green', # green
    'GHG_FLUX_TOWER' : 'red'
}

CHART_FONT = dict(
    color="#7f7f7f")

TIMESERIES_LAYOUT = dict(
    xaxis=dict(showgrid=False),
    height=450,
    margin={"t": 0, "b": 0, "r": 0, "l": 0, },
    plot_bgcolor='#f7fbfd',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis_fixedrange = True,
    yaxis_fixedrange = True,
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
    # Surface Atmoshere
    {
        'chapter-num': '2.1',
        'id': 'sa-1',
        'title': 'Surface Temperature',
        'href': '_2_1_SurfaceAirTemperature',
        'icon-lg-src': 'surface-temperature.png',
        'icon-lg-hover-src': 'surface-temperature_hover.png',
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
        'href': '_2_5_Precipitation',
        'icon-lg-src': 'precipitation.png',
        'icon-lg-hover-src': 'precipitation_hover.png',
        'icon-src': 'ico-sa-precipitation.png',
        'icon-hover-src': 'ico-sa-precipitation_hover.png',
        'domain': 'Atmosphere',
        'subdomain': 'Surface',
        'scientific-area': 'Hydrosphere',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Keith Lambkin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.10',
        'id': 'ac-1',
        'title': 'Carbon Dioxide',
        'href': '_2_10_CarbonDioxide',
        'icon-lg-src': 'carbon-dioxide.png',
        'icon-lg-hover-src': 'carbon-dioxide_hover.png',
        'icon-src': 'ico-ac-co2.png',
        'icon-hover-src': 'ico-ac-co2_hover.png',
        'domain': 'Atmosphere',
        'subdomain': 'Atmospheric Composition',
        'scientific-area': 'Carbon cycle and other GHGs',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Damien Martin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.11',
        'id': 'ac-2',
        'title': 'Methane',
        'href': '_2_11_Methane',
        'icon-lg-src': 'methane.png',
        'icon-lg-hover-src': 'methane_hover.png',
        'icon-src': 'ico-ac-ch4.png',
        'icon-hover-src': 'ico-ac-ch4_hover.png',
        'domain': 'Atmosphere',
        'subdomain': 'Atmospheric Composition',
        'scientific-area': 'Carbon cycle and other GHGs',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Damien Martin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },
    {
        'chapter-num': '2.12',
        'id': 'ac-3',
        'title': 'Other Greenhouse Gases',
        'href': '_2_12_OtherGreenhouseGases',
        'icon-lg-src': 'greenhouse-gases.png',
        'icon-lg-hover-src': 'greenhouse-gases_hover.png',
        'icon-src': 'ico-ac-co2-ghgs.png',
        'icon-hover-src': 'ico-ac-co2-ghgs_hover.png',
        'domain': 'Atmosphere',
        'subdomain': 'Atmospheric Composition',
        'scientific-area': 'Carbon cycle and other GHGs',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Damien Martin',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR

    },

    # Ocean Biogeochemistry
    {
        'chapter-num': '3.1a',
        'id': 'sop-1',
        # Both Surface and Sub-surface on same page
        'title': 'Sea Surface Temperature',
        'href': '_3_1a_SeaSurfaceTemperature',
        'icon-lg-src': 'sea-surface-temperature.png',
        'icon-lg-hover-src': 'sea-surface-temperature_hover.png',
        'icon-src': 'ico-sop-sea-surface-temp.png',
        'icon-hover-src': 'ico-sop-sea-surface-temp_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': 'Energy and Temperature',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Kieran Lyons, Caroline Cusack, Glenn Nolan',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
            {
        'chapter-num': '3.1b',
        'id': 'ssop-1',
        'title': 'Sea Subsurface Temperature',
        'href': '_3_1b_SeaSubsurfaceTemperature',
        'icon-lg-src': 'subsurface-temperature_1.png',
        'icon-lg-hover-src': 'subsurface-temperature_1_hover.png',
        'icon-src': 'ico-ssop-subsurface-temp.png',
        'icon-hover-src': 'ico-ssop-subsurface-temp_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': 'Energy and Temperature',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Kieran Lyons, Caroline Cusack, Glenn Nolan',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },

    {
        'chapter-num': '3.4',
        'id': 'sop-2',
        'title': 'Sea Level',
        'href': '_3_4_SeaLevel',
        'icon-lg-src': 'sea-level_0.png',
        'icon-lg-hover-src': 'sea-level_0_hover.png',
        'icon-src': 'ico-sop-sea-level.png',
        'icon-hover-src': 'ico-sop-sea-level_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': 'Physical Properties',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Guy Westbrook, Glenn Nolan, Rosemarie Lawlor, Sarah Gallaher, Gerard McCarthy',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },

    {
        'chapter-num': '3.6',
        'id': 'obgc-1',
        'title': 'Inorganic Carbon',
        'href': '_3_6_InorganicCarbon',
        'icon-lg-src': 'inorganic-carbon.png',
        'icon-lg-hover-src': 'inorganic-carbon_hover.png',
        'icon-src': 'ico-obgc-inorganic-carbon.png',
        'icon-hover-src': 'ico-obgc-inorganic-carbon_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemical',
        'scientific-area': 'Carbon Cycle and other GHGs',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer, Margot Cronin, Evin McGovern',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'chapter-num': '3.7',
        'id': 'obgc-2',
        'title': 'Dissolved Oxygen',
        'href': '_3_7_DissolvedOxygen',
        'icon-lg-src': 'oxygen.png',
        'icon-lg-hover-src': 'oxygen_hover.png',
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
        'href': '_4_1_RiverDischarge',
        'icon-lg-src': 'river-discharge.png',
        'icon-lg-hover-src': 'river-discharge_hover.png',
        'icon-src': 'ico-hyd-river-discharge.png',
        'icon-hover-src': 'ico-hyd-river-discharge_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Hydrology',
        'scientific-area': 'Hydrosphere',
        'authors': 'Walther C.A. Cámaro García, Barry O’Dwyer, Conor Murphy, Ned Dwyer',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'chapter-num': '4.6',
        'id': 'bio-1',
        'title': 'Land Cover',
        'href': '_4_6_LandCover',
        'icon-lg-src': 'land-cover.png',
        'icon-lg-hover-src': 'land-cover_hover.png',
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
        'href': '_4_7_FAPAR',
        'icon-lg-src': 'fapar.png',
        'icon-lg-hover-src': 'fapar_hover.png',
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
        'href': '_4_11_Fire',
        'icon-lg-src': 'fire_0.png',
        'icon-lg-hover-src': 'fire_0_hover.png',
        'icon-src': 'ico-bio-fire.png',
        'icon-hover-src': 'ico-bio-fire_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': 'Biosphere',
        'authors': 'Ciaran Nugent, Ned Dwyer, Walther C.A. Cámaro García, Keith Lambkin, Frank Barrett  ',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'chapter-num': '4.14',
        'id': 'ant-1',
        'title': 'Anthropogenic Greenhouse Gas Emissions',
        'href': '_4_14_AnthropogenicGreenhouseGasEmissions',
        'icon-lg-src': 'anthropogenic-ghg-fluxes.png',
        'icon-lg-hover-src': 'anthropogenic-ghg-fluxes_hover.png',
        'icon-src': 'ico-ant-ghg-fluxes.png',
        'icon-hover-src': 'ico-ant-ghg-fluxes_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Human Use of Natural Resources',
        'scientific-area': 'Biosphere',
        'authors': 'Walther C.A. Cámaro García, Ned Dwyer',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
]

CHAPTERS_DEV = [
    # Upper-air Atmoshere
    {
        'id': 'uaa-1',
        'title': 'Lightning',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-lightning.png',
        'icon-hover-src': 'ico-uaa-lightning_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'uaa-2',
        'title': 'Clouds',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-cloud-properties.png',
        'icon-hover-src': 'ico-uaa-cloud-properties_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'uaa-3',
        'title': 'Earth Radiation Budget',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-earth-radiation-budget.png',
        'icon-hover-src': 'ico-uaa-earth-radiation-budget_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'uaa-4',
        'title': 'Wind Speed',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-windspeed.png',
        'icon-hover-src': 'ico-uaa-windspeed_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'uaa-5',
        'title': 'Upper Air Atmosphere Temperature',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-temperature.png',
        'icon-hover-src': 'ico-uaa-temperature_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'uaa-6',
        'title': 'Upper Air Atmosphere Water Vapour',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-uaa-watervapour.png',
        'icon-hover-src': 'ico-uaa-watervapour_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    # ATMOSPHERE - COMPOSITION
    {
        'id': 'ac-4',
        'title': 'Aerosols',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ac-aerosols.png',
        'icon-hover-src': 'ico-ac-aerosols_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'ac-5',
        'title': 'Ozone',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ac-ozone.png',
        'icon-hover-src': 'ico-ac-ozone_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'ac-6',
        'title': 'Precursors for Aerosols and Ozone',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ac-precursors.png',
        'icon-hover-src': 'ico-ac-precursors_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    # ATMOSPHERE - SURFACE
    {
        'id': 'sa-3',
        'title': 'Surface Pressure',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sa-pressure.png',
        'icon-hover-src': 'ico-sa-pressure_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'sa-4',
        'title': 'Surface Radiation Budget',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sa-surfaceradiationbudget.png',
        'icon-hover-src': 'ico-sa-surfaceradiationbudget_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'sa-5',
        'title': 'Surface Wind Speed and Direction',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sa-windspeed.png',
        'icon-hover-src': 'ico-sa-windspeed_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    {
        'id': 'sa-6',
        'title': 'Surface Water Vapour',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sa-watervapour.png',
        'icon-hover-src': 'ico-sa-watervapour_hover.png',
        'domain': 'Atmosphere',
        'subdomain': '',
        'scientific-area': '',
        'authors': '',
        'domain-color': ATMOSPHERE_COLOR,
        'domain-bg-color': ATMOSPHERE_BG_COLOR
    },
    # OCEANIC - SURFACE OCEAN PHYSICS
    {
        'id': 'sop-3',
        'title': 'Sea State',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sop-sea-state.png',
        'icon-hover-src': 'ico-sop-sea-state_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'sop-4',
        'title': 'Surface Stress',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sop-surface-stress.png',
        'icon-hover-src': 'ico-sop-surface-stress_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'sop-5',
        'title': 'Ocean Surface Heat Flux',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sop-ocean-surface-heat-flux.png',
        'icon-hover-src': 'ico-sop-ocean-surface-heat-flux_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'sop-6',
        'title': 'Sea Surface Ocean Salinity',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sop-sea-surface-salinity.png',
        'icon-hover-src': 'ico-sop-sea-surface-salinity_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'sop-7',
        'title': 'Surface Currents',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-sop-sea-surface-currents.png',
        'icon-hover-src': 'ico-sop-sea-surface-currents_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    # OCEANIC - SUBSURFACE OCEAN PHYSICS
    {
        'id': 'ssop-2',
        'title': 'Subsurface Currents',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ssop-subsurface-currents.png',
        'icon-hover-src': 'ico-ssop-subsurface-currents_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'ssop-3',
        'title': 'Subsuface Salinity',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ssop-subsurface-salinity.png',
        'icon-hover-src': 'ico-ssop-subsurface-salinity_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Physical',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    # OCEANIC -  Biogeochemistry
    {
        'id': 'obgc-3',
        'title': 'Nutrients',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obgc-nutrients.png',
        'icon-hover-src': 'ico-obgc-nutrients_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemistry',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'obgc-4',
        'title': 'Transient Tracers',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obgc-transient-tracers.png',
        'icon-hover-src': 'ico-obgc-transient-tracers_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemistry',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'obgc-5',
        'title': 'Nitrous Oxide',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obgc-nitrous-oxide.png',
        'icon-hover-src': 'ico-obgc-nitrous-oxide_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemistry',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'obgc-6',
        'title': 'Ocean Colour',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obgc-ocean-colour.png',
        'icon-hover-src': 'ico-obgc-ocean-colour_hover.png',
        'domain': 'Ocean',
        'subdomain': 'Biogeochemistry',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    # OCEANIC - BIOECO
    {
        'id': 'obe-1',
        'title': 'Marine Habitats',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obe-marine-habitat.png',
        'icon-hover-src': 'ico-obe-marine-habitat_hover.png',
        'domain': 'Biological/Ecosystems',
        'subdomain': 'Biosphere',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    {
        'id': 'obe-2',
        'title': 'Plankton',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-obe-plankton.png',
        'icon-hover-src': 'ico-obe-plankton_hover.png',
        'domain': 'Biological/Ecosystems',
        'subdomain': 'Biosphere',
        'scientific-area': '',
        'authors': '',
        'domain-color': OCEAN_COLOR,
        'domain-bg-color': OCEAN_BG_COLOR
    },
    # TERRESTRIAL - HYDROSPHERE
    {
        'id': 'hyd-2',
        'title': 'Lakes',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-hyd-lakes.png',
        'icon-hover-src': 'ico-hyd-lakes_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Hydrology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'hyd-3',
        'title': 'Groundwater',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-hyd-groundwater.png', 
        'icon-hover-src': 'ico-hyd-groundwater_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Hydrology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'hyd-4',
        'title': 'Soil Moisture',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-hyd-soil-moisture.png', 
        'icon-hover-src': 'ico-hyd-soil-moisture_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Hydrology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    # TERRESTRIAL - BIOSPHERE
    {
        'id': 'bio-4',
        'title': 'Above-ground Biomass',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-bio-above-ground-biomass.png',
        'icon-hover-src': 'ico-bio-above-ground-biomass_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'bio-5',
        'title': 'Albedo',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-bio-albedo.png',
        'icon-hover-src': 'ico-bio-albedo_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'bio-6',
        'title': 'Land Surface Temperature',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-bio-land-surface-temperature.png',
        'icon-hover-src': 'ico-bio-land-surface-temperature_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'bio-7',
        'title': 'Leaf Area Index (LAI)',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-bio-leaf-area-index.png',
        'icon-hover-src': 'ico-bio-leaf-area-index_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },
    {
        'id': 'bio-8',
        'title': 'Soil Carbon',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-bio-soil-carbon.png',
        'icon-hover-src': 'ico-bio-soil-carbon_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
        'scientific-area': '',
        'authors': '',
        'domain-color': TERRESTRIAL_COLOR,
        'domain-bg-color': TERRESTRIAL_BG_COLOR
    },    
    {
        'id': 'ant-2',
        'title': 'Anthropogenic Water Use',
        'href': '',
        'icon-lg-src': '',
        'icon-lg-hover-src': '',
        'icon-src': 'ico-ant-wateruse.png',
        'icon-hover-src': 'ico-ant-wateruse_hover.png',
        'domain': 'Terrestrial',
        'subdomain': 'Biology',
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


IMAGES_PATH = '/dash/assets/images/'
# IMAGES_PATH='/Users/dan/ClimateIreland/Projects/CI-Status-Report-Dash/assets/images/'
# IMAGES_PATH='https://www.climateireland.ie/web_resource/images/'

PROJECT_PATH = pathlib.Path(__file__).parent.parent
if os.path.isdir(str(PROJECT_PATH)+'/data'):
    DATA_PATH = str(PROJECT_PATH)+'/data/'
else:
    DATA_PATH = "/home/data/"
