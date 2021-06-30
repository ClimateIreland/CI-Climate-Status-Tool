import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Habitats_Tomasz_Szumski_IMG_9140_biodiscovery survey 2014.jpg'
bannerImgCredit = 'Tomasz Szumski'

introText = """
Seaweed, seagrass and coral abundance and condition are good indicators of 
marine health and are essential elements of the marine environment. As well as 
playing a role in the carbon cycle they provide crucial habitats for many fish,
 crustaceans and other species. However, they are under constant transformation
  in response to human activities and global change. 
        """
bulletPoint1 = """
More than 1000 species of algae have been identified in Irish waters, some of 
which are invasive causing economic and environmental impacts.  
        """
bulletPoint2 = """
Seagrass is found close to coasts and is very vulnerable to human actions. 
It is estimated that almost 30% of seagrass meadows globally have died off over
 the last century. Surveys in Ireland since 2006 suggest an increase in the 
 presence of seagrass in most sites monitored. 
        """

bulletPoint3 = """
Deep-water or cold-water corals are found on parts of the continental slope to 
the west of Ireland at water depths ranging between 600 m and 1000 m, and 
worldwide they are found at depths of up to 2000 m.
        """

bulletPoints = [bulletPoint1, bulletPoint2,bulletPoint3]
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
