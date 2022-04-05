import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.12c'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Other_Marine_Institute_ DSC_03515_Weather buoy.JPG'
bannerImgCredit = 'Marine Institute'

introText = """
Surface heat flux is exchange of heat, per unit area, crossing the surface 
between the ocean and the atmosphere. Heat may be transferred into the ocean 
from the atmosphere or vice-versa. This heat transfer occurs in a number of 
different ways. Heat may be transferred through evaporation or condensation of 
water; it can be transferred directly by conduction and convection; it can be 
transferred into the ocean by direct radiation from the sun or back from the 
ocean by reflection or emission of energy to the atmosphere. 
        """
bulletPoint1 = """
Surface heat flux has a strong influence on climate and is linked to floods and 
droughts, storm intensity and tracks. 
        """
bulletPoint2 = """
Climate variations such as the North 
Atlantic Oscillation and the El Niño Southern Oscillation are also associated 
with variability in these heat exchanges. 
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Parameters related to heat flux may 
be measured from moored instruments and from those deployed by ships. Pilot 
studies to retrieve relevant parameters from data collected by satellite 
platforms are underway.
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Ocean Surface Heat Flux Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ocean-heat/'},
         {'text': 'Information about GO-SHIP',
     'url': 'https://www.go-ship.org/About.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendText= """
Surface Heat Flux was added in the 2016 revision of the GCOS implementation plan. To date no observations have been established for Ireland.
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
            custom_trend,
            custom_infrastructure,
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
