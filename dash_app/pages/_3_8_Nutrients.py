import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Nutrients_Tomas Szumski_167.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
The major nutrients, such as dissolved inorganic phosphorus, nitrogen and silicon, 
play a key role in ocean life. They are essential for plant growth (e.g. 
phytoplankton, algae) at the base of the food web and when depleted can limit 
growth. In excess, they can cause eutrophication, whereby accelerated algal 
growth can lead to depletion of oxygen and result in severe ecological harm. 
        """
bulletPoint1 = """
Nutrient concentrations in Irish waters are determined by natural dynamics and 
the seasonal variability in the growth of phytoplankton and macroalgae; they 
are also influenced by riverine and atmospheric inputs from human activities – 
for example agricultural application of fertiliser and municipal waste discharges. 
        """
bulletPoint2 = """
Locations with elevated nitrogen concentrations linked to sources of pollution 
are generally found on the south and east coasts of Ireland.
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
