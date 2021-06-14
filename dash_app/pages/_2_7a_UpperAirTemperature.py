import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_13_a, map_2_7

chapter_num = '2.7a'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Upper Air_Met_Eireann_Fig14.jpg'
bannerImgCredit = 'Met Eireann'

introText = """
        Knowledge of the vertical profiles of temperature and wind in the atmosphere 
        is vital for a better understanding of the weather and climate system. 
        Upper air temperature plays a key role in the energy budget, being linked to 
        the energy transmitted from the atmosphere to space.
        """
bulletPoint1 = """
        Globally, cooling of the upper atmosphere (stratosphere) and warming of the lower atmosphere 
        (troposphere) has been observed since the mid-20th century, consistent with the impact of 
        increased GHG concentrations estimated through climate model simulations.
        """
bulletPoint2 = """
        Measurements at Valentia Observatory show a slight decrease in upper air temperature 
        in the period 1980– 2015, in line with patterns observed globally.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Upper Air Temperature - Valentia, Co.Kerry'
trendChart = figure_2_13_a()

trendCaption = """
        Example of annual mean temperature at Valentia Observatory from one level in the atmosphere (1980–2018).
        """

infrastructureText = """
        Upper-air measurements have been taken by Met Éireann at Valentia Observatory, Co. Kerry 
        since 1917 as a manual process and since 1943 by means of a radiosonde – a helium-filled 
        balloon with instruments attached. 
        The balloon is released into the atmosphere; as it ascends, readings are transmitted back 
        to the surface station. 
        As the balloon rises, it expands until it eventually bursts. The instruments measure pressure, 
        wind speed and direction, humidity and temperatures twice a day. The measurements are taken 
        every 2 seconds as the balloon travels up through the atmosphere. This enables the production 
        of a tephigram which is a ‘snapshot’ of the vertical structure of the atmosphere. 
        Since the late 1970s, globally upper air temperature measurements have been made 
        based on satellite-borne microwave sounders. Changes in sensor technology have made it difficult 
        to integrate and compare the temperature measurements over time. Consequently, 
        climate quality data sets can be extracted only following a careful intercalibration 
        process between the data extracted from different sensors.
        """
infrastructureMap = map_2_7()

infoLinks = [
    {'text': 'Upper Air Temperature ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/upper-temperature'},
         {'text': 'Radiosonde  measurements at Valentia Observatory',
     'url': 'https://www.met.ie/climate/what-we-measure/upper-air'},
         {'text': 'Data availability from Met Éireann',
     'url': 'https://www.met.ie/climate/available-data'},

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
