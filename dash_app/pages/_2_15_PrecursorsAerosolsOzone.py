import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import map_2_15

chapter_num = '2.15'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Precursotrs_Met_Eireann_20160315_062831.jpg'
bannerImgCredit = 'Met Éireann'

introText = """
Precursors are chemical species in the atmosphere that lead to the production 
of aerosols and ozone. Precursors include nitrogen dioxide (NO\u2082), sulfur 
dioxide (SO\u2082), carbon monoxide (CO) and formaldehyde (HCHO). In Ireland 
emissions from vehicles are the main source of NO\u2082 and CO, while domestic 
heating and electricity generation leads to emissions of SO\u2082. Aerosols and O\u2083 
in the near-surface atmosphere allied with these precursors can directly harm 
human health and produce detrimental environmental impacts (e.g. crop damage, 
acid rain).
       """
bulletPoint1 = """
Reductions in the concentrations of near-surface aerosols and O\u2083
have been observed in specific regions where the emissions of 
some precursors are regulated.
        """
bulletPoint2 = """

        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Nitrogen Dioxide Concentration - Ballyfermot'
# trendChart = figure_2_31()

trendCaption = """
Hourly concentrations (µg/m\u00b3) of nitrogen dioxide, NO\u2082, at Ballyfermot, Co. Dublin (2013–2018).
        """
infrastructureMap = map_2_15()
infrastructureText = """
The Environmental Protection Agency (EPA), through the national ambient air 
quality monitoring network, monitors NO\u2082, SO\u2082 and CO, as part of the air 
quality for health programme. These are not monitored as part of a climate 
observation programme. These observations comply to the EU's ambient air 
quality directives. The accompanying map shows the current national air monitoring 
sites. Not all species are measured at all sites.  
        """


infoLinks = [
    {'text': 'Precursors for Aerosols and Ozone Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/precursors/'},
     {'text': 'National Ambient Air Quality Monitoring Programme 2017–2022',
     'url': 'https://www.epa.ie/publications/monitoring--assessment/air/national-ambient-air-quality-monitoring-programme-2017-2022.php'},
     {'text': 'EPA Air Quality Index for Health',
     'url': 'https://www.epa.ie/environment-and-you/air/'},
          {'text': 'EPA Air Quality Index for Health Map',
     'url': 'https://airquality.ie/'},
]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendImg = IMAGES_PATH+'AtmosphericSections/figure_2_31.png'

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
                                children=trendChartTitle),
                            html.Img(
                                className='w-100',
                                style={'max-width':800},
                                src=trendImg
                            )
                        ]
                        ),

            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[
                                    html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption]
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
