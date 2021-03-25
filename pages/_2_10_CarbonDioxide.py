import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_18

chapter_num = '2.10'
bannerImgSrc = IMAGES_PATH + \
    'AtmosphericSections/CarbonDioxide_Pixabay.com_traffic-jam-688566.jpg'
bannerImgCredit = 'Pixabay.com'

introText = """
Carbon dioxide (CO\u2082) is the most important greenhouse gas in the atmosphere apart from water vapour. 
Some CO\u2082 is removed by plants, soils and the ocean, the rest remains in the atmosphere for centuries 
and is one of the main drivers of climate change.  Human activities such as fossil fuel combustion, 
cement production, deforestation, vegetation fires and land-use changes all contribute to CO\u2082 emissions. 
        """
bulletPoint1 = """
The annual rate of increase in atmospheric CO\u2082 over the past 60 years is about 
100 times faster than previous natural increases, 
such as those that occurred at the end of the last ice age 11,000-17,000 years ago.
        """
bulletPoint2 = """
Atmospheric CO\u2082 concentrations of 413 ppm at Mace Head in 2018 are estimated to be more than 50% higher than those of the pre-industrial era. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]

trendChartTitle = 'Carbon Dioxide (CO\u2082) Concentration (1958-2018)'
trendChart = figure_2_18()

trendCaption = """
        Monthly mean concentration of carbon dioxide at Mauna Loa, Hawaii (1958–2012) and Mace Head Research Station, Ireland (1992–2018). 
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
