import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_4, map_2_2

chapter_num = '2.2'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Wind_Myrtleville_Ophelia_Aldert Otter.jpg'
bannerImgCredit = 'Aldert Otter'

introText = """

        """
bulletPoint1 = """

        """
bulletPoint2 = """

        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()
trendChartA, trendChartB = figure_2_4()
trendChart = trendChartA

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = map_2_2()

infoLinks = [
    {'text': '',
     'url': ''},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

figure_2_5 = IMAGES_PATH+'AtmosphericSections/Figure2.5_v2.png'
trendCaption2 = """

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
                dbc.Col(className="col-12",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Wind Speed and Gale Gust Days')]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Valentia'),
                            dcc.Graph(
                                figure=trendChartA,
                                config={'displayModeBar': False})]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Dublin Airport'),
                            dcc.Graph(
                                figure=trendChartB,
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
             dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 col-lg-8 offset-lg-2 text-center col",
                        children=[
                             html.H4(
                                className='sr-chart-title',
                                children='Example of Wind Speed and Direction Map'),
                            html.Img(
                                src=figure_2_5)]
                        ),
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
                                    trendCaption2]
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
        #     pb.build_trend(trendChartTitle,
        #                    trendChart,
        #                    trendCaption,
        #                    chapter_dict
        #                    ),
            custom_trend,
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
