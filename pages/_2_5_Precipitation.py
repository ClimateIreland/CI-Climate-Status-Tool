import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_2_9, map_2_5

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
In Ireland the decade from 2006 to 2015 has been the wettest in the period 1711 to 2016.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]

trendChartTitle = 'Annual Rainfall Totals and Anomalies'
trendChart = figure_2_9()

trendCaption = """
Annual rainfall totals and anomalies averaged over Ireland (1941–2019).
        """

infrastructureText = """
Being a key indicator, precipitation has been measured systematically in 
Ireland since the late nineteenth century with a peak of over 800 rainfall
stations in the late 1950s. Currently precipitation is measured at the 25 
synoptic (red) and 57 climatological (blue) weather stations; in addition, 
there is a wide network of over 400 voluntary rainfall observers (yellow) 
(map 2.5). At the synoptic stations, readings are made continuously 
and reported on the hour; at climate and rainfall stations a daily 
precipitation total is recorded each day at 09:00 am. 
There are some gauges in remote locations which are read once a month.  
All precipitation data since January 1941 are available in digital format. 
        """
infrastructureMap = map_2_5()

infoLinks = [
    {'text': '',
     'url': ''},

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
