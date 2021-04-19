import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_3, map_3_1b
import copy

chapter_num = '3.1b'
bannerImgSrc = IMAGES_PATH + \
    'OceanicSections/Sea_Subsurface_Temperature_TomaszSzumski.jpg'
bannerImgCredit = 'Tomasz Szumski'

introText = """
        The temperature of the ocean is influenced by a number of factors, including the amount of heat 
        from the sun transferred through the atmosphere to the water, surface and 
        subsurface circulation and current patterns. Heat uptake by the global ocean accounts for 
        more than 90% of the excess heat trapped in the Earth system in the past few decades. 
        """
bulletPoint1 = """
        Globally, the upper ocean (0-700 m) and intermediate ocean (700-2000 m) have warmed since the 1970s.   
        """
bulletPoint2 = """
        However, observations of the annual water temperature in the Rockall Trough at depths between 1500 m and 2000 m from 1975 to 2018 show no evident trend.   
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Mean Sea Subsurface Temperature' #(1961-2018)
trendChart = figure_3_3()

trendCaption = """
 Annual water temperature at the Rockall Trough at depths between 1500 m and 2000 m on the Extended Ellett Line 
 for the period 1975–2018. Over the time series, there is no significant trend evident.
        """

infrastructureText = """
Measurements of subsurface ocean temperature in Irish waters are made by the Marine Institute at the M6 buoy mooring (red dot, Map 3.1) 
and at the SmartBay Observatory (black dot) in Galway Bay. Since 2008, the Marine Institute has deployed 20 Argo floats in the North Atlantic; 
these underwater autonomous profilers measure temperature and salinity down to a depth of 2000 m.
        """
infrastructureMap = map_3_1b()

infoLinks = [
     {'text': 'Sea Subsurface Temperature ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/subsurface-temperature'},

     {'text': 'Annual ICES Report on Ocean Climate (IROC)',
     'url': 'https://ocean.ices.dk/iroc/#'},

     {'text': 'Marine Institute data portal',
     'url': 'http://data.marine.ie/'},

     {'text': 'Information from the Irish Marine Data Buoy Observation Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/integrated-marine-observations'},

     {'text': 'Information about Euro-Argo',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/oceanography/euro-argo'},

     {'text': 'Information about Extended Ellet Line',
     'url': 'https://mars.noc.ac.uk/projects/extended-ellet-line'},

     {'text': 'Information about NEPHROPS survey ',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/fisheries-ecosystems/nephrops-under-water-tv-surveys'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)


########################################################################################################################
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
