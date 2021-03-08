import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='3.1a'
bannerImgSrc=IMAGES_PATH+'OceanicSections/Sea_Temperature_Annual Ocean Climate Survey 2019_Photo by Tomasz Szumski_158.JPG'
bannerImgCredit='Tomasz Szumski'

introText="""
        The temperature of the ocean is influenced by a number of factors, including the amount of heat 
        from the sun transferred through the atmosphere to the water, surface and 
        subsurface circulation and current patterns. Heat uptake by the global ocean accounts for 
        more than 90% of the excess heat trapped in the Earth system in the past few decades. 
        """
bulletPoint1="""
        The global ocean surface temperatures has increased by  approximately 0.7°C since the 1850s, 
        with the rate of warming estimated to have doubled since the 1990s.  
        """
bulletPoint2="""
        The sea surface temperature record at Malin Head in the period 2009 to 2018  was on average 0.47°C above the 1981-2010 mean.
        """
bulletPoint3="""
        Observations of the annual water temperature in the Rockall Trough at depths between 1500 m and 2000m from 1975 to 2018 show no evident trend.   
        """
bulletPoints=[bulletPoint1, bulletPoint2, bulletPoint3]
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
