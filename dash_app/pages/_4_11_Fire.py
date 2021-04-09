import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_22

chapter_num = '4.11'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Fire on arrival Ian Kiely.jpg'
bannerImgCredit = 'Ian Kiely'

introText = """
Vegetation fires and wildfires are an increasingly visible phenomenon in Ireland in recent years. 
Despite Ireland’s generally moist oceanic climate, periodic dry spells in spring annually give 
rise to fire risk conditions and facilitate fire outbreaks. Most fires in Ireland can be attributed 
to human causes, whether deliberate or unintentional.  
        """
bulletPoint1 = """
Globally, along with fossil-fuel burning and agriculture, vegetation fires are one of the largest 
human-caused greenhouse gas emission contributors.   
        """
bulletPoint2 = """
Annual burned area in Ireland is thought to range between 4,000 and 6,000 ha annually, 
with the bulk of fire activity taking place between March and June each year.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Very High or Extreme Fire Danger'
trendChart = figure_4_22()
trendCaption = """
Number of days on which the fire index was very high or extreme as 
calculated using data from Dublin airport and Shannon airport synoptic stations (1971–2018).
        """

trendChartTitle2 = 'Forest Fires in Ireland'
trendChart2 = IMAGES_PATH+'TerrestrialSections/Figure4.21_ForestFiresInIreland.png'
trendCaption2 = """
Combined forest area burned (2000 – 2019) and annual Fire Service mobilizations (2000-2018) to bog, grass, and forest fires. 
Bars: Area burned, dark green public (Coillte) forest, light green private forest. Blue line: number of Fire Service mobilizations. 
Red line: Trend in mobilisations. Source: Department of Housing, Planning, Community and Local Government and Department of Agriculture, 
Food and the Marine (DAFM).
        """
trendChartTitle3 = 'Optimised Hotspot Analysis'
trendChart3 = IMAGES_PATH+'TerrestrialSections/optimised_hot_spot_analysis_rev_2_V2.png'
trendCaption3 = """
Optimised Hotspot analysis of fire detection locations in Ireland 2002-2017, based on identification of 
fire locations from satellite imagery. Location of fires detected by satellite shown as pink crosses
        """

infrastructureText = """
Data on vegetation fires are generally not compiled centrally by the fire services, 
however burned area estimates, based on assessments of known fires are generated 
for reporting by the Department of Agriculture, Fisheries and the Marine (DAFM) 
to the European Commission annually. Daily fire risk is assessed by Met Éireann 
using meteorological variables derived using the Canadian Fire Weather Index (FWI), 
and fire danger notices are issued to forestry interests by DAFM throughout the fire season. 
Satellite data are used internationally to make regional and global estimates of fire 
disturbance and their impact on the atmosphere and some research studies have been 
carried out on their utility over Ireland This image from the Sentinel- 2 satellite 
shows a fire burning in Co. Wicklow on June 30th 2018. 
        """
infrastructureImg = IMAGES_PATH+'TerrestrialSections/FireInfrastructure.png'

infoLinks = [
    {'text': 'Fire ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/fire/'},

     {'text': 'Prat-Guitart, N.; Nugent, C.; Mullen, E.; et al. (2019) Peat Fires of Ireland. In Coal and Peat Fires: A Global Perspective; Stracher, G.B., Prakash, A., Sokol, E.V., Eds.;Elsevier Inc.: Amsterdam, The Netherlands, Vol. 5, pp. 451–482',
     'url': 'https://doi.org/10.1016/C2016-0-02048-X'},

     {'text': 'Annual Reports on Forest Fires in Europe Middle East and North Africa',
     'url': 'https://effis.jrc.ec.europa.eu/reports-and-publications/annual-fire-reports'},

     {'text': 'Global Wildfire Information System',
     'url': 'https://gwis.jrc.ec.europa.eu/apps/gwis_current_situation/'},

     {'text': 'Fire, Land and Atmospheric Remote Sensing of Emissions (FLARES) project',
     'url': 'https://www.ucc.ie/en/eri/projects/flares--fire-land-and-atmospheric-remote-sensing-of-emissions.html'},

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
                        dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1 text-center",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle2),
                                html.Img(
                                style={"max-width":"800px"},
                                # className='w-100',
                                src=trendChart2)
                                    ]
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
                                    dbc.Row(
                children=[
                    dbc.Col(className="col-md-10 offset-md-1 text-center",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle3),
                                html.Img(
                                style={"max-width":"600px"},
                                # className='w-100',
                                src=trendChart3)
                                    ]
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
                dbc.Col(className="col-12 col-md-6 my-auto",
                        children=[
                            html.P(infrastructureText)]
                        ),
                dbc.Col(className="col-12 col-md-6 my-auto",
                        children=[
                        html.Img(
                                src=infrastructureImg)
                        ])
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
