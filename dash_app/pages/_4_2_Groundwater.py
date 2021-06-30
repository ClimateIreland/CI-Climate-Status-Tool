import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Groundwater_Ned_Dwyer_P1090393.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Groundwater is located beneath the ground surface in pore spaces and fractures 
of geological formations. It is estimated that almost 30% of the world’s 
fresh water is stored as groundwater. Globally, it is a major source of 
drinking water and is also widely used in agriculture and industry. 
Groundwater volumes and levels are influenced by not only rainfall and dry 
periods but mainly human use.
        """
bulletPoint1 = """
In Ireland about 18% of drinking water is from groundwater sources. 
        """
bulletPoint2 = """
Abstraction, especially in the world’s arid and semi-arid zones, is leading to 
rapid rates of groundwater depletion.  
        """
bulletPoint3 = """
Regular analysis of groundwater levels in Ireland is carried out but not 
primarily for identifying climate-driven changes.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
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
