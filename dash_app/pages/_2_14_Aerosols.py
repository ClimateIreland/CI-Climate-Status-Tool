import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_2_14

chapter_num = '2.14'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Aerosols_Mihaly Csernus.jpg'
bannerImgCredit = 'Mihaly Csernus'

introText = """
    Atmospheric aerosols include windblown dust, sea spray, volcanic ash, smoke 
    from vegetation fires and pollution from factories and vehicles. 
    Aerosols are minor constituents of the atmosphere by mass but affect 
    climate dynamics in several ways and represent an area of great uncertainty in 
    the understanding of Earth’s climate system. 
        """
bulletPoint1 = """
     Aerosols influence the global radiation balance directly by scattering 
     and absorbing solar radiation and indirectly through influencing cloud 
     albedo (reflectivity), cover and lifespan. 
        """
bulletPoint2 = """
    Near-ground aerosols from smoke and other pollutants can also adversely affect human health.
        """
bulletPoint3 = """
    Measurements at Mace head between 1980 and 2015 show an almost 80% reduction in atmospheric sulfur pollution.    
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
    Aerosol observations are made at the Mace Head Atmospheric Research Station, Carna, Co. Galway 
    and Valentia Observatory, Co. Kerry. A range of aerosol parameters have been 
    measured on a continual basis at Mace Head, since 1986, although some measurements 
    took place on an intermittent basis from 1958. Measurements made include the scattering, 
    backscattering and absorption coefficient at various wavelengths; the total particle number 
    concentration, particle size and mass distribution; particulate matter (PM) mass (PM10 and PM2.5); 
    black carbon mass concentration, aerosol flux, aerosol optical depth, cloud condensation nuclei, 
    and aerosol chemical composition. This suite of measurements is one of the most comprehensive made 
    in at any remote location in the world and are webcast in near real time every 10-minutes. 
    Routine condensation nuclei measurements were made at Valentia Observatory between 1951 and 1994. 
    Measurements of aerosol optical depth are currently carried out at the Observatory.  
        """
infrastructureMap = map_2_14()

infoLinks = [
    {'text': 'Aerosol Properties ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/aerosols'},
         {'text': 'A description of the Aerosol Optical Depth Measurement Programme at Valentia Observatory',
     'url': 'https://www.met.ie/science/valentia/aerosol-optical-depth-measurement'},
         {'text': 'Information on the Mace Head Facility',
     'url': 'http://www.macehead.org/'},
         {'text': 'Real-time data from Mace Head',
     'url': 'http://www.macehead.org/index.php?option=com_content&view=category&layout=blog&id=96&Itemid=30'},
         {'text': 'Copernicus Atmospheric Monitoring Service',
     'url': 'https://www.copernicus.eu/en/services/atmosphere'},
         {'text': 'Copernicus Climate Change Service',
     'url': 'https://www.copernicus.eu/en/services/climate-change'},
         {'text': 'ESA Climate Change Initiative - Aerosol',
     'url': 'http://cci.esa.int/aerosol'},
         {'text': 'NASA Earth Observations (NEO)',
     'url': 'https://neo.sci.gsfc.nasa.gov/'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption1 = """
    Monthly (grey) and Yearly (green) median values of aerosol scattering coefficient 
    observed at Mace Head (1999-2015). There are some gaps in the data record. 
        """

trendCaption2 = """
Sulfur air pollution trends. SO\u2082 pollution levels measured at Valentia Observatory over 
the period of 1980–2018 and European SOx emissions over the same period. 
The dashed line represents an exponential fit to the SO\u2082 measurement data 
and the pink shaded area represents confidence bands (95%) of exponential 
fits to EU SOx emissions (left); non-sea-salt-SO\u2084 PM10 pollution levels 
measured at Valentia Observatory and non-sea-salt-SO\u2084 PM1 observed at 
Mace Head over the same time period of 1980–2018. The dashed line 
represents an exponential fit to the non-sea-salt-SO\u2084 PM10  measurement data (right). 
Both in terms of micrograms of sulfur per metre cubed (\u00b5gSm\u207b\u00b3). 
This shows a significant reduction (~80%) over a 35-year period (1980–2015) and is in line with European observations.
        """

custom_trend = dbc.Container(
    className='sr-trends',
    style={'borderColor': chapter_dict['domain-color']},
    id='trends',
    children=[
        html.H3(
            className='sr-section-heading',
            style={'color': chapter_dict['domain-color']},
            children='Trends',
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Aerosol Scattering Coefficient - Mace Head'),
                            html.Img(
                                src=IMAGES_PATH+'AtmosphericSections/Figure 2.28_MonthlyYearlyAerosolMaceHead.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          trendCaption1]
                            )]
                        )
            ]
        ),
                dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Sulfur Air Pollution Trends'),
                            html.Img(
                                src=IMAGES_PATH+'AtmosphericSections/Figure2.29_SulphurAirPollutionTrends_v2.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          trendCaption2]
                            )]
                        )
            ]
        ),
    ])
def create_layout(app):
    return html.Div(
        children=[
            pb.build_banner(bannerImgSrc,
                            bannerImgCredit,
                            chapter_dict
                            ),
            pb.build_breadcrumb(chapter_dict),
            pb.build_nav(chapter_dict),
            pb.build_intro(introText,
                           bulletPoints,
                           chapter_dict
                           ),
            custom_trend,
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
