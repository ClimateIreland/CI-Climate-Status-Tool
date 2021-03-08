import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num='2.12'
bannerImgSrc=IMAGES_PATH+'AtmosphericSections/Other_GHG_IMG_3709 Hester Whyte.JPG'
bannerImgCredit='Hester Whyte'

introText="""
In addition to water vapour, carbon dioxide (CO2) and methane (CH4), 
a number of other gases contribute significantly to the enhanced greenhouse effect.  
These include Nitrous oxide (N2O) which has a global warming potential 265 times that of 
CO2 and synthetic gases which are exclusively produced by human activities but have extremely high global warming potentials.
        """
bulletPoint1="""
        N2O concentrations in the atmosphere are now approximately 20% 
        higher compared to the pre-industrial era  
        """
bulletPoint2="""
        Synthetic gasses, which replaced ozone depleting chlorofluorocarbons 
        (CFCs) are increasing steadily in the atmosphere.
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
