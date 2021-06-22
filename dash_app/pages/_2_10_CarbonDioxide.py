import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_18, map_2_10

chapter_num = '2.10'
bannerImgSrc = IMAGES_PATH + \
    'AtmosphericSections/CarbonDioxide_Pixabay.com_traffic-jam-688566.jpg'
bannerImgCredit = 'Pixabay.com'

introText = """
Carbon dioxide (CO\u2082) is the most important greenhouse gas in the atmosphere apart from water vapour. 
Some CO\u2082 is removed by plants, soils and the ocean, the rest remains in the atmosphere for centuries 
and is one of the main drivers of climate change.  Human activities such as fossil fuel combustion, 
cement production, deforestation, vegetation fires and land-use changes all contribute to CO\u2082 emissions. 
        """
bulletPoint1 = """
The annual rate of increase in atmospheric CO\u2082 over the past 60 years is about 
100 times faster than previous natural increases, 
such as those that occurred at the end of the last ice age 11,000-17,000 years ago.
        """
bulletPoint2 = """
Atmospheric CO\u2082 concentrations of 413 ppm at Mace Head in 2018 are estimated to be more than 50% higher than those of the pre-industrial era. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]

trendChartTitle = 'Carbon Dioxide (CO\u2082) Concentration' #(1958-2018)
trendChart = figure_2_18()

trendCaption = """
Monthly mean concentration of CO\u2082 at Mauna Loa Observatory, Hawaii (1958–2018), and Mace Head Atmospheric Research Station, 
Ireland (1992–2018). The signal observed at Mace Head is more variable because of its 
proximity to Europe and the influence of North America, where the uptake of CO\u2082 
by growing vegetation and its subsequent release when the vegetation decays causes seasonal fluctuations. 
In addition, the seasonal cycle of the phytoplankton bloom in the North Atlantic affects the levels.  
        """

infrastructureText = """
Mace Head Atmospheric Research Station, Carna, Co. Galway (red), has been conducting CO\u2082 observations since 1992. 
CO\u2082 concentrations are also measured at Carnsore Point, Co. Wexford, and Malin Head, Co. Donegal (green), since 2009. 
Measurements at Valentia Observatory, Co. Kerry (blue), started in 2019. The site at Mace Head is of global importance, 
as the measurements are representative of the background concentration of atmospheric CO\u2082 in the North-east Atlantic region.
        """
infrastructureMap = map_2_10()

infoLinks = [
    {'text': 'Carbon Dioxide, Methane & Other Greenhouse Gases ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ghg/'},
     {'text': 'Information on the Mace Head Facility',
     'url': 'http://www.macehead.org/'},
     {'text': 'Ireland´s GHG emissions by sector and gas',
     'url': 'http://www.epa.ie/ghg/'},
     {'text': 'ESA’s Greenhouse Gases Climate Change Initiative',
     'url': 'http://cci.esa.int/ghg'},
     {'text': 'NASA’s Orbiting Carbon Observatory-2 mission information',
     'url': 'https://www.nasa.gov/mission_pages/oco2/index.html'},
     {'text': 'Greenhouse Gas Concentration in the European State of the Climate Bulletin – 2019',
     'url': 'https://climate.copernicus.eu/ESOTC/2019/greenhouse-gas-concentrations'},
     {'text': 'Integrated Carbon Observation System (ICOS) information',
     'url': 'https://www.icos-cp.eu/'},
     {'text': 'Global Carbon Budget 2019, Pierre Friedlingstein et al., Earth Syst. Sci. Data, 11, 1783–1838, 2019',
     'url': 'https://doi.org/10.5194/essd-11-1783-2019'}
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
