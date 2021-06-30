import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '0'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Soil_Moisture_Ned_DwyerP1090366.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Soil moisture comprises only a tiny percentage of the total global water 
budget, but it has a key role in influencing the hydrological cycle and is a 
major driving force in the soil’s ability to act as a carbon sink or source. 
Soil moisture content refers to the amount of water held in the soil and is 
affected by the soil texture, topography, land cover and weather conditions. 
Both local climate and vegetation influence soil moisture through 
evapotranspiration.
        """
bulletPoint1 = """
Soil moisture is a determinant of the type and conditions of vegetation in a 
region, and it is an important measure for agriculture, as it affects the 
length of the grazing season, grass and crop growth rates and nutrient uptake 
and loss.
        """
bulletPoint2 = """
Soil moisture deficits calculated at Dublin airport in June and July 2018 were 
the highest since records began in 1981. 
        """
bulletPoint3 = """
In general, the greatest soil moisture deficits are seen in the east and 
south-east of the country.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
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
