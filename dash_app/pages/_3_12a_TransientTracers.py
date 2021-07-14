import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart

chapter_num = '3.12a'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Other_Marine_Institute_ DSC_03515_Weather buoy.JPG'
bannerImgCredit = 'Marine Institute'

introText = """
Transient tracers are human-made chemical substances that have a known 
concentration history in the atmosphere. These substances are partly absorbed 
by the ocean and becomes dissolved in water. Their  measurement provides an 
insight into ocean processes. By measuring their presence in the subsurface 
of the ocean it is possible to estimate when the gas entered the ocean, how 
quickly it disperses and how it is transported by currents and into the deep 
ocean. Such knowledge also helps in understanding and quantifying the 
concentration and fates of other compounds such as anthropogenic carbon and 
nitrous oxide. Moreover, it improves knowledge of the overturning circulation 
of water masses in the ocean itself. 
     """
bulletPoint1 = """
Chlorofluorocarbons (CFCs), themselves a 
powerful greenhouse gas, are a persistent industrial chemical whose 
atmospheric concentrations increased and then decreased after the signing of 
the Montreal Protocol to phase them out in 1987. This was in response to the 
recognition of the damage they were causing to the Earth’s ozone layer.
     """
bulletPoint2 = """
14C 
and tritium were released to the atmosphere in pulses during nuclear weapons 
tests in the 1950s and 1960s.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
The leading global observation network 
that supports collection of the required information is the Global Ocean Ship 
based Hydrographic Investigations Programme (GO-SHIP). NUI Galway and the 
Marine Institute have collaborated with GEOMAR, Germany who have specific 
<<<<<<< HEAD
expertise in this field, to sample for CFCs and SF\u2086 during the trans-Atlantic 
=======
expertise in this field, to sample for CFCs and SF6 during the trans-Atlantic 
>>>>>>> a72fadad0ee2461f2812cb8210d88bd419730c0c
GOSHIP A02 survey in 2017 and subsequently in the Rockall Trough. 
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Transient Tracers Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/transient-tracers'},
         {'text': 'Information about GO-SHIP',
     'url': 'https://www.go-ship.org/About.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendText= """
Transient tracers have only been observed on a very limited number of 
occasions in Irish waters, hence it is currently not possible to provide any 
information on their evolution over time or trends. 
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
<<<<<<< HEAD
            custom_trend,
=======
>>>>>>> a72fadad0ee2461f2812cb8210d88bd419730c0c
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
