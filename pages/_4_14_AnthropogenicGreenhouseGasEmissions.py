import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_27

chapter_num = '4.14'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/GHG_EMissions_Metro Centric.jpg'
bannerImgCredit = 'Metro Centric'

introText = """
        Greenhouse gas emissions including carbon dioxide (CO2), methane (CH4), 
        and nitrous oxide (N2O) from human (anthropogenic) activities such as 
        fossil fuel use, industry, agriculture and the waste sector continue to increase globally.  
        These gases reside in the atmosphere for a period from decades to thousands of years 
        and the increase in their concentrations is a cause of increase in surface temperature and climate change.       
        """
bulletPoint1 = """
        In 2018 in Ireland emissions from fossil fuel energy use were 18% higher 
        than in 1990 with emissions from agriculture having increased 2%.  
        Combined these represent over 87% of total emissions.
        """
bulletPoint2 = """
        Nitrous oxide emissions decreased by 10% over the period, mainly because of 
        reductions of synthetic fertiliser and animal manure use in agriculture.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'National Greenhouse Gas Emissions 1990-2018'
trendChart = figure_4_27()

trendCaption = """
National total Greenhouse Gas emissions by IPCC sectors 1990 – 2018. Ref: Ireland’s National Inventory Report 2020. 
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
