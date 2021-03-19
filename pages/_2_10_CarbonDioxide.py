import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '2.10'
bannerImgSrc = IMAGES_PATH + \
    'AtmosphericSections/CarbonDioxide_Pixabay.com_traffic-jam-688566.jpg'
bannerImgCredit = 'Pixabay.com'

introText = """
Carbon dioxide (CO2) is the most important greenhouse gas in the atmosphere apart from water vapour. 
Some CO2 is removed by plants, soils and the ocean, the rest remains in the atmosphere for centuries 
and is one of the main drivers of climate change.  Human activities such as fossil fuel combustion, 
cement production, deforestation, vegetation fires and land-use changes all contribute to CO2 emissions. 
        """
bulletPoint1 = """
The annual rate of increase in atmospheric CO2 over the past 60 years is about 
100 times faster than previous natural increases, 
such as those that occurred at the end of the last ice age 11,000-17,000 years ago.
        """
bulletPoint2 = """
Atmospheric CO2 concentrations of 413 ppm at Mace Head in 2018 are estimated to be more than 50% higher than those of the pre-industrial era.
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
