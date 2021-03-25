import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart,figure_3_8

chapter_num = '3.4'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Sea_Level_Aldert Otter.jpg'
bannerImgCredit = 'Aldert Otter'

introText = """
        Sea Level is among the primary indicators of global climate change. 
        Sea level continues to rise because increasing global temperatures cause 
        thermal expansion of the oceans as well as increasing freshwater input due 
        to melting land ice sources (e.g. glaciers and ice sheets, permafrost). 
        """
bulletPoint1 = """
        Estimates show that globally, average sea level has risen approximately 160 mm 
        since 1902, at a rate of approximately 1.4 mm per year. 
        """
bulletPoint2 = """
        Satellite observations indicate that the sea level around Ireland has 
        risen by approximately 2-3mm/year since the early 1990s.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Mean Sea Level (1938-2016) - Dublin Port'
trendChart = figure_3_8()

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Sea level ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/sea-level/'},

     {'text': 'Nejad, A.S., Parnell, A., Greene, A., et al. (2020, May 27) Recent Rapid Sea Level Rise in Dublin Bay Based on Tide Gauge Analysis',
     'url': 'https://doi.org/10.31223/osf.io/z9hk2'},

     {'text': 'Dataset from the Irish National Tide Network project portal',
     'url': 'http://www.Irishtides.ie'},

     {'text': 'Hydrometric data from the Office of Public Works',
     'url': 'https://waterlevel.ie/group/16/'},

     {'text': 'Dataset from the GLOSS sea level data centres',
     'url': 'https://www.gloss-sealevel.org/data'},

     {'text': 'Tide gauge data from around the world',
     'url': 'https://www.psmsl.org/data/'},

     {'text': 'Information on sea level retrieval from altimeters for the Copernicus Programme',
     'url': 'https://duacs.cls.fr/'},

     {'text': 'Sea Level. European State of the Climate 2018',
     'url': 'https://climate.copernicus.eu/sea-level'},

     {'text': 'Sea Level Global and Regional interactive products based on satellite information',
     'url': 'https://www.aviso.altimetry.fr/?id=1599'},


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
