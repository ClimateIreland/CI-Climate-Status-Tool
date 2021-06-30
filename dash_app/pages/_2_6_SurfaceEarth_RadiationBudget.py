import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Radiation_Ned_Dwyer_P1090408.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Energy reaches the Earth’s surface from the sun directly and diffusely, from 
scattering caused by clouds, aerosols and various gases in the atmosphere. 
Some of this incident energy is reflected and emitted back to space. 
The balance at the top of the atmosphere between the incoming energy from the 
sun and the outgoing reflected energy and thermal energy from the Earth is 
known as the Earth radiation budget. The radiation balance at ground level is 
known as the surface radiation budget and is essential for climate dynamics, 
such as hydrological cycles and crop productivity.

        """
bulletPoint1 = """
A decrease in the annual solar radiation is observed over the period 1964–1984,
 followed by an increasing trend until the late 2000s. Over the last decade a 
 slight decrease is observed. 
        """
bulletPoint2 = """
Regular analysis of national trends and further measurements of the net surface
 radiation balance needs to be carried out, given its role in plant growth, the
  hydrological cycle and the larger climate system.
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
