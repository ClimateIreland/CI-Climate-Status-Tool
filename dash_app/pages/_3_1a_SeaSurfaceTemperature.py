import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_1, map_3_1a
import copy

chapter_num = '3.1a'
bannerImgSrc = IMAGES_PATH + \
    'OceanicSections/Sea_Temperature_Annual Ocean Climate Survey 2019_Photo by Tomasz Szumski_158.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
        The temperature of the ocean is influenced by a number of factors, including the amount of heat 
        from the sun transferred through the atmosphere to the water, surface and 
        subsurface circulation and current patterns. Heat uptake by the global ocean accounts for 
        more than 90% of the excess heat trapped in the Earth system in the past few decades. 
        """
bulletPoint1 = """
        The global ocean surface temperature has increased by  approximately 0.7°C since the 1850s, 
        with the rate of warming estimated to have doubled since the 1990s.  
        """
bulletPoint2 = """
        The sea surface temperature record at Malin Head in the period 2009 to 2018  was on average 0.47°C above the 1981-2010 mean.
        """

bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Mean Sea Surface Temperature' #(1961-2018)
trendChart = figure_3_1()

trendCaption = """
 Annual mean observed sea surface temperature (SST) at Malin Head  (1961–2018) (right-hand axis). 
 The left-hand axis indicates anomalies (the difference between the mean annual temperature and the 1981–2010 reference mean value). 
 A trend towards progressive warming can be seen from the mid-1990s to the late 2000s, followed by cooler conditions for a 
 short period and a return to warmer conditions in recent years. Furthermore, all the values observed since the early 2000s 
 are above the 1981–2010 mean.
        """

infrastructureText = """
Sea surface temperature (SST) measurements are made by the Irish Marine Data Buoy Observation Network (orange), 
at the Malin Head Atmospheric Research Station, Co. Donegal (red), at the Ballycotton tide gauge station, Co. Cork (purple), 
and at wave buoys (yellow). A set of coastal temperature sensors (blue) installed predominately at aquaculture sites by 
the Marine Institute measure temperature but are not accurate enough for climate studies.
        """
infrastructureMap = map_3_1a()

infoLinks = [
    {'text': 'Sea Surface Temperature ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/sst'},
     
     {'text': 'Cannaby, H. and Hüsrevoğlu, Y.S. (2009) The Influence of low-frequency variability and long-term trends in Irish SST records, ICES Journal of Marine Science, Vol. 66, No. 7, pp. 1480–9',
     'url': 'https://academic.oup.com/icesjms/article/66/7/1480/657991'},

     {'text': 'Tinker, J., Howes, E., Wakelin, S., et al. (2020) The impacts of climate change on temperature (air and sea), relevant to the coastal and marine environment around the UK. MCCIP Science Review 2020, Marine Climate Change Impacts Partnership, pp 1–30',
     'url': 'http://www.mccip.org.uk/media/2003/01_temperature_2020.pdf'},

     {'text': 'Annual ICES Report on Ocean Climate (IROC)',
     'url': 'https://ocean.ices.dk/iroc/#'},

     {'text': 'Marine Institute data portal',
     'url': 'http://data.marine.ie/'},

     {'text': 'Information from the Irish Marine Data Buoy Observation Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/integrated-marine-observations'},
     
     {'text': 'Copernicus Marine Environment Monitoring Service OCEAN PRODUCTS',
     'url': 'http://marine.copernicus.eu/services-portfolio/access-to-products/'},

     {'text': 'NOAA National Centers for Environmental information, Climate at a Glance: Global Time Series',
     'url': 'https://www.ncdc.noaa.gov/cag/'},
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
