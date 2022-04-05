import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_2_1, figure_2_3, map_2_1

chapter_num = '2.1'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/AirTemp_MetEireann.jpg'
bannerImgCredit = 'Met Éireann'

introText = """
        Surface air temperature is a key climate indicator and has widespread impacts 
        on natural systems and on human lives and activities. 
        It affects health, agriculture, energy demand and much more. 
        The global mean surface air temperature has increased on average by 0.85°C over 
        the last century, but the rate of warming has nearly doubled since 1975 to 
        almost 1.65°C per century.
        """
bulletPoint1 = """
        In Ireland the annual average surface air temperature has increased by 
        approximately 0.9°C over the last 120 years.
        """
bulletPoint2 = """
        The number of warm spell days across Ireland has slightly 
        increased over the last 60 years.
        """

bulletPoints = [bulletPoint1, bulletPoint2]

trendChartTitle = 'Surface Air Temperature - Ireland'
trendChart = figure_2_1()

trendCaption = """
        A time series graph of mean annual observed temperature for Ireland (1900-2019) (yellow dots) 
        along with simple statistical fits to the data. 
        The left hand axis indicates anomalies (the difference between the mean annual temperature and the 1961-1990 
        normal or reference mean value) and the right-hand axis the mean annual temperature for the period. 
        A simple linear trend line (green dashed ) has been fitted to the annual anomaly values. 
        This indicates that temperature has been increasing at an average rate of 0.078°C per decade since 1900 
        and that the annual average temperature is now approximately 0.9°C higher than it was in the early 1900s. 
        Fifteen of the top 20 warmest years on record have occurred since 1990.
        """
trendChart2, trendChart3 = figure_2_3()
trendChartTitle2 = 'Cold Spell Days'
trendChartTitle3 = 'Warm Spell Days'
trendCaption2 = """
       Trend in number of annual cold spell days (number of days in a year with temperature below a certain threshold 
       for at least 6 consecutive days) per decade and number of annual warm spell days (number of days in a year 
       with temperature above a certain threshold for at least 6 consecutive days)  per decade (1961–2018). 
       For example, there are on average 2 or 3 additional warm spell days each decade at Belmullet, Co. Mayo, over the six decades analysed. 
       The trends indicate a slight increase in the number of warm spell days across the whole country and very little change in the number 
       of cold spell days.
        """

infrastructureText = """
        Surface air temperature is measured at the 25 synoptic (red) and numerous climatological 
        (blue) weather stations and also at the Irish Marine Data Buoy Observation Network stations (orange). 
        Readings at automated synoptic stations are made every minute and at staffed stations, located in the main airports, 
        every hour on the hour; at climatological stations readings of maximum and minimum temperature over the previous 24 
        hours are made once a day at 0900 Coordinated Universal Time (UTC). Eighty climatological stations are currently 
        being automated to facilitate sub-hourly temperature measurements. Surface air temperature is measured every hour 
        on the marine data buoys, the first of which was deployed in 2000.
        """
infrastructureMap = map_2_1()

infoLinks = [{'text': 'Surface Temperature ESSENTIAL CLIMATE VARIABLES (ECV). GCOS FACTSHEETS',
              'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-temperature/'},

             {'text': 'ETCCDI/CRD Climate Change Indices. Definition of the 27 core indices',
             'url': 'http://etccdi.pacificclimate.org/list_27_indices.shtml'},

             {'text': 'Met Éireann information on air temperature in Ireland',
             'url': 'https://www.met.ie/climate/what-we-measure/temperature'},

             {'text': 'Met Éireann information on data availability',
             'url': 'https://www.met.ie/climate/available-data/'},

             {'text': 'Information from the Irish Marine Weather Buoy Network',
             'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/irish-marine-data-buoy-observation-network'},

             {'text': 'NOAA BAMS annual State of the Climate reports',
             'url': 'https://www.ncdc.noaa.gov/bams'},

             {'text': 'WMO State of the Climate 2020 report',
             'url': 'https://public.wmo.int/en/our-mandate/climate/wmo-statement-state-of-global-climate'}
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
                                children=[
                                    html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption]
                            )]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle2),
                            dcc.Graph(
                                figure=trendChart2,
                                config={'displayModeBar': False,
                                        'scrollZoom': False, },
                            )]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle3),
                            dcc.Graph(
                                figure=trendChart3,
                                config={'displayModeBar': False,
                                        'scrollZoom': False, },
                            )]
                        ),
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[
                                    html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption2]
                            )]
                        )
            ]
        ),
    ])


def create_chart(app):
    return dcc.Graph(
        figure=trendChart,
        config={'displayModeBar': False})


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
