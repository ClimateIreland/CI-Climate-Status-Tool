import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_2_14

chapter_num = '2.14'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Aerosols_Mihaly Csernus.jpg'
bannerImgCredit = 'Mihaly Csernus'

introText = """

        """
bulletPoint1 = """

        """
bulletPoint2 = """

        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """

        """
infrastructureMap = map_2_14()

infoLinks = [
    {'text': '',
     'url': ''},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

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
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Aerosol Scattering Coefficient - Mace Head, Co. Galway'),
                            html.Img(
                                src=IMAGES_PATH+'AtmosphericSections/Figure 2.28_MonthlyYearlyAerosolMaceHead.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          '']
                            )]
                        )
            ]
        ),
                dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Sulphur Air Polution Trend'),
                            html.Img(
                                src=IMAGES_PATH+'AtmosphericSections/Figure2.29_SulphurAirPollutionTrends_v2.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          '']
                            )]
                        )
            ]
        ),
                        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Global Aerosol Optical Depth'),
                            html.Img(
                                src=IMAGES_PATH+'AtmosphericSections/Figure2.30_GlobalAerosolOpticalDepthSatelliteObservations.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          '']
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
