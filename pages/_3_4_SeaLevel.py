import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='3.4'
bannerImgSrc=IMAGES_PATH+'OceanicSections/Sea_Level_Aldert Otter.jpg'
bannerImgCredit='Aldert Otter'

introText="""
        Sea Level is among the primary indicators of global climate change. 
        Sea level continues to rise because increasing global temperatures cause 
        thermal expansion of the oceans as well as increasing freshwater input due 
        to melting land ice sources (e.g. glaciers and ice sheets, permafrost). 
        """
bulletPoint1="""
        Estimates show that globally, average sea level has risen approximately 160 mm 
        since 1902, at a rate of approximately 1.4 mm per year. 
        """
bulletPoint2="""
        Satellite observations indicate that the sea level around Ireland has 
        risen by approximately 2-3mm/year since the early 1990s.
        """
bulletPoints=[bulletPoint1,bulletPoint2]
trendChartTitle=''
trendChart=empty_chart()

trendCaption="""

        """

infrastructureText="""

        """
infrastructureMap=empty_chart()

infoLinks=[
        {'text':'', 
        'url':''},

            ]




########################################################################################################################
chapter_dict=next((item for item in CHAPTERS if item['chapter-num']==chapter_num),None)

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
