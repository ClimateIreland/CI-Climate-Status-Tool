import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_2_9, figure_2_10, map_2_5, empty_chart

chapter_num = '2.5'
bannerImgSrc = IMAGES_PATH + \
    'AtmosphericSections/Precipitation_Glendalough-Lynn Walsh.JPG'
bannerImgCredit = 'Lynn Walsh'

introText = """
Rainfall (precipitation) plays a vital role in the water cycle and water balance and is essential for the maintenance of life.   
An understanding of precipitation distribution and trends is essential for assessing potential effects of climate change on 
the supply of water and for supporting both flood and drought mitigation initiatives. 
        """
bulletPoint1 = """
Globally there has been a discernible intensification in heavy rainfall events over the second half of the 20th century.
        """
bulletPoint2 = """
In Ireland the decade from 2006 to 2015 has been the wettest in the period 1711 to 2016.
        """

bulletPoint3 = """
There is evidence that there is an increasing trend in winter rainfall and a decrease in summer rainfall.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]

trendChartTitle = 'Annual Rainfall Totals and Anomalies'
trendChart = figure_2_9()

trendCaption = """
A time-series graph (1941-2019) of the annual average rainfall totals (yellow bars, right-hand axis) 
and the annual anomalies, or differences, from the 1961–1990 normal (left-hand axis). 
A moving average for periods of 11 years is also shown (blue line). 
Since the 1980s an increasing trend can be observed in the 11-year moving average. 
Compared with an annual average rainfall of 1186 mm in the period 1961–1990 (blue dashed line), 
the last 30-year period (1990–2019) (blue dashed line) shows a 79 mm or almost 7% increase in annual rainfall.
        """


trendChart2, trendChart3 = figure_2_10()
trendChartTitle2 = 'Wet Spell Days'
trendChartTitle3 = 'Dry Spell Days'
trendCaption2 = """
Trends in the maximum length of annual wet spell days 
(maximum number of consecutive days with precipitation of 1 mm or above) 
per decade and the maximum length of annual dry spell days 
(maximum number of consecutive days with precipitation below 1 mm) per decade. 
For example, there is on average 1 additional wet spell day in each decade at Valentia, Co. Kerry, 
over the six decades analysed. The trends indicate an increase in the length of wet spell days across 
all of the country; however, no consistent trend is apparent in dry spell days.
        """

infrastructureText = """
Precipitation is measured at the 25 synoptic (red) and 57 climatological (blue) weather stations; 
in addition, there is a wide network of over 400 voluntary rainfall observers (yellow). 
At the synoptic stations, readings are made continuously and reported on the hour; at climatological 
and rainfall stations a daily precipitation total is recorded each day at 0900. There are some gauges 
in remote locations that are read once a month.
        """
infrastructureMap = map_2_5()

infoLinks = [
    {'text': 'Precipitation ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/precipitation'},

    {'text': 'Murphy, C., Broderick, C. et al., 2018, A 305-year continuous monthly rainfall series for the island of Ireland (1711–2016), Climate of the Past, 14, 413–440',
     'url': 'https://doi.org/10.5194/cp-14-413-2018'},

    {'text': 'ETCCDI/CRD Climate Change Indices. Definition of the 27 core indices',
     'url': 'http://etccdi.pacificclimate.org/list_27_indices.shtml'},

    {'text': 'Information on precipitation in Ireland',
     'url': 'https://www.met.ie/climate/what-we-measure/rainfall'},

    {'text': 'Information on data availability',
     'url': 'https://www.met.ie/climate/available-data'},

    {'text': 'About EUMETSAT, Europe´s weather satellite programme',
     'url': 'https://www.eumetsat.int/website/home/index.html'},

    {'text': 'About EUMETNET',
     'url': 'https://www.eumetnet.eu/about-us/'},

    {'text': 'About the Global Precipitation Measurement mission',
     'url': 'https://www.nasa.gov/mission_pages/GPM/overview/index.html'},
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
                                children=trendCaption
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
                                 config={'displayModeBar': False,'scrollZoom': False,},
                                )]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle3),
                            dcc.Graph(
                                figure=trendChart3,
                                config={'displayModeBar': False,'scrollZoom': False,},
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
                                children=trendCaption2
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
        #     pb.build_trend(trendChartTitle,
        #                    trendChart,
        #                    trendCaption,
        #                    chapter_dict
        #                    ),
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
