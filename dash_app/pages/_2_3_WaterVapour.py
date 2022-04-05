import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_6, map_2_3
import copy

chapter_num = '2.3'
bannerImgSrc = IMAGES_PATH + \
    'AtmosphericSections/Water_Vapour_madeleineweber_valentiamist.jpg'
bannerImgCredit = 'Madeleine Weber'

introText = """
    Water vapour is a gaseous constituent of air at all levels in the 
    atmosphere, accounting for almost 60% of the natural greenhouse effect. 
    Evaporation from the Earth’s surface is the source of water in the 
    atmosphere, which condenses to form clouds, changing radiative properties 
    and releasing heat that affects atmospheric circulation systems. 
        """
bulletPoint1 = """
    Globally, higher air temperatures and warmer oceans have led to an 
    increase in atmospheric water vapour, which may be linked to more 
    intense precipitation events and enhanced warming.   
        """
bulletPoint2 = """
    No significant annual trend is apparent in water vapour measurements 
    over Ireland, but more comprehensive analysis of the data is required.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''

trendCaption = """

        """

infrastructureText = """
Surface level water vapour and water vapour pressure are derived from humidity 
measurements taken at the 25 synoptic weather stations (red) operated by Met 
Éireann. Since 1943 weather balloons which are launched a number of times a day
 from Valentia Observatory in Co. Kerry, measure the humidity up through the 
 atmosphere. Since 2009 Ireland has contributed to the E-GVAP Programme of 
 EUMETNET, retrieving column-integrated water vapour quantities from the 
 Ordnance Survey Ireland (OSI) Global Navigation Satellite System (GNSS) active
  network (blue) on an hourly basis. A number of instruments on different 
  satellites measure water vapour. These include the HIRS, MHS and AMSU-A 
  sensors that are part of the Metop satellite constellation operated by 
  EUMETSAT. 

        """
infrastructureMap = map_2_3()

infoLinks = [
    {'text': 'Surface Water Vapour ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-vapour/'},
        {'text': 'Upper-air Water Vapour ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/upper-vapour'},
        {'text': 'Met Éireann data source',
     'url': 'https://www.met.ie/climate/available-data/historical-data'},
        {'text': 'Met Éireann Water Vapour measurements information',
     'url': 'https://www.met.ie/climate/what-we-measure/water-vapour'},
        {'text': 'Valentia Observatory information',
     'url': 'https://www.met.ie/about-us/our-history/valentia-observatory'},
        {'text': 'About EUMETSAT, Europe´s weather satellite programme',
     'url': 'https://www.eumetsat.int/about-us/who-we-are'},
        {'text': 'About EUMETNET',
     'url': 'https://www.eumetnet.eu/about-us/'},
        {'text': 'E-GVAP observation Programme information',
     'url': 'https://www.eumetnet.eu/activities/observations-programme/current-activities/e-gvap/'},
        {'text': 'OSI active GNSS data',
     'url': 'https://www.osi.ie/services/geodetic-services/active-gnss-data/'},
]





########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)
combined_chapter_dict = copy.copy(chapter_dict)
combined_chapter_dict['title'] = 'Surface and Upper Air Atmosphere Water Vapour'
combined_chapter_dict['subdomain'] = 'Surface / Upper Atmosphere'

trendChart1, trendChart2 = figure_2_6()
trendChartTitle1 = 'Monthly Average Vapour Pressure - Valentia'

trendCaption1 = """
Monthly average water vapour pressure at Valentia Observatory (1940-2019). 
It is higher in summer as the air is warmer and can hold more moisture. 
        """

trendChartTitle2 = 'Mean Annual Vapour Pressure - Valentia'

trendCaption2 = """
Mean annual water vapour pressure at Valentia Observatory (1940-2019).
        """

trendImage = IMAGES_PATH+'AtmosphericSections/VapourPressureCurves2019.png'
trendCaption3 = """
Annual average water vapour pressure across Ireland for 2019.
"""

custom_trend_alt = dbc.Container(
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
                dbc.Col(className="col-12 col-lg-5   text-center my-auto",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle),
                            html.Img(
                                        style={"max-width": "400px"},
                                        src=trendImage
                                        ),
                                               dbc.Row(
            children=[
                dbc.Col(className="",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption3]
                            )]
                        )
            ]
        ),
                        ]),
                dbc.Col(className="col-12 col-lg-7 my-auto",
                        children=[
                dbc.Row(
            children=[
                dbc.Col(className="",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle1),
                            dcc.Graph(
                                figure=trendChart1,
                                config={'displayModeBar': False})]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="",
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
                dbc.Col(className="",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle2),
                            dcc.Graph(
                                figure=trendChart2,
                                config={'displayModeBar': False})]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption2]
                            )]
                        )
            ]
        )
                        ])
            ]
        ),


    ])

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
                dbc.Col(className="col-md-10 offset-md-1 text-center my-auto",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle),
                            html.Img(
                                        style={"max-width": "400px"},
                                        src=trendImage
                                        ),
                                ]
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
                                    trendCaption3]
                            )]
                        )
            ]
        ),
                dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle1),
                            dcc.Graph(
                                figure=trendChart1,
                                config={'displayModeBar': False})]
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
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle2),
                            dcc.Graph(
                                figure=trendChart2,
                                config={'displayModeBar': False})]
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
        )
    ])



def create_layout(app):
    return html.Div(
        children=[
            pb.build_banner(bannerImgSrc,
                            bannerImgCredit,
                            combined_chapter_dict
                            ),
            pb.build_breadcrumb(combined_chapter_dict),
            pb.build_nav(combined_chapter_dict),
            pb.build_intro(introText,
                           bulletPoints,
                           combined_chapter_dict
                           ),
            custom_trend_alt,

            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
