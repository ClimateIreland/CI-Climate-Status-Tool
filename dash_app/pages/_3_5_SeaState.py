import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Sea_State_Tomasz_SzumskiDSC_9048.JPG'
bannerImgCredit = 'Tomasz_Szumski'

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
Seasonal variations in wave heights are observed at buoys deployed of the coast
 of Ireland, however no comprehensive analysis of wave parameters has been 
 carried out on these data. 
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
