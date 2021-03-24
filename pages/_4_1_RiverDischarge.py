import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '4.1'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/River_Discharge_NedDwyer_P1090399.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
        Changes in climate affect rivers and the flora, fauna and humans that depend on them, 
        in the form of increasing droughts, floods and waterborne diseases. 
        Changes in precipitation patterns, temperature, groundwater runoff and sea level 
        rise as well as human use and interventions affect river conditions, generating 
        impacts on energy production, infrastructure, human health, agriculture and ecosystems.
        """
bulletPoint1 = """
        Analysis of a long time series of more than 50 years of data (1972 to 2017) 
        indicates an increase in river flows across most of the country
        """
bulletPoint2 = """
        Analysis of a shorter data period from 1992 suggests an increase in potential 
        drought conditions, especially in the east. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Annual Trend of River Flow'
trendChart = empty_chart()

trendCaption = """
Annual trend of river flows over the island of Ireland for different types of 
flow based on the hydrometric network as of 1972 (long period) and 1992 (short period).  
Blue arrows indicate and increasing trend while red arrows indicate a decreasing trend. 
Changes identified as significant are indicated by arrows with white fills. (adapted from  Murphy et al., 2013)  
        """

infrastructureText = """

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': '',
     'url': ''},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

figure_4_1 = IMAGES_PATH+'TerrestrialSections/Figure4.1_AnnualTrendRiverFlows.png'
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
                                html.Img(
                                    className='w-100',
                                    src=figure_4_1
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
                                    children=trendCaption
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
