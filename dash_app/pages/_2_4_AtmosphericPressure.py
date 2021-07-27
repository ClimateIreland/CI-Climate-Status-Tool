import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_8, map_2_4

chapter_num = '2.4'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Pressure_Tomasz_Szumski_DSC_9880.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
Atmospheric pressure is a key meteorological variable for monitoring the 
climate system, as the local and large-scale atmospheric circulation patterns 
are driven by differences in air pressure. Changes in large-scale pressure 
patterns can affect local and regional weather. 
     """
bulletPoint1 = """
An understanding of atmospheric pressure distributions is required for the 
long-term simulations of past weather and climate known as reanalyses. This 
understanding is also fundamental for weather forecasting.  
        """
bulletPoint2 = """
Resources are required to digitise older records and carry out comprehensive 
time series analysis, which would help in understanding if and how storm 
tracks are changing.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Annual and Monthly Surface Pressure - Valentia'
trendChart = figure_2_8()

trendCaption = """
Monthly and annual minimum, average and maximum surface pressure at Valentia 
Observatory, Co. Kerry (1940–2019). Little variation is seen in the average 
series. However, maximum and minimum series show greater variability, 
particularly the minimum values. This behaviour is linked to mid-latitude 
cyclones or low-pressure systems that frequently pass over Ireland. The very 
low pressure observed in December 1989 was associated with an Atlantic 
depression that passed over Ireland, causing some damage due to high seas, 
high tides and heavy rain.
     """

infrastructureText = """
Atmospheric pressure measurements are taken automatically at the 25 
synoptic weather stations (red dots) operated by Met Éireann. Pressure is 
also measured at the Irish Marine Data Buoy Observation Network stations 
(orange dots), the first of which was deployed in 2000. To allow for 
comparison between measurements at different locations and elevations, all 
pressure readings are converted to mean sea level (msl) pressure.
       """

infrastructureMap = map_2_4()

infoLinks = [
    {'text': 'Surface Pressure Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/pressure'},
     {'text': 'Met Éireann historical data',
     'url': 'https://www.met.ie/climate/available-data/historical-data'},
     {'text': 'Met Éireann information on atmospheric pressure measurements',
     'url': 'https://www.met.ie/climate/what-we-measure/atmospheric-pressure'},
     {'text': 'Information from the Irish Marine Data Buoy Observation Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/irish-marine-data-buoy-observation-network'},
     {'text': 'Information on Valentia Observatory',
     'url': 'https://www.met.ie/about-us/our-history/valentia-observatory'},
]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)


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
            pb.build_trend(trendChartTitle,
                           trendChart,
                           trendCaption,
                           chapter_dict
                           ),
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
