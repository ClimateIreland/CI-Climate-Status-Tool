import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_11, map_2_6
import copy

chapter_num = '2.6'
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
trendChartTitle = html.Span(
        children=[
                'Solar Radiation, R',
                html.Sub('s'),
                ' - Valentia Observatory'
                ])
trendChart = figure_2_11()

trendCaption = """
Annual solar radiation at Valentia Observatory (1964–2019). Units are in 
Gigajoules per metre squared (GJ/m\u00B2) per year.
        """

infrastructureText = """
Solar radiation has been measured by Met Éireann since 1954, when the first 
sensor was placed at Valentia Observatory. Historically, sunshine duration was 
the observed solar variable with continuous records dating back to 1893, but 
more recently there has been a greater demand for solar radiation (incoming 
radiation), also known as global radiation, which represents a more 
comprehensive measurement of solar energy. Solar observations are measured at 
the 25 synoptic weather stations (red and blue) by Met Éireann.  A more 
complete suite of solar measurements is measured by Met Éireann’s AUTOSOL 
infrastructure at a subset of sites (blue). Long term Irish solar measurements 
are routinely submitted to the World Radiation Data Centre.
Measurements linked to the Earth Radiation Budget at the top of the atmosphere 
can only be made from space. NASA and ESA sensors are widely used for the 
measurements of all the radiation fluxes linked to the Earth Radiation Budget. 

        """
infrastructureMap = map_2_6()

infoLinks = [
    {'text': 'Surface Radiation Budget ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-radiation'},
         {'text': 'Earth Radiation Budget ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/earth-radiation'},
         {'text': 'Sunshine and solar radiation from Met Éireann',
     'url': 'https://www.met.ie/climate/what-we-measure/sunshine'},
         {'text': 'Data availability from Met Éireann',
     'url': 'https://www.met.ie/climate/available-data'},
         {'text': 'World Radiation Data Centre',
     'url': 'http://wrdc.mgo.rssi.ru'},
         {'text': 'About EUMETSAT, Europe´s weather satellite programme',
     'url': 'https://www.eumetsat.int/website/home/index.html'},

]



###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

combined_chapter_dict = copy.copy(chapter_dict)
combined_chapter_dict['title'] = 'Surface and Earth Radiation Budget'
combined_chapter_dict['subdomain'] = 'Surface / Upper Atmosphere'
def create_layout(app):
    return html.Div(
        children=[
            pb.build_banner(bannerImgSrc,
                            bannerImgCredit,
                            combined_chapter_dict
                            ),
            pb.build_breadcrumb(combined_chapter_dict),
            pb.build_nav(combined_chapter_dict),
            pb.build_intro(introText,
                           bulletPoints,
                           combined_chapter_dict
                           ),
            pb.build_trend(trendChartTitle,
                           trendChart,
                           trendCaption,
                           combined_chapter_dict
                           ),
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    combined_chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          combined_chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
