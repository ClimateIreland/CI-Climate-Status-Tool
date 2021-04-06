import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.6'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Inorganic Carbon_Tomas Szumski.jpg'
bannerImgCredit = 'Tomas Szumski'

introText = """
        The ocean absorbs significant quantities of carbon through natural cycles 
        driven by ocean circulation, biogeochemistry and biology.  
        It is estimated that the ocean has absorbed between 20–30% of total anthropogenic CO\u2082 
        emissions since the 1980s thereby reducing atmospheric accumulation and thus partially 
        mitigating global warming. 
        """
bulletPoint1 = """
        Estimates of future carbon dioxide levels indicate that by the end of this 
        century the surface waters of the ocean could be nearly 150% more acidic, 
        a condition not experienced for more than 20 million years.
        """
bulletPoint2 = """
        Measurements of surface waters in the Rockall Trough to the west of Ireland between 
        1991 and 2013 indicate increasing acidity  comparable to the rate of change in other ocean time series.  
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Inorganic Carbon ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/inorganic-carbon/'},

     {'text': 'Ocean Acidification Observing in Coastal, Shelf and Ocean Waters around Ireland, (2019) E. McGovern, T. McGrath, M. Cronin,  G. O’Donnell, B. Ward, C. Cusack, R. Cave, Poster at Conference: 4th Global Ocean Acidification Observing Network (GOA-ON) International Workshop, Hangzhou',
     'url': 'https://www.researchgate.net/publication/332950133_Ocean_Acidification_Observing_in_Coastal_Shelf_and_Ocean_Waters_around_Ireland'},

     {'text': 'Information about ICES',
     'url': 'https://www.ices.dk/'},

     {'text': 'Surface Ocean CO\u2082 Atlas',
     'url': 'http://www.socat.info'},

     {'text': 'The GO-SHIP programme',
     'url': 'https://www.go-ship.org/About.html'},

     {'text': 'The Marine Institute operated Research Vessels',
     'url': 'https://www.marine.ie/Home/site-area/infrastructure-facilities/research-vessels/research-vessels'},
]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendTitle1='Deep-water Dissolved Inorganic Carbon Concentration (µmol/kg) '
figure_3_13 = IMAGES_PATH+'OceanicSections/Figure3.13_DeepWater_DissolvedInorganicConcentration_RockallTrough.png'
trendCaption1 = """
Deep-water dissolved inorganic carbon concentration (µmol/kg) section for the Rockall Trough in 
the winter of 2013 (left), during the annual survey on the Irish Shelf (right).  
The rows of vertical dots represent sampling points at different depths (left) 
and correspond to the blue point locations indicated in the red polygon (left)
"""
trendTitle2='Surface Water Dissolved Inorganic Carbon Concentration (µmol/kg) '
figure_3_14_a=IMAGES_PATH+'OceanicSections/HR_Final_ Winter2017_18 shelf pCO2_2.jpg'
figure_3_14_b = IMAGES_PATH+'OceanicSections/HR_Final_Summer 2018_final_2.jpg'
trendCaption2 = """
Surface water pCO2 measurements in a) Winter 2017-18 and b) Summer 2018, as collected by the RV Celtic Explorer. 
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
                                children=trendTitle1),
                            html.Img(
                                className='w-100',
                                src=figure_3_13
                            )
                                ]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    className="col-md-10 offset-md-1",
                    children=[
                        html.P(
                            className='sr-chart-caption',
                            children=trendCaption1
                        )]
                )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-12",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendTitle2)]
                        ),
                dbc.Col(className="col-12 col-md-6 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Winter 2017-18 '),
                            html.Img(
                                style={"marginTop":"-40px",
                                       "position":"relative",
                                       "z-index":"-1"},
                                src=figure_3_14_a
                            )]
                        ),
                dbc.Col(className="col-12 col-md-6 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Summer 2018'),
                        html.Img(
                                style={"marginTop":"-40px",
                                       "position":"relative",
                                       "z-index":"-1"},
                                src=figure_3_14_b
                            )
                                ]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    className="col-md-10 offset-md-1",
                    children=[
                        html.P(
                            className='sr-chart-caption',
                            style={"marginTop":"-40px",
                                   "position":"relative",},
                            children=trendCaption2
                        )]
                )
            ]
        ),

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
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
