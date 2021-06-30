import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Biomass-Mihaly Csernus.jpg'
bannerImgCredit = 'Mihaly Csernus'

introText = """
Biomass is any organic or biological material that comes from plants or 
animals. Above-ground biomass includes all biomass stored above the soil in 
both woody and herbaceous living vegetation and is a key parameter for 
understanding the evolution of and changes in the climate system. The process 
of photosynthesis stores carbon in vegetation biomass in a similar amount to 
that stored in the atmosphere and is one of the most visible carbon pools. 
        """
bulletPoint1 = """
The growing stock volume of trees has increased by 38% in Ireland in the period
 between 2006 and 2017.
        """
bulletPoint2 = """
Just under 50% of the trees grown in Ireland are in private ownership and this 
is where the biggest increase in tree volume has occurred thanks to state 
grant aid.
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


###############################################################################
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
