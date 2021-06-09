import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_13_b, map_2_7

chapter_num = '2.7b'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Upper Air_Met_Eireann_Fig14.jpg'
bannerImgCredit = 'Met Eireann'

introText = """

        """
bulletPoint1 = """

        """
bulletPoint2 = """

        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Upper Air Wind Speed - Valentia, Co.Kerry'
trendChart = figure_2_13_b()

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = map_2_7()

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
