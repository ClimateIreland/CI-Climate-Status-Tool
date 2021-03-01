import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import CHAPTERS
from charts import dissolvedOxygenTrend, dissolvedOxygenStationsMap

# get relative data folder
PATH = pathlib.Path(__file__).parent
IMAGES_PATH=PATH.joinpath("../assets/images").resolve()

chapter=3.7
ecvName='Dissolved Oxygen'
bannerImgSrc='assets/images/OceanicSections/Dissolved OxygenTomasz_Szumski.JPG'
bannerImgCredit='Credit: Tomasz_Szumski'
ecvIconSrc='assets/images/icons/oxygen.png'

introText="""
        Oxygen is essential for ocean life. 
        There is an optimum range for dissolved oxygen concentration in oceanic 
        water to avoid stress and potential death to marine organisms. 
        Although low levels of oxygen exist in certain habitats, 
        in general oxygen in subsurface waters is a good indicator of ocean health. 
        """
bulletPoint1="""
        Globally there has been a decrease of oxygen concentrations from 
        the surface to 1000 m depth over the last 60 years.
        """
bulletPoint2="""
        The levels of oxygen seen in McSwyne´s Bay, Co Donegal, in 2005 and 
        2012 are associated with summer phytoplankton blooms which caused 
        major mortalities of marine organisms.
        """

domain='Ocean'
subdomain='Biogeochemistry'
scientificArea='Biosphere'
authors='Walther C.A. Cámaro García, Ned Dwyer, Robert Wilkes, Rob Thomas, Evin McGovern'

trendChartTitle='Dissolved Oxygen Saturation (2002-2019)'
trendChart=dissolvedOxygenTrend()

trendCaption="""
        Above shows the percentage saturation of dissolved oxygen taken at sampling sites 
        in McSwyne’s Bay, Co. Donegal, mainly during summer months, from 2002 to 2019. 
        Measurements were made at water depths ranging from just below the surface to 30 m. 
        In general, levels were close to full saturation over the period of the observations. 
        Super-saturated values (>100%) usually occur in the well-mixed surface layer, 
        while the lower levels of saturation are found in stratified subsurface layers. 
        The maximum and minimum values observed during the 2005 and 2012 summers are linked to 
        phytoplankton blooms present during these periods in the coastal areas. 
        The low dissolved oxygen values following the 2005 intense dinoflagellate bloom resulted in 
        major mortalities of marine organisms in both the water column and near the sea floor. 
        """

infrastructureText="""
        The MI and NUI Galway have undertaken ship-based hydrographic observations including dissolved
        oxygen since 2008 and supported additional initiatives such as GO-SHIP. Data collected from these 
        programmes are reported to the International Council for the Exploration of the Sea (ICES) and 
        other international data centres.

        There is a need to sustain “climate” quality objective seawater 
        dissolved oxygen measurements that meet international standards 
        such as those described in the GO-SHIP hydrography manual.

        """
infrastructureMap=dissolvedOxygenStationsMap()

infoLinks=[{'text':'Oxygen ESSENTIAL CLIMATE VARIABLES (ECV). GCOS FACTSHEETS', 
            'url':'https://gcos.wmo.int/en/essential-climate-variables/oxygen/'},
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
        pb.build_breadcrumb(ecvName,chapter_dict),
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
        pb.build_info(infoLinks,chapter_dict),
                  
        pb.build_nav_carousel(chapter_dict)
        ])
