import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_3_15, map_3_6

chapter_num = '3.7'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Dissolved OxygenTomasz_Szumski.JPG'
bannerImgCredit = 'Tomasz_Szumski'

introText = """
        Oxygen is essential for ocean life. 
        There is an optimum range for dissolved oxygen concentration in oceanic 
        water to avoid stress and potential death to marine organisms. 
        Although low levels of oxygen exist in certain habitats, 
        in general oxygen in subsurface waters is a good indicator of ocean health. 
        """
bulletPoint1 = """
        Globally there has been a decrease of oxygen concentrations from 
        the surface to 1000 m depth over the last 60 years.
        """
bulletPoint2 = """
        The levels of oxygen seen in McSwyne´s Bay, Co Donegal, in 2005 and 
        2012 are associated with summer phytoplankton blooms which caused 
        major mortalities of marine organisms.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
# domain='Ocean'
# subdomain='Biogeochemistry'
# scientificArea='Biosphere'
# authors='Walther C.A. Cámaro García, Ned Dwyer, Robert Wilkes, Rob Thomas, Evin McGovern'

trendChartTitle = 'Dissolved Oxygen Saturation (2002-2019)'
trendChart = figure_3_15()

trendCaption = """
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

infrastructureText = """
        The MI and NUI Galway have undertaken ship-based hydrographic observations including dissolved
        oxygen since 2008 and supported additional initiatives such as GO-SHIP. Data collected from these 
        programmes are reported to the International Council for the Exploration of the Sea (ICES) and 
        other international data centres.

        There is a need to sustain “climate” quality objective seawater 
        dissolved oxygen measurements that meet international standards 
        such as those described in the GO-SHIP hydrography manual.

        """
infrastructureMap = map_3_6()

infoLinks = [
    {'text': 'Oxygen ESSENTIAL CLIMATE VARIABLES (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/oxygen/'},
    {'text': 'Silke, J., O\'Beirn, F. & Cronin, M. (2005), "Karenia mikimotoi: An Exceptional Dinoflagellate Bloom in Western Irish Waters, Summer 2005", Marine Environment and Health Series No. 21, Marine Institute 2005 ',
     'url': 'https://oar.marine.ie/handle/10793/240'},
    {'text': 'Linden, O., (2019), Evidence for ocean deoxygenation and its patterns, in: Ocean Deoxygenation: Everyone´s Problem, Laffoley, D. & Baxter, J.M. (eds), IUCN, Geneva.',
     'url': 'https://doi.org/10.2305/IUCN.CH.2019.13.en'},
    {'text': 'Information about ICES',
     'url': 'https://www.ices.dk/'},
    {'text': 'The GO-SHIP programme',
     'url': 'https://www.go-ship.org/About.html'},
    {'text': 'The Marine Institute operated Research Vessels',
     'url': 'https://www.marine.ie/Home/site-area/infrastructure-facilities/research-vessels/research-vessels'},
    {'text': 'Water Quality in Ireland under the Water Framework Directive',
     'url': 'http://www.epa.ie/pubs/reports/water/waterqua/waterqualityinireland2013-2018.html'},
]


################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

################################################################################

trendCaption2 = """
Above shows a deep-water dissolved oxygen section as measured during the annual
 Rockall Ocean Climate Survey in winter 20131. The lowest values are observed in the subsurface waters at 
 approximately 500m depth due to respiration associated with decomposition of organic matter. 
"""
custom_trend = dbc.Container(
    className='sr-trends',
    style={'borderColor': chapter_dict['domain-color']},
    id='trends',
    children=[
        html.H3(
            className='sr-section-heading',
            style={'color': chapter_dict['domain-color']},
            children='Trends',
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle),
                            dcc.Graph(
                                figure=trendChart,
                                config={'displayModeBar': False})]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=trendCaption
                            )]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.Img(
                                # src=DATA_PATH+'Oceanic_Domain/3.7Oxygen/Figure3.16/Figure3.16_OxygenConcentrationSectionRockallTrough.png'
                                className='w-100',
                                src=IMAGES_PATH+'Figure3.16_OxygenConcentrationSectionRockallTrough.png'
                            )]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=trendCaption2
                            )]
                        )
            ]
        ),
    ])


##############################################################################

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
            # pb.build_trend(trendChartTitle,
            #                trendChart,
            #                trendCaption,
            #                chapter_dict
            #                ),
            custom_trend,
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks, chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
