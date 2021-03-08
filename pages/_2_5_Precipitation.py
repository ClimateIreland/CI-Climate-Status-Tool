import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='2.5'
bannerImgSrc=IMAGES_PATH+'AtmosphericSections/Precipitation_Glendalough-Lynn Walsh.JPG'
bannerImgCredit='Lynn Walsh'

introText="""
Rainfall (precipitation) plays a vital role in the water cycle and water balance and is essential for the maintenance of life.   
An understanding of precipitation distribution and trends is essential for assessing potential effects of climate change on 
the supply of water and for supporting both flood and drought mitigation initiatives. 
        """
bulletPoint1="""
Globally there has been a discernible intensification in heavy rainfall events over the second half of the 20th century.
        """
bulletPoint2="""
In Ireland the decade from 2006 to 2015 has been the wettest in the period 1711 to 2016.
        """

bulletPoint3="""
In Ireland the decade from 2006 to 2015 has been the wettest in the period 1711 to 2016.
        """
bulletPoints=[bulletPoint1,bulletPoint2,bulletPoint3]

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
