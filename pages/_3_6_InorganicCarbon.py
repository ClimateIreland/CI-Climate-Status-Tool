import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.6'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Inorganic Carbon_Tomas Szumski.jpg'
bannerImgCredit = 'Tomas Szumski'

introText = """
        The ocean absorbs significant quantities of carbon through natural cycles 
        driven by ocean circulation, biogeochemistry and biology.  
        It is estimated that the ocean has absorbed between 20–30% of total anthropogenic CO2 
        emissions since the 1980s thereby reducing atmospheric accumulation and thus partially 
        mitigating global warming. 
        """
bulletPoint1 = """
        Estimates of future carbon dioxide levels indicate that by the end of this 
        century the surface waters of the ocean could be nearly 150% more acidic, 
        a condition not experienced for more than 20 million years.
        """
bulletPoint2 = """
        Measurements of surface waters in the Rockall Trough to the west of Ireland between 
        1991 and 2013 indicate increasing acidity  comparable to the rate of change in other ocean time series.  
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
