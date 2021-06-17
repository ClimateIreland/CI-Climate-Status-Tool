import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_4, map_2_2

chapter_num = '2.2'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Wind_Myrtleville_Ophelia_Aldert Otter.jpg'
bannerImgCredit = 'Aldert Otter'

introText = """
Wind is the movement of air caused by pressure differences at the Earth’s surface, 
which in turn are caused by the differential heating of the Earth’s surface by the sun. 
Wind drives the production of ocean waves and is a key component of ocean circulation, 
which is responsible for the global transport of heat and carbon. Extreme winds, 
especially during storms, can have huge social and economic impacts.  
        """
bulletPoint1 = """
      No long-term trend in wind speed can be 
      determined with confidence based on the limited analysis carried out to date.
        """
bulletPoint2 = """
      Comprehensive analysis of wind data will be carried out by Met Éireann during 2021.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()
trendChartA, trendChartB = figure_2_4()
trendChart = trendChartA

trendCaption = """
    Annual mean wind speeds (top) and number of days per year with gale gusts (bottom) 
    at Valentia Observatory (1940–2019) and Dublin Airport (1944–2019). At Valentia a 
    slightly decreasing trend in both parameters can be observed during the last two decades, 
    while in Dublin the number of days with gale gusts also shows a decreasing trend. However, 
    because of instrument changes in the 1990s and a lack of homogenisation of the full data record, 
    long-term trends cannot be determined with confidence.
        """



infrastructureText = """
    Wind speed and direction are measured  at the 23 synoptic weather stations (red) operated 
    by Met Éireann and at the 5 Irish Marine Data Buoy Observation Network stations (orange). 
    Additional parameters are calculated including gust speeds, the times of highest daily gusts, 
    the mean wind speed and direction at the time of the highest gust and the highest 
    10-minute mean speed in a 24-hour period. Records available in Ireland go back 
    several decades at a number of stations, although there has been an upgrade and change in 
    measurement equipment in the 1990s at many of these. As well as precipitation, rainfall 
    radar also measure wind speed and direction and Met Éireann contributes to the 
    E-WINPROF European wind profiler programme.
    Space-borne radar scatterometer and passive microwave 
    radiometer data are key sources for wind-field information over the ocean, 
    where in situ measurements are sparse.

        """
infrastructureMap = map_2_2()

infoLinks = [
    {'text': 'Surface Wind Speed and Direction ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS. ',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-wind'},
         {'text': 'Met Éireann data source',
     'url': 'https://www.met.ie/climate/available-data/historical-data'},
         {'text': 'Met Éireann Wind measurements information',
     'url': 'https://www.met.ie/climate/what-we-measure/wind'},
         {'text': 'Information on data availability',
     'url': 'https://www.met.ie/climate/available-data'},
         {'text': 'Information from the Irish Marine Data Buoy Observation Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/irish-marine-data-buoy-observation-network'},
         {'text': 'About EUMETSAT, Europe´s weather satellite programme',
     'url': 'https://www.eumetsat.int/website/home/index.html'},
         {'text': 'European wind profiler and weather radar (winds) network',
     'url': 'http://cfa.aquila.infn.it/wiki.eg-climet.org/index.php5/E-WINPROF'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

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
                dbc.Col(className="col-12",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Wind Speed and Gale Gust Days')]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Valentia'),
                            dcc.Graph(
                                figure=trendChartA,
                                config={'displayModeBar': False})]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Dublin Airport'),
                            dcc.Graph(
                                figure=trendChartB,
                                config={'displayModeBar': False})]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    className="col-md-10 offset-md-1",
                    children=[
                        html.P(
                            className='sr-chart-caption',
                                    children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption]
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
