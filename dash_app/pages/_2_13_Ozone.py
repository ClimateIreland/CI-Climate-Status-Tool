import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Ozone_MetEireann.jpg'
bannerImgCredit = 'Met Éireann'

introText = """
Ozone (O\u2083) is another potent greenhouse gas in terms of radiative forcing.
 The influence of O3 on climate is complex, with different impacts in the upper
  and lower atmosphere. It also has multiple potential environmental and health
   impacts. In the upper atmosphere (stratosphere) it prevents harmful 
   ultraviolet radiation from reaching the Earth’s surface. In the lower 
   atmosphere (troposphere) it is a pollutant, harmful to all living things. 
        """
bulletPoint1 = """
The implementation of the internationally agreed Montreal Protocol (1987) has 
been effective in reducing the production of O\u2083-depleting substances and 
gradually restoring stratospheric O3 concentrations.
        """
bulletPoint2 = """
At Mace Head average annual near-ground O\u2083 amounts increased over the 
period 1987–1997, followed by a step change during 1998/1999 and relatively 
constant levels since then.
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
