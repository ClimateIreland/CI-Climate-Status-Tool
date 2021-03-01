import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import CHAPTERS
from charts import surfaceAirTempChart, surfaceAirTempStationsMap

# get relative data folder
PATH = pathlib.Path(__file__).parent
IMAGES_PATH=PATH.joinpath("../assets/images").resolve()

chapter=2.1
ecvName='Surface Air Temperature'
bannerImgSrc='assets/images/AtmosphericSections/AirTemp_MetEireann.jpg'
bannerImgCredit='Credit: Met Eirean'
ecvIconSrc='assets/images/icons/surface-temperature.png'

introText="""
        introText
        """
bulletPoint1="""
        In Ireland the annual average surface air temperature has increased by 
        approximately 0.9°C over the last 120 years
        """
bulletPoint2="""
        The number of warm spell days across Ireland has slightly 
        increased over the last 60 years.
        """

domain='Atmosphere'
subdomain='Surface'
scientificArea='Energy and Temperature'
authors='authors'

trendChartTitle='chart title'
trendChart=surfaceAirTempChart()

trendCaption="""
           Text
        """

infrastructureText="""
        Text
        """
infrastructureMap=surfaceAirTempStationsMap()

infoLinks=[{'text':'text', 
            'url':'https://gcos.wmo.int/en/essential-climate-variables/surface-temperature/'},

            ]



########################################################################################################################
chapter_dict=next((item for item in CHAPTERS if item['chapter']==chapter),None)

def create_layout(app):
      return html.Div(
              children=[
        pb.build_banner(ecvName,
                        bannerImgSrc,
                        bannerImgCredit,
                        chapter_dict
                        ),
        pb.build_breadcrumb(ecvName,
        chapter_dict),
        pb.build_nav(chapter_dict),
        pb.build_intro(ecvName,
                       introText,
                       bulletPoint1,
                       bulletPoint2,
                       ecvIconSrc,
                       subdomain,
                       scientificArea,
                       authors,
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
