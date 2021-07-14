import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.12b'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Other_Marine_Institute_ DSC_03515_Weather buoy.JPG'
bannerImgCredit = 'Marine Institute'

introText = """
When wind blows over the open ocean a surface stress is induced. This stress 
depends on a number of characteristics of the atmosphere, such as 
stratification and air density, and of the ocean, such as wave state and wave 
age. The magnitude of the stress influences the air-sea exchange of energy, 
water (evaporation), and oxygen, carbon dioxide and other gases.      
        """
bulletPoint1 = """
Surface 
stress drives coastal currents, storm surge, surface waves, and ice transport; 
also, ocean surface turbulence and mixed layer evolution, and is a factor in 
deep-water formation.
        """
bulletPoint2 = """
Ocean surface stress is 
critically important for determining the large-scale wind- and buoyancy-driven 
ocean circulation.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Surface stress can be determined from data collected by 
moored instruments, those deployed by ships and from data collected by 
satellite borne instruments.
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Ocean Surface Stress Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-stress'},
         {'text': 'Information about GO-SHIP',
     'url': 'https://www.go-ship.org/About.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendText= """
Surface stress was added in the 2016 revision of the GCOS implementation plan. To date no observations have been established for Ireland.
"""
custom_trend = dbc.Container(
        className='sr-trends',
        style={'borderColor': chapter_dict['domain-color']},
        id='trends',
    children=[
        html.H3(
            className='sr-section-heading',
            children='Trends',
            style={'color': chapter_dict['domain-color']},
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-12 my-auto",
                        children=[
                            html.P(trendText)]
                        ),

            ])
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
