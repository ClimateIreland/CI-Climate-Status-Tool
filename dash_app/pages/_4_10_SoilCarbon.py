import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Soil Carbon_Teagasc.jpg'
bannerImgCredit = 'Teagasc'

introText = """
Organic carbon in soil is derived from decomposition of plant matter, such as 
leaf litter and woody debris, and is a significant part of the carbon cycle. 
Carbon is incorporated into vegetation through the process of photosynthesis, 
whereby CO\u2082 is sequestered from the atmosphere. The amount of carbon present 
in the soil is determined by geology, soil type, climate and land use.
        """
bulletPoint1 = """
Peat soils dominate the terrestrial carbon budget and store some 1566 million 
tonnes of carbon, representing approximately 64% of the total soil organic 
carbon stock present in Ireland.
        """
bulletPoint2 = """
Soil organic carbon in agricultural lands is highest in the west and around 
the Wicklow mountains in areas with higher precipitation and close to peatlands. 
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
