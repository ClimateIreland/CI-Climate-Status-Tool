import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_7

chapter_num = '4.5'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Albedo_Malahide-BarryDuggan.jpg'
bannerImgCredit = 'Barry Duggan'

introText = """
    Radiation from the sun is essential for all biological processes on Earth. 
    The proportion of this radiation that is reflected by the Earth’s surface is known as 
    albedo. Albedo is key to understanding energy exchanges between the atmosphere 
    and the surface. The average Earth albedo is 0.3 on a scale from 0.0 to 1.0. 
    However, this proportion changes seasonally and regionally. 
        """
bulletPoint1 = """
    High albedo values are observed from surfaces covered by snow, while dense forest 
    and water bodies, which absorb most of the incident radiation, have low albedo.  
        """
bulletPoint2 = """
    An anomalously high value of albedo was observed during the last week of 2010, 
    when most of Ireland was covered in snow.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Mean 10-Day Albedo - Ireland'
trendChart = figure_4_7()

trendCaption = """

        """

infrastructureText = """
Ground-based observations of albedo require measurement of incoming and reflected solar radiation. These measurements tend to be made at local scales and for research studies. There is no long-term in situ albedo monitoring programme in Ireland.
Regional albedo measurements are generally made by satellite sensors, which have the ability to measure the total radiation reflected by the Earth’s surface on a regular basis. There is very good continuity of satellite observations since the 1980s from which albedo estimates can be inferred. The Copernicus Global Land Service (CGLS) generates a surface albedo dataset as part of a suite of energy monitoring products. This dataset is derived from the SPOT VEGETATION and PROBA-V satellite programmes. 

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Albedo ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/albedo/'},
         {'text': 'The Copernicus Global Land Service (CGLS) data',
     'url': 'https://land.copernicus.eu/global/products/sa'},
         {'text': 'Current global satellite albedo products',
     'url': 'https://lpvs.gsfc.nasa.gov/producers2.php?topic=SurfRad'},
         {'text': 'EUMETSAT Surface Albedo Validation Sites',
     'url': 'http://savs.eumetsat.int/'},
         {'text': 'Wang, Z., et al. (2019). Global Surface Albedo Product Validation Best Practices Protocol. Practice for Satellite Derived Land Product Validation (p. 45): Land Product Validation Subgroup (WGCV/CEOS). doi:10.5067/DOC/CEOSWGCV/LPV/ALBEDO.001 ',
     'url': 'https://www.researchgate.net/publication/332106030_Global_Surface_Albedo_Product_Validation_Best_Practices'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption1 = """
Time series of 10-Day periods of average albedo over Ireland derived from the Copernicus Global
 Land Service (CGLS) datasets for the period 1999 to 2018. 
 A seasonal trend is observed, in which the highest values occur during winter, particularly in 
 late December and early January, while the lowest values are observed during the summer months, 
 when vegetation cover is at its maximum.
        """

trendCaption2 = """
Albedo during four 10-day periods in 2018 derived from the Copernicus Global Land Service (CGLS) 
datasets. © European Union, Copernicus Land Monitoring Service 2020, European Environment Agency (EEA). 
The highest values are observed during the autumn and winter, when the presence of vegetation is reduced. 
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
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle),
                                dcc.Graph(
                                    figure=trendChart,
                                    id='chart'+chapter_dict['href'],
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
                                    children=[
                                        html.I(className="fas fa-play _up",
                                               style={"color": chapter_dict['domain-color']}),
                                        trendCaption1]
                                )]
                            )
                ]
            ),
                        dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children='Albedo Over Four 10-Day Periods in 2018'),
                                html.Img(src=IMAGES_PATH+'TerrestrialSections/Albedo_Seasonal_Maps.png')]
                            )
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
                                        trendCaption2]
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
        #     pb.build_trend(trendChartTitle,
        #                    trendChart,
        #                    trendCaption,
        #                    chapter_dict
        #                    ),
            custom_trend,
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            custom_infrastructure,
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
