import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_22, figure_2_23, figure_2_24

chapter_num = '2.12'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Other_GHG_IMG_3709 Hester Whyte.JPG'
bannerImgCredit = 'Hester Whyte'

introText = """
In addition to water vapour, carbon dioxide (CO\u2082) and methane (CH\u2084), 
a number of other gases contribute significantly to the enhanced greenhouse effect.  
These include Nitrous oxide (N\u2082O) which has a global warming potential 265 times that of 
CO2 and synthetic gases which are exclusively produced by human activities but have extremely high global warming potentials.
        """
bulletPoint1 = """
        N\u2082O concentrations in the atmosphere are now approximately 20% 
        higher compared to the pre-industrial era  
        """
bulletPoint2 = """
        Synthetic gasses, which replaced ozone depleting chlorofluorocarbons 
        (CFCs) are increasing steadily in the atmosphere.
        """
bulletPoints = [bulletPoint1, bulletPoint2]

# first chart
trendChartTitle = 'Nitrous oxide (N\u2082O) Concentration (1978-2018)'
trendChart = figure_2_22()
trendCaption = """
        Monthly mean nitrous oxide concentration observed at Adrigole (1978-1984) and Mace Head Research Station (1987–2018). There are some gaps in the data record. Units are part per billion (ppb).
        """
# second chart
trendChartTitle2 = 'CFC-12 Concentration (1978-2018)'
trendChart2 = figure_2_23()
trendCaption2 = """
        Monthly mean CFC-12 concentration observed at Adrigole (1978-1984) and Mace Head Research Station (1987-–2018). There are some gaps in the data record. Units are part per trillion (ppt).
        """
# third chart
trendChartTitle3 = 'HFC-134a Concentration (1994-2018)'
trendChart3 = figure_2_24()
trendCaption3 = """
        Monthly mean HFC-134a concentration observed at Mace Head Research Station (1994-2018). Units are part per trillion (ppt).
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


# create a custom layout for >1 chart
custom_trend =  dbc.Container(
            className='sr-trends',
        style={'borderColor': chapter_dict['domain-color']},
        id='trends',
        children=[
            html.H3(
                className='sr-section-heading',
                style={'color': chapter_dict['domain-color']},
                children='Trends',
            ),
            # First chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle),
                                dcc.Graph(
                                    figure=trendChart,
                                    config={'displayModeBar': False})]
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
            # Second chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle2),
                                dcc.Graph(
                                    figure=trendChart2,
                                    config={'displayModeBar': False})]
                            )
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.P(
                                    className='sr-chart-caption',
                                    children=trendCaption2
                                )]
                            )
                ]
            ),
            # Third chart
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle3),
                                dcc.Graph(
                                    figure=trendChart3,
                                    config={'displayModeBar': False})]
                            )
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.P(
                                    className='sr-chart-caption',
                                    children=trendCaption3
                                )]
                            )
                ]
            ),
        ])

########################################################################################################################
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
