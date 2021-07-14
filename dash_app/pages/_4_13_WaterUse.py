import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_26

chapter_num = '4.13'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Water_Use_Pixabay_tap-791172.jpg'
bannerImgCredit = 'Pixabay'

introText = """
Fresh water is used for drinking, cooking, cleaning, agriculture, producing 
electricity, industrial processes and recreation. 
This water generally comes from rivers, lakes and underground sources. 
Climate change is projected to aggravate already water-stressed areas and 
generate stress in regions where there is currently an adequate supply.
     """
bulletPoint1 = """
Global water use has increased by a factor of six over the past 100 years and 
continues to grow steadily at a rate of about 1% per year as a result of 
increasing population, economic development and shifting consumption patterns. 
     """
bulletPoint2 = """
Although Ireland generally has abundant water resources, periods of drought 
can lead to limited supplies and deteriorating quality. 
     """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
In 2018 the EPA launched the National Water Abstraction Register, in 
compliance with the WFD. Any person or organisation abstracting 25,000 l 
(25 m\u00B3) or more of groundwater or surface water per day is required to 
register. Before 2018, only public water supply bodies were obliged to 
register; therefore, there are  inaccuracies in the data on overall water use. 
Quality checking of the register is ongoing and this may lead to differences 
in future years, for example because of misclassification of registrations and 
the inclusion of additional abstractions in the register.
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Anthropogenic Water Use Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/water-use/'},
    {'text': 'Water use data on the OECD (Organisation for Economic Co-operation and Development) portal ',
     'url': 'https://stats.oecd.org/'},
    {'text': 'The EPA website on water abstraction registration',
     'url': 'https://www.epa.ie/our-services/monitoring--assessment/freshwater--marine/rivers/water-resources-and-abstractions/'},
    {'text': 'The EPA website on the Water Framework Directive',
     'url': 'https://www.epa.ie/our-services/monitoring--assessment/freshwater--marine/'},
    {'text': 'UNESCO (United Nations Educational, Scientific and Cultural Organization), The United Nations World Water Development Report 2020: Water and Climate Change',
     'url': 'https://unesdoc.unesco.org/ark:/48223/pf0000372985.locale=en'},
]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendTitle = "Freshwater Abstraction by End-use 2018"
trendChart1, trendChart2, trendChart3 = figure_4_26()
trendTitle1 = ""
trendTitle2 = "Surface Water"
trendTitle3 = "Groundwater"
trendCaption = """Total freshwater abstracted by sectors in Ireland during 2018 
from surface water and groundwater sources."""

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
                dbc.Col(className="col-12",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendTitle),
                            html.H5(
                                className='sr-chart-title',
                                children="Total: 2,030  million m\u00B3")],
                        ),
                dbc.Col(className="col-12 col-lg-6",
                        children=[
                            dcc.Graph(
                                figure=trendChart2,
                                config={'displayModeBar': False})]
                        ),
                dbc.Col(className="col-12 col-lg-6",
                        children=[
                            dcc.Graph(
                                figure=trendChart3,
                                config={'displayModeBar': False})]
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
                            children=[html.I(className="fas fa-play _up",
                                             style={"color": chapter_dict['domain-color']}),
                                      trendCaption]
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
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
