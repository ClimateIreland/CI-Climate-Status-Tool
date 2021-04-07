import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart,figure_3_8, map_3_4, figure_3_7_1, figure_3_7_2, figure_3_7_3, figure_3_7_4

chapter_num = '3.4'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Sea_Level_Aldert Otter.jpg'
bannerImgCredit = 'Aldert Otter'

introText = """
        Sea Level is among the primary indicators of global climate change. 
        Sea level continues to rise because increasing global temperatures cause 
        thermal expansion of the oceans as well as increasing freshwater input due 
        to melting land ice sources (e.g. glaciers and ice sheets, permafrost). 
        """
bulletPoint1 = """
        Estimates show that globally, average sea level has risen approximately 160 mm 
        since 1902, at a rate of approximately 1.4mm per year. 
        """
bulletPoint2 = """
        Satellite observations indicate that the sea level around Ireland has 
        risen by approximately 2-3mm/year since the early 1990s.
        """
bulletPoints = [bulletPoint1, bulletPoint2]

# first chart
trendChartTitle = 'Mean Sea Level - Dublin Port' #(1938-2016)
trendChart = figure_3_8()
trendCaption = """
The complete time series for the Dublin Port monthly mean sea level from 1938 to 2016 (updated by Maynooth University). 
Since the 1980s there has been significant variability in the record, with an upward trend over the last 25 years. 
The attribution of this recent increase is not certain. However, taken over the full time period, the sea level in 
Dublin has risen by 1.67 mm per year, consistent with global rates.
        """

# second chart
trendChartTitle2 = 'Malin Head'
trendChart2 = figure_3_7_1()

# third chart
trendChartTitle3 = 'Ballyglass Harbour'
trendChart3 = figure_3_7_2()

# fourth chart
trendChartTitle4 = 'Castletownbare Port'
trendChart4 = figure_3_7_3()

# fifth chart
trendChartTitle5 = 'Howth Harbour'
trendChart5 = figure_3_7_4()

trendCaption2 = """
Tide gauge measurements at four different locations, in the north, west, south and east respectively, since the mid-2000s. 
The time series are not yet long enough to accurately determine any trend. Moreover, any land elevation changes due to 
glacial isostatic adjustment or other factors are not taken into account.
        """

infrastructureText = """
Measurements of sea level rely on high precision contemporaneous measurements of sea and land level. 
Measurements of relative sea levels are mainly made by a network of tide gauges around the Irish Coast, 
which are operated by a number of different bodies including the Marine Institute (MI) (blue), the Office of Public Works (OPW) 
(red and yellow), Local Authorities and Port Companies (brown and orange) (map 3.4). 
The “EPA Gauging Station Register” is a national inventory for all gauges including tide gauges. 
The longest continuous records for Ireland are from Dublin Port (orange) where a tide gauge has been 
in operation since at least 1923, with digitised records available from 1938, and from Malin Head, Co. Donegal (yellow), 
in operation since 1958.
        """
infrastructureMap = map_3_4()

infoLinks = [
    {'text': 'Sea level ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/sea-level/'},

     {'text': 'Nejad, A.S., Parnell, A., Greene, A., et al. (2020, May 27) Recent Rapid Sea Level Rise in Dublin Bay Based on Tide Gauge Analysis',
     'url': 'https://doi.org/10.31223/osf.io/z9hk2'},

     {'text': 'Dataset from the Irish National Tide Network project portal',
     'url': 'http://www.Irishtides.ie'},

     {'text': 'Hydrometric data from the Office of Public Works',
     'url': 'https://waterlevel.ie/group/16/'},

     {'text': 'Dataset from the GLOSS sea level data centres',
     'url': 'https://www.gloss-sealevel.org/data'},

     {'text': 'Tide gauge data from around the world',
     'url': 'https://www.psmsl.org/data/'},

     {'text': 'Information on sea level retrieval from altimeters for the Copernicus Programme',
     'url': 'https://duacs.cls.fr/'},

     {'text': 'Sea Level. European State of the Climate 2018',
     'url': 'https://climate.copernicus.eu/sea-level'},

     {'text': 'Sea Level Global and Regional interactive products based on satellite information',
     'url': 'https://www.aviso.altimetry.fr/?id=1599'},


]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

# create a custom layout for >1 chart
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
            # First chart
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
            # Second chart
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
            # Third chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle3),
                                dcc.Graph(
                                    figure=trendChart3,
                                    config={'displayModeBar': False})]
                            )
                ]
            ),
        # Fourth chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle4),
                                dcc.Graph(
                                    figure=trendChart4,
                                    config={'displayModeBar': False})]
                            )
                ]
            ),
        # Fifth chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle5),
                                dcc.Graph(
                                    figure=trendChart5,
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
                        #    trendChart,
                        #    trendCaption,
                        #    chapter_dict
                        #    ),
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
