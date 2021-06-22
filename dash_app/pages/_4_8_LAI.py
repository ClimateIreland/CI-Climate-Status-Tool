import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_14

chapter_num = '4.8'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/LAI_AnnetteMathys.jpg'
bannerImgCredit = 'Annette Mathys'

introText = """
    Leaf area index (LAI) is a measure of the amount of surface area of 
    leaf per area of ground surface and is a key parameter for assessing 
    the health and growth of vegetation over time. LAI is defined by the 
    structure of a plant canopy and is directly linked to the interaction 
    between biosphere and atmosphere through several process, such as 
    photosynthesis, evapotranspiration, respiration, rain interception 
    and leaf litter fall.  
        """
bulletPoint1 = """
    Regular observations of LAI are essential for several ecological models 
    describing vegetation–atmosphere interactions, such as biogeochemical cycles, 
    hydrological budgets and carbon uptake and sequestration.
        """
bulletPoint2 = """
    The highest values of LAI in Ireland, which are seen in forest areas, 
    are observed between May and June.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = '10-Day Mean Leaf Area Index Over Ireland'
trendChart = figure_4_14()

trendCaption = """

        """

infrastructureText = """
Ground-based LAI is normally calculated directly by collecting leaf material over a certain area, or indirectly estimated based on relationships with other more easily measurable parameters through photography and other optical instruments. It is a time consuming and laborious process and can only be done at the local scale. There is no long-term in situ monitoring programme in Ireland.
LAI is also estimated over large areas from satellite-sensor data using reflectance information from the visible and infrared part of the spectrum. The Copernicus Global Land Service (CGLS) generates a LAI dataset as part of a set of vegetation monitoring products. This dataset is derived from the SPOT VEGETATION and PROBA-V satellite programmes. 

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Leaf Area Index ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/lai/'},
         {'text': 'Copernicus Global Land Service (CGLS) data',
     'url': 'https://land.copernicus.eu/global/products/lai'},
         {'text': 'Copernicus vegetation phenology and productivity product',
     'url': 'https://land.copernicus.eu/pan-european/biophysical-parameters/high-resolution-vegetation-phenology-and-productivity'},
         {'text': 'Vegetation Status Indicators from Sentinel-2 for Agriculture (Sen2-Agri) project',
     'url': 'http://www.esa-sen2agri.org/products/vegetation-status/'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption1 = """
    Heat map of 10-Day periods of average LAI over Ireland derived from the Copernicus Global Land Service 
    (CGLS) datasets for the period 1999 to 2018. The data are presented as percentiles. 
    For example, the 75th percentile means that 75% of all the values are below 3.07 and 25% of the values are above it.
    Seasonal variability is observed, in which the highest values occur during late spring and early summer, 
    particularly between May and June, while the lowest values are observed during the winter months.
        """
trendCaption2 = """
    Leaf Area Index (LAI) during four 10-day periods in 2018 derived from the Copernicus Global Land Service 
    (CGLS) datasets. © European Union, Copernicus Land Monitoring Service 2020, European Environment Agency (EEA).
    The brown shading corresponds to areas with high LAI and yellow/white shading indicates sparse vegetation.
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
                                    children='Leaf Area Index During Four 10-Day Periods in 2018'),
                                html.Img(src=IMAGES_PATH+'TerrestrialSections/LAI_Seasonal_Maps.png')]
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
