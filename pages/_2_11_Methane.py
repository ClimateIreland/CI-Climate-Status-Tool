import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_20

chapter_num = '2.11'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Methane_Ned_Dwyer_P1000356.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Methane (CH\u2084) is the third most important greenhouse gas in the atmosphere after CO\u2082 and water vapour.   
Although estimated to have a global warming potential evaluated over 100 years of approximately 28 times that of CO\u2082, methane does not persist for much more than a decade in the atmosphere.  
Approximately 60% of methane emissions are due to human activities, the remaining 40% are due to natural processes. 
        """
bulletPoint1 = """
In Ireland, agriculture contributes almost 93% of total CH\u2084 emissions, with the remainder due to waste management (5%) and the energy sectors. 
        """
bulletPoint2 = """
Following a stable period in the late 1990s and early 2000s there has been a 4% increase in CH\u2084 concentrations since 2007 observed at Mace Head. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Methane (CH\u2084) Concentration at Mace Head (1987-2018)'
trendChart = figure_2_20()

trendCaption = """
        Monthly mean methane concentration observed at Mace Head Research Station (1987–2018).     
        """

infrastructureText = """

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Carbon Dioxide, Methane & Other Greenhouse Gases ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ghg/'},
     {'text': 'Nisbet, E.G., Dlugokencky, E.J., Manning, M.R., et al., (2016) Rising atmospheric methane: 2007–2014 growth and isotopic shift, Global Biogeochemical Cycles, Vol. 30, 9, pp. 1356-1370',
     'url': 'https://doi.org/10.1002/2016GB005406'},
     {'text': 'Jackson, R.B., Saunois, M., Bousquet, P., et al, (2020), Increasing anthropogenic methane emissions arise equally from agricultural and fossil fuel sources,  Environ. Res. Lett. 15 071002',
     'url': 'https://doi.org/10.1088/1748-9326/ab9ed2'},
     {'text': 'Information on the Mace Head Facility',
     'url': 'http://www.macehead.org/'},
     {'text': 'Ireland´s GHG emissions by sector and gas',
     'url': 'http://www.epa.ie/ghg/'},
     {'text': 'ESA’s Greenhouse Gases Climate Change Initiative',
     'url': 'http://cci.esa.int/ghg'},
     {'text': 'ESA Sentinel 5P Mission',
     'url': 'https://sentinel.esa.int/web/sentinel/missions/sentinel-5p'},
     {'text': 'Greenhouse Gas Concentration in the European State of the Climate Bulletin – 2019',
     'url': 'https://climate.copernicus.eu/ESOTC/2019/greenhouse-gas-concentrations'},
     {'text': 'Integrated Carbon Observation System (ICOS)',
     'url': '(https://www.icos-cp.eu/'}
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
