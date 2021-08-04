import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.12d'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Other_Marine_Institute_ DSC_03515_Weather buoy.JPG'
bannerImgCredit = 'Marine Institute'

introText = """
Nitrous oxide (N\u2082O) is present in the atmosphere in small quantities. 
In the upper atmosphere it acts as a strong greenhouse gas with a global 
warming potential 256 times that of carbon dioxide and in the lower atmosphere 
it destroys ozone.  
        """
bulletPoint1 = """
Globally, about 40% of total N\u2082O emissions come from human activities, 
approximately 30% comes the microbial breakdown of nitrogen in soils, and 
microbial activity in the ocean is responsible for the remaining 30%. 
        """
bulletPoint2 = """
Understanding the spatio-temporal variability in oceanic N\u2082O concentrations 
and emissions is important in order to improve quantification of and 
understanding of the role of the ocean in the nitrogen cycle.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
The leading global observation network that supports collection of the required information is the Global Ocean Ship based Hydrographic Investigations Programme (GO-SHIP). 
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Nitrous Oxide Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/n2o/'},
         {'text': 'Information about GO-SHIP',
     'url': 'https://www.go-ship.org/About.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendText= """
Nitrous Oxide was added in the 2016 revision of the GCOS implementation plan. To date no observations have been established for Ireland.
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
