import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Salinity_TomaszSzumski.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
Salinity is defined as the total amount of dissolved salts in water. 
These salts constitute approximately 3.5% of the ocean’s mass. Globally, 
areas that currently have net evaporation are expected to become saltier 
at the ocean surface, while areas with net precipitation, increased river 
un-off and land ice melt are expected to get fresher. Salinity and temperature 
control water density and are key variables for identifying and tracing 
ocean water masses and for understanding ocean physical processes. 
        """
bulletPoint1 = """
Decadal changes have taken place, and an unprecedented reduction in salinity 
levels has been observed in recent years in the North-east Atlantic, based on 
an analysis of 120 years of data.
        """
bulletPoint2 = """
Monitoring of changes in ocean salinity is an indirect method of detecting 
changes in precipitation, evaporation, river run-off and ice melt and therefore
 helps in understanding changes in the Earth’s hydrological cycle.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': '',
     'url': ''},

]


###############################################################################
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
