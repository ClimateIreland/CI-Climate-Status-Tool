import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '4.10'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Soil Carbon_Teagasc.jpg'
bannerImgCredit = 'Teagasc'

introText = """
Organic carbon in soil is derived from decomposition of plant matter, such as 
leaf litter and woody debris, and is a significant part of the carbon cycle. 
Carbon is incorporated into vegetation through the process of photosynthesis, 
whereby CO\u2082 is sequestered from the atmosphere. The amount of carbon present 
in the soil is determined by geology, soil type, climate and land use.
        """
bulletPoint1 = """
Peat soils dominate the terrestrial carbon budget and store some 1566 million 
tonnes of carbon, representing approximately 64% of the total soil organic 
carbon stock present in Ireland.
        """
bulletPoint2 = """
Soil organic carbon in agricultural lands is highest in the west and around 
the Wicklow mountains in areas with higher precipitation and close to peatlands. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Changes in soil carbon are very slow and therefore difficult to detect and at a
 given site require observations over several decades. In Ireland, a number of 
 initiatives have aimed to produce soil carbon stock maps.  Estimations are 
 based on several properties such as soil type and depth, carbon density, land 
 cover and in particular the soil bulk density. The bulk density reflects the 
 soil’s ability to function for structural support, water and solute movement, 
 and soil aeration. 
The “Soil Geochemical Atlas of Ireland” was an EPA funded project, concluded in
 2007, which had the goal of creating a map with the basic geochemical 
 properties of soils in Ireland, based on data collected between 1995 and 2006.
  Another project “The Soil C – Measuring and Modelling of Soil Carbon Stocks 
  and Stock Changes in Irish Soils” was an EPA funded project, concluded in 
  2009, which measured and modelled the soil carbon stocks and stock changes in
   a number of Irish soils based on numerous samples collected at several 
   increments over a depth of 50 cm. 
The most recent initiative, concluded in 2016, was carried out under the EPA 
and Teagasc funded project “Irish Soil Information System (Irish SIS)”. An 
indicative Soil Organic Carbon (SOC) Map was created for the majority of 
mineral and organo-mineral soils in Ireland, with the exception of peat soils. 
This is because information associated with bulk density data are not recorded 
for these soils. 

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Soil Carbon ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/soil-carbon/'},
    {'text': 'Creamer, R. et al., 2016. Irish Soil Information System: Soil Property Maps. Environmental Protection Agency',
     'url': 'https://www.epa.ie/publications/research/land-use-soils-and-transport/research-204.php'},
    {'text': 'Irish SIS data sources',
     'url': 'http://gis.teagasc.ie/soils/'},
    {'text': 'ay, D. et al., 2007. Soil Geochemical Atlas of Ireland. Teagasc and Environmental Protection Agency',
     'url': 'https://www.teagasc.ie/media/website/publications/2011/Soil_Geochemical_AtlasofIreland.pdf'},

    {'text': 'Soil Geochemical Atlas of Ireland',
     'url': 'http://erc.epa.ie/safer/iso19115/displayISO19115.jsp?isoID=105'},
    {'text': 'Kiely, G. et al., 2010. SoilC – Measurement and Modelling of Soil Carbon Stocks and Stock Changes in Irish Soils. Environmental Protection Agency ',
     'url': 'https://www.epa.ie/publications/research/land-use-soils-and-transport/strive-35.php'},
    {'text': 'SoilC data sources',
             'url': 'http://erc.epa.ie/safer/iso19115/displayISO19115.jsp?isoID=107#files'},
    {'text': 'National Peatlands Strategy',
     'url': 'https://www.npws.ie/peatlands-and-turf-cutting/peatlands-council/national-peatlands-strategy'},
    {'text': 'Orgiazzi, A. et al., 2018. LUCAS Soil, the largest expandable soil dataset for Europe: a review, European Journal of Soil Science 69: 140–153',
     'url': 'https://doi.org/10.1111/ejss.12499'},
]


###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Bulk Density Map of Agricultural Soils'
trendImg1 = IMAGES_PATH+'TerrestrialSections/Figure4.19.png'
trendCaption1 = """
Indicative bulk density map of agricultural soils in Ireland (left: 0–30 cm 
and right: 30-50cm). (Ref: Soil Property Maps, EPA and Teagasc funded project 
“Irish Soil Information System”) 
"""

trendChartTitle2 = 'Carbon Stock Map of Agricultural Soils'
trendImg2 = IMAGES_PATH+'TerrestrialSections/SoilCarbonStockMap.png'
trendCaption2 = """
Indicative soil organic carbon stock map of agricultural soils (0–50 cm). 
(Ref: Soil Property Maps, EPA and Teagasc funded project “Irish Soil 
Information System”) 
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
                dbc.Col(className="col-md-10 offset-md-1 ",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle1),
                            html.Img(
                                className='w-100',
                                src=trendImg1
                            )
                        ]
                        ),

            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[
                                    html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption1]
                            )]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 col-lg-6 offset-lg-3",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle2),
                            html.Img(
                                className='w-100',
                                src=trendImg2
                            )
                        ]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[
                                    html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption2]
                            )]
                        )
            ]
        ),
    ])

custom_infrastructure = dbc.Container(
    className='sr-infrastructure',
    style={'borderColor': chapter_dict['domain-color']},
    id='infrastructure',
    children=[
        html.H3(
            className='sr-section-heading',
            children='Infrastructure',
            style={'color': chapter_dict['domain-color']},
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-12 my-auto",
                        children=[
                            html.P(infrastructureText)]
                        ),
            ])
    ])


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
            custom_trend,
            #     pb.build_trend(trendChartTitle,
            #                    trendChart,
            #                    trendCaption,
            #                    chapter_dict
            #                    ),
            custom_infrastructure,
            #     pb.build_infrastructure(infrastructureText,
            #                             infrastructureMap,
            #                             chapter_dict
            #                             ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
