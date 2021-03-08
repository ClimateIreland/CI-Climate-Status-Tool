import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='4.11'
bannerImgSrc=IMAGES_PATH+'TerrestrialSections/Fires_CiaranNugent.jpg'
bannerImgCredit='Ciaran Nugent'

introText="""
        Land cover - the observed (bio)-physical cover on the Earth’s surface, 
        including grassland, forest, built environment, etc. 
        – plays a key role in climate dynamics such as water and energy exchanges 
        between the ground and the atmosphere, and contributes to the capture 
        and release of greenhouse gases and aerosols.  
        """
bulletPoint1="""
        Peatlands represent almost 14% of Irish land cover and are an 
        essential feature in the regulation of the climate by removing carbon
        """
bulletPoint2="""
        Land cover observations since 1990 show increases in the area covered 
        by artificial surfaces and forests and a decrease in wetland areas which include peatlands.
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
