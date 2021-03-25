import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_1, figure_3_3, map_3_1
import copy

chapter_num = '3.1'
bannerImgSrc = IMAGES_PATH + \
    'OceanicSections/Sea_Temperature_Annual Ocean Climate Survey 2019_Photo by Tomasz Szumski_158.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
        The temperature of the ocean is influenced by a number of factors, including the amount of heat 
        from the sun transferred through the atmosphere to the water, surface and 
        subsurface circulation and current patterns. Heat uptake by the global ocean accounts for 
        more than 90% of the excess heat trapped in the Earth system in the past few decades. 
        """
bulletPoint1 = """
        The global ocean surface temperatures has increased by  approximately 0.7°C since the 1850s, 
        with the rate of warming estimated to have doubled since the 1990s.  
        """
bulletPoint2 = """
        The sea surface temperature record at Malin Head in the period 2009 to 2018  was on average 0.47°C above the 1981-2010 mean.
        """
bulletPoint3 = """
        Observations of the annual water temperature in the Rockall Trough at depths between 1500m and 2000m from 1975 to 2018 show no evident trend.   
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
trendChartTitle = 'Mean Sea Surface Temperature (1961-2018)'
trendChart = figure_3_1()

trendCaption = """
Mean annual sea surface temperature (SST) and anomalies at Malin Head (1961-2018).
        """

infrastructureText = """
Sea surface temperature (SST) measurements are made by the Irish Marine Data Buoy Observation Network 
(orange and red), at the Malin Head Co. Donegal weather station (yellow), at the Ballycotton Co. Cork 
tide gauge station (purple) and at wave buoys (brown and black) (map 3.1). A set of coastal temperature 
sensors (blue) installed predominately at aquaculture sites by the Marine Institute measure temperature 
but are not accurate enough for climate studies.
The Malin Head station has collected SST observations since 1958 and is the longest record available in Irish waters, 
although water temperature records for parts of the northeast Atlantic go back to 1850.\u000A\u000A
Measurements of subsurface ocean temperature in Irish waters are made by the Marine Institute at the M6 buoy mooring 
(red) and at the SmartBay Observatory (black) in Galway Bay.  Since 2008, the Marine Institute has deployed twenty 
Argo floats in the North Atlantic; these underwater autonomous profilers measure temperature and salinity down to a 
depth of 2000m and Ireland contributes to international efforts through the Euro-Argo programme
        """
infrastructureMap = map_3_1()

infoLinks = [
    {'text': '',
     'url': ''},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)
# deep copy insures object indepdence
chapter_dict_combined = copy.deepcopy(chapter_dict)
chapter_dict_combined['title'] = 'Surface and Sub-surface Temperature'

trendChartTitle2 = "Mean Sub-Surface Temperture (1975-2018)"
trendChart2 = figure_3_3()
trendCaption2 = """
Mean annual sea sub-surface temperature and anomalies at Rockall Trough (1500-2000m) on the Extended Ellett Line  (1961-2018). 
Line (Data Provider: National Oceanography Centre and Scottish Association for Marine Science – UK). Ref: ICES Report on Ocean Climate 2018.
"""


custom_intro = dbc.Container(
    style={'borderColor': chapter_dict_combined['domain-color']},
    className='sr-intro',
    children=[
        dbc.Row(
            children=[
                dbc.Col(className="col-6 col-md-1 offset-md-1 my-auto",
                        children=[
                            html.Img(
                                className='sr-intro-icon float-right',
                                src=IMAGES_PATH+'icons/' +
                                chapter_dict['icon-lg-src']
                            ), ]
                        ),
                dbc.Col(className="col-6 col-md-1  my-auto",
                        children=[
                            html.Img(
                                className='sr-intro-icon float-left',
                                src=IMAGES_PATH+'icons/'+'subsurface-temperature_1.png'
                            ),

                        ]
                        ),
                dbc.Col(className="col-12 col-md-7 my-auto text-center",
                        children=[
                            html.H1(
                                className='sr-ecv-heading',
                                children=chapter_dict_combined['title'],
                                style={
                                    'color': chapter_dict['domain-color']},
                            )]
                        ),

            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.P(
                            children=introText
                        )
                    ]

                )
            ]

        ),
        dbc.Row(
            children=[
                dbc.Col(
                    className='sr-bullet-col',
                    style={'backgroundColor': chapter_dict['domain-bg-color']},
                    children=[
                        html.Ul(
                            className='sr-bullet-ul',
                            children=[
                                html.Li(
                                    className='',
                                    children=point)
                                for point in bulletPoints]

                        )
                    ]
                )]

        ),
        dbc.Row(
            style={'color': chapter_dict['domain-color']},
            children=[
                dbc.Col(

                    className='col-xs-6 col-md-2',
                    children='Domain:'
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=chapter_dict['domain']
                ),
            ]
        ),
        dbc.Row(
            style={'color': chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    style={
                        'backgroundColor': chapter_dict['domain-bg-color']},
                    className='col-xs-6 col-md-2',
                    children='Subdomain:'
                ),
                dbc.Col(
                    style={
                        'backgroundColor': chapter_dict['domain-bg-color']},
                    className='col-xs-6 col-md-10',
                    children=chapter_dict['subdomain']
                ),
            ]
        ),
        dbc.Row(
            style={'color': chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    className='col-xs-6 col-md-2',
                    children='Scientific Area:'
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=chapter_dict['scientific-area']
                ),
            ]
        ),
        dbc.Row(
            style={'color': chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    className='col-xs-6 col-md-2',
                    children='Authors:',
                    style={
                        'backgroundColor': chapter_dict['domain-bg-color']},
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=chapter_dict['authors'],
                    style={
                        'backgroundColor': chapter_dict['domain-bg-color']},
                ),
            ]
        ),
    ])

custom_trend =  dbc.Container(
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
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle),
                                dcc.Graph(
                                    figure=trendChart,
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
                                    children=trendCaption
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
                                    children=trendCaption2
                                )]
                            )
                ]
            ),
        ])


########################################################################################################################
def create_layout(app):
    return html.Div(
        children=[
            pb.build_banner(bannerImgSrc,
                            bannerImgCredit,
                            chapter_dict_combined
                            ),
            pb.build_breadcrumb(chapter_dict_combined),
            pb.build_nav(chapter_dict),
            custom_intro,
            # pb.build_intro(introText,
            #                bulletPoints,
            #                chapter_dict
            #                ),
            custom_trend,
    
            # pb.build_trend(trendChartTitle,
            #                trendChart,
            #                trendCaption,
            #                chapter_dict
            #                ),
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
