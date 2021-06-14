import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_24

chapter_num = '4.12'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Land_Surface_Temp_HayBales-Peter Dominiak.jpg'
bannerImgCredit = 'Peter Dominiak'

introText = """
    The land surface temperature (LST) – the temperature of the land surface rather 
    than that of the near-surface air – is a fundamental aspect of climate and biology, 
    affecting organisms and ecosystems from local to global scales. LST is a mixture 
    of vegetation and bare soil temperatures. This parameter is key to understanding 
    terrestrial thermal behaviour and the exchange processes between the 
    land surface and the atmosphere. 
        """
bulletPoint1 = """
    In the period 2002 to 2018 the highest LST occurred during the summers of 2013 and 2018.
        """
bulletPoint2 = """
    In summer LST can reach 40°C in some parts of the east of the country.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Area-Averaged Monthly Land Surface Temperature Over Ireland'
trendChart = figure_4_24()

trendCaption = """

        """

infrastructureText = """
Ground-based measurements of LST tend to be made only at local scales, for research studies. There is no long-term in situ LST monitoring programme in Ireland. Regional and global LST measurements are generally made by satellite sensors, which have the ability to measure the thermal infra-red radiation emitted by the Earth’s surface on a regular basis. The Copernicus Global Land Service (CGLS) generates a LST dataset as part of a set of energy monitoring products. This dataset is derived from the Meteosat Second Generation (MSG), the GOES and the MTSAT satellites. In addition, one of the longest global time series of LST is derived from the MODIS instruments aboard the Terra and Aqua satellites. 
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'LST ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/land-temperature/'},
         {'text': 'Copernicus Global Land Service (CGLS) data',
     'url': 'https://land.copernicus.eu/global/products/sa'},
         {'text': 'NASA’S Earth Observing System Data',
     'url': 'https://giovanni.gsfc.nasa.gov/giovanni/'},
         {'text': 'Information about SENTINEL-3 SLSTR',
     'url': 'https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-slstr'},
         {'text': 'LST ESA Climate Change Initiative project',
     'url': 'http://cci.esa.int/lst'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption1 = """
Time series of monthly average Land Surface Temperature for day and night time over Ireland derived from MODIS for the period of 2002 to 2018. 
        """

trendCaption2 = """
Maximum Land Surface Temperature during four 10-day periods in 2018 derived from the Copernicus Global Land Service (CGLS) datasets.    © European Union, Copernicus Land Monitoring Service 2020, European Environment Agency (EEA).
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
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle),
                                dcc.Graph(
                                    figure=trendChart,
                                    id='chart'+chapter_dict['href'],
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
                                    children='Max. Land Surface Temperature Over Four 10-Day Periods in 2018'),
                                html.Img(src=IMAGES_PATH+'TerrestrialSections/LST_Seasonal_Maps.png')]
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
                                        trendCaption2]
                                )]
                            )
                ]
            ),
        ])

custom_infrastructure = dbc.Container(
        className='sr-infrastructure',
        style={'borderColor': chapter_dict['domain-color']},
        id='infrastructure',
        children=[
            html.H3(
                className='sr-section-heading',
                children='Infrastructure',
                style={'color': chapter_dict['domain-color']},
            ),
            dbc.Row(
                children=[
                    dbc.Col(className="col-12 my-auto",
                            children=[
                                html.P(infrastructureText)]
                            ),
   
                ])
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
        #     pb.build_trend(trendChartTitle,
        #                    trendChart,
        #                    trendCaption,
        #                    chapter_dict
        #                    ),
            custom_trend,
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            custom_infrastructure,
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
