import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_10, map_3_5

chapter_num = '3.5'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Sea_State_Tomasz_SzumskiDSC_9048.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
Observations of wave height, direction, length, frequency and swell are relevant 
for monitoring changes in the marine environment, such as winds, storms and 
extreme events. Knowledge of the sea state and how it is changing is also vital
 for marine safety, marine transport, ocean energy development, coastal erosion
  and storm-related flooding, among others.
        """
bulletPoint1 = """
Increasing wave heights have been observed over the last 70 years in the North 
Atlantic with typical winter season trends of increases up to 20 cm per decade,
 along with a northward displacement of storm tracks.
        """
bulletPoint2 = """
Seasonal variations in wave heights are observed at buoys deployed off the coast
 of Ireland, however no comprehensive analysis of wave parameters has been 
 carried out on these data. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Wave height and wave period measurements have been made at the Irish Marine 
Data Buoy Observation Network (IMDBON) (orange) since 2002 and in addition since 
2013 wave direction has been measured.  Wave height, wave period and 
direction measurements are also made as part of the Ocean Energy Programme by 
the Waverider network (yellow) operated by the Marine Institute. 
Radar altimeters, on board a number of satellites including the Jason and 
Sentinel series, make measurements from which wave height and wave frequency 
can be inferred. In situ measurements are required to calibrate and validate 
such measurements.
        """
infrastructureMap = map_3_5()

infoLinks = [
    {'text': 'Sea State ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/sea-state/'},
         {'text': 'Dataset from the Irish National Waverider Network',
     'url': 'http://www.digitalocean.ie/'},
         {'text': 'Information from the Irish Marine Weather and Wave Buoy Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/integrated-marine-observations'},
         {'text': 'Information about the Ocean Energy Programme',
     'url': 'https://www.marine.ie/Home/site-area/infrastructure-facilities/ocean-energy/marine-renewable-energy'},
         {'text': 'Copernicus Marine Environment Monitoring Service OCEAN PRODUCTS',
     'url': 'http://marine.copernicus.eu/services-portfolio/access-to-products/'},
]


###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Daily Average Significant Wave Height - Buoy M3'
trendChart1 = figure_3_10()

trendCaption1 = """
Daily averaged significant wave height at Buoy M3 off the southwest coast 
(2016-2018). Seasonal variations are evident.
        """

figure_3_11a = IMAGES_PATH+'OceanicSections/Figure3.11_HeatMapSignificantWaveHeight_BuoyM2.png'
figure_3_11b = IMAGES_PATH+'OceanicSections/Figure3.11_HeatMapSignificantWaveHeight_BuoyM3.png'
trendChartTitle2 = 'Monthly Mean of Average Significant Wave Height - Buoy M2 and M3'
trendChart2 = empty_chart()

trendCaption2 = """
Heat Map of Monthly Mean of Average Significant Wave Height at Buoys M2 and M3 
(2002 – 2018). The data are presented as percentiles of all data combined for 
both buoys. For example, the 75th percentile means that 75% of all the values 
are below 2.7 m and 25% of the values are above it. The values observed at the 
M3 buoy are higher than those observed at M2, which is in a less exposed 
location.
        """

trendChartTitle3 = ''
trendChart3 = empty_chart()

trendCaption3 = """

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
                                    children=trendChartTitle1),
                                dcc.Graph(
                                    figure=trendChart1,
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
                                     dbc.Col(className="col-12",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle2),
                                    ]
                            ),
                    dbc.Col(className="col-12 col-md-6",
                            children=[
                                    html.Img(
                                    className='w-100',
                                    src=figure_3_11a
                                )
                                    ]
                            ),
                        dbc.Col(className="col-12 col-md-6",
                            children=[
                                    html.Img(
                                    className='w-100',
                                    src=figure_3_11b
                                )
                                    ]
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
