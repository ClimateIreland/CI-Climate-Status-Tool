import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_3, map_4_3

chapter_num = '4.3'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Lakes_Lough Derg - Bronislav kordovanik.jpg'
bannerImgCredit = 'Bronislav Kordovanik'

introText = """
        Lakes are linked to climate change effects due to evaporation of water. 
        Information on variations in the level, area and temperature of lakes 
        is essential to understand the dynamics of these water bodies, which 
        are directly affected by regional climate. Lakes provide a range of 
        services such as drinking water and supplies for industry and agriculture, 
        recreational opportunities and ecosystem maintenance. 
        """
bulletPoint1 = """
        The most significant threats to Ireland´s more than 12,000 lakes and 
        their biology is changes in water quality caused by land use change 
        in their catchments and water temperature changes in the lakes themselves.
        """
bulletPoint2 = """
        Levels in Lough Oughter, Co. Cavan show seasonal variation, but no long-term 
        trend in the 40-year data set is apparent.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Monthly Mean Lake Level - Lough Oughter'
trendChart = figure_4_3()

trendCaption = """
        Monthly mean levels on Lake Oughter, Co. Cavan (1977–2018). 
        Levels show seasonal variation, with minimum values during the summer and maximum 
        values during the winter, but no long-term trend in the data is apparent.
        """

infrastructureText = """
Lake levels are currently measured at 74 locations by the EPA, the Office of Public Works and 
the Electricity Supply Board. The lake monitoring programme is undertaken to comply with the 
Water Framework Directive (WFD). In this programme, 226 lakes are examined for a broader 
range of biological and chemical parameters Lake water quality measures have been published regularly since 1987 by the EPA.  
        """
infrastructureMap = map_4_3()

infoLinks = [
    {'text': 'Lakes ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/lakes/'},
         {'text': 'The EPA’S website on lake monitoring',
     'url': 'https://www.epa.ie/our-services/monitoring--assessment/freshwater--marine/lakes/'},
         {'text': 'Data on lake locations and water quality from the EPA',
     'url': 'http://gis.epa.ie/GetData/Download'},
         {'text': 'Lake level data from the EPA',
     'url': 'https://www.epa.ie/hydronet/#Water%20Levels'},
         {'text': 'Online hydrometric data from the Office of Public Works hydrometric network.',
     'url': 'https://waterlevel.ie/'},
         {'text': 'ESA´s Lakes Climate Change Initiative',
     'url': 'http://cci.esa.int/lakes'}

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
