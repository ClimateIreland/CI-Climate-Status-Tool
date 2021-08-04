import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_2, map_4_2

chapter_num = '4.2'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Groundwater_Ned_Dwyer_P1090393.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Groundwater is located beneath the ground surface in pore spaces and fractures 
of geological formations. It is estimated that almost 30% of the world’s 
fresh water is stored as groundwater. Globally, it is a major source of 
drinking water and is also widely used in agriculture and industry. 
Groundwater volumes and levels are influenced by not only rainfall and dry 
periods but mainly human use.
        """
bulletPoint1 = """
In Ireland about 18% of drinking water is from groundwater sources. 
        """
bulletPoint2 = """
Abstraction, especially in the world’s arid and semi-arid zones, is leading to 
rapid rates of groundwater depletion.  
        """
bulletPoint3 = """
Regular analysis of groundwater levels in Ireland is carried out but not 
primarily for identifying climate-driven changes.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
trendChartTitle = 'Daily Groundwater Levels - Knocktopher'
trendChart = figure_4_2()

trendCaption = """
Daily mean groundwater level (m) at a well in Knocktopher, Co. Kilkenny 
(1980–2018). Levels change on a seasonal basis, with a minimum during the 
summer months and a maximum during winter, when groundwater recharge occurs.
        """

infrastructureText = """
Groundwater level data have been collected in Ireland since the late 1960s. 
In the 1990s, the EPA took responsibility for its monitoring and currently 
there are 387 in situ stations (green dots) where groundwater levels are 
monitored.  
 Information regarding levels for 126 of these stations is available to 
 download through the EPA web portal ´hydronet´. In addition, water quality 
 monitoring is carried out at a number of the stations taking measurements of 
 several chemical parameters such as oxygen content, conductivity, nitrates 
 and ammonium.
Satellites which form part of the collaborative US and German Gravity 
Recovery and Climate Experiment (GRACE) are being used internationally for 
the monitoring of groundwater over large areas. Large pockets of water exert a 
greater gravitational pull on the satellites than areas without water. 
        """
infrastructureMap = map_4_2()

infoLinks = [
    {'text': 'Groundwater Essential Climate Variable (ECV) Factsheet ',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/groundwater/'},
     {'text': 'The EPA website on groundwater monitoring',
     'url': 'https://www.epa.ie/our-services/monitoring--assessment/freshwater--marine/groundwater/'},
     {'text': 'The EPA Geo Portal data source on groundwater ',
     'url': 'http://gis.epa.ie/GetData/Download'},
     {'text': 'The EPA HydroNet portal – groundwater level data',
     'url': 'https://www.epa.ie/hydronet/#Water%20Levels'},
     {'text': 'About the GRACE mission',
     'url': 'https://grace.jpl.nasa.gov/applications/groundwater/'},
     {'text': 'Groundwater information from the Geological Survey of Ireland',
     'url': 'https://www.gsi.ie/en-ie/data-and-maps/Pages/Groundwater.aspx'},

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
