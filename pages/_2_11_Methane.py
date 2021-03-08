import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='2.11'
bannerImgSrc=IMAGES_PATH+'AtmosphericSections/Methane_Ned_Dwyer_P1000356.JPG'
bannerImgCredit='Ned Dwyer'

introText="""
Methane (CH4) is the third most important greenhouse gas in the atmosphere after CO2 and water vapour.   
Although estimated to have a global warming potential evaluated over 100 years of approximately 28 times that of CO2, methane does not persist for much more than a decade in the atmosphere.  
Approximately 60% of methane emissions are due to human activities, the remaining 40% are due to natural processes. 
        """
bulletPoint1="""
In Ireland, agriculture contributes almost 93% of total CH4 emissions, with the remainder due to waste management (5%) and the energy sectors. 
        """
bulletPoint2="""
Following a stable period in the late 1990s and early 2000s there has been a 4% increase in CH4 concentrations since 2007 observed at Mace Head. 
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
