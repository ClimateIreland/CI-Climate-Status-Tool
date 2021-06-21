import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_4_10_1, figure_4_10_2, figure_4_11

chapter_num = '4.6'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Land_Cover_IMG_1918 Barry O Dwyer.jpg'
bannerImgCredit = 'Barry O Dwyer'

introText = """
        Land cover - the observed (bio)-physical cover on the Earth’s surface, 
        including grassland, forest, built environment, etc. – plays a key role in 
        climate dynamics such as water and energy exchanges between the ground and 
        the atmosphere, and contributes to the capture and release of greenhouse gases and aerosols. 
        """
bulletPoint1 = """
        Peatlands represent almost 14% of Irish land cover and are an essential 
        feature in the regulation of the climate by removing carbon.
        """
bulletPoint2 = """
        Land cover observations since 1990 show increases in the area covered 
        by artificial surfaces and forests and a decrease in wetland areas which include peatlands.
        """
bulletPoints = [bulletPoint1, bulletPoint2]

trendChartTitle = 'Percentage of Cumulative Change within Each Class'
trendChart = figure_4_11()


trendCaption = """
           CORINE main category distribution over Ireland (% national area) for the CORINE 1990 version and for the CORINE 2018 version.
        """
trendCaption2 = """
              Percentage cumulative change within each main category for 
              the five CORINE versions between 1990 and 2018.  Artificial surfaces 
              show the greatest cumulative increase, with a particularly high rate 
              between 1990 and 2006. Forest areas have also increased, being particularly marked during the 1990s.  
              The wetlands class is mostly formed on peat, and a continuous decreasing trend is observed in this land cover class  
              """


infrastructureText = """
Since 1990 regular, systematic land cover mapping of Ireland, using satellite imagery, has taken place as part of the 
European Commission’s CORINE  programme. Until now, CORINE has been the only initiative in place in Ireland that 
provides a set of time series of land cover data, however albeit with a coarse (25-ha) spatial resolution that misses 
many important environmental features within the very fragmented landscape of Ireland. A current EPA and Ordnance Survey 
Ireland (OSi) led initiative aimed at generating a new land cover dataset, with a spatial resolution almost 250 times better than CORINE,
 will be released later in 2021.
        """
# custom infrastruture uses corina iframe
# infrastructureMap=surfaceAirTempStationsMap()

infoLinks = [
    {'text': 'Land Cover ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/land-cover/'},
    {'text': 'The CORINE dataset in Ireland',
     'url': 'https://www.epa.ie/soilandbiodiversity/soils/land/corine/'},
    {'text': 'View CORINE maps for all of Europe',
     'url': 'https://land.copernicus.eu/pan-european/corine-land-cover'},
    {'text': 'The ILMO project',
     'url': 'https://landmapping.wordpress.com/ilmo/'},
    {'text': 'The TALAM project',
     'url': 'https://landmapping.wordpress.com/talam/'},
    {'text': 'The BRIAR project',
     'url': 'https://landmapping.wordpress.com/briar-biomass-retrieval-in-ireland-using-active-remote-sensing/'},
    {'text': 'Irish Times article on Ireland´s new land cover mapping initiative',
     'url': 'https://www.irishtimes.com/news/science/ireland-needs-needs-more-detailed-land-use-maps-1.4010070'},
]

chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)
########################################################################################################################



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
                                children='Ireland Landcover Distribution')]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='1990'),
                            dcc.Graph(
                                figure=figure_4_10_1(),
                                config={'displayModeBar': False})]
                        ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='2018'),
                            dcc.Graph(
                                figure=figure_4_10_2(),
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
                            dcc.Link(
                                style={
                                    'color':chapter_dict['domain-color'],
                                    'position': 'relative', 'float': 'right',
                                       'bottom': '-30px', 'margin-right': '10px'},
                                href='https://maps.eea.europa.eu/CopernicusViewer/?webmap=f9a8ae48d60a49f1bd9b16dba0f2c5fe',
                                target='_blank',
                                title='Open Full Screen',
                                children=[
                                    html.I(className='fas fa-arrows-alt ')]),
                            html.Iframe(
                                style={'height': '450px',
                                       'width': '100%', 'border': 'none'},
                                src='https://maps.eea.europa.eu/CopernicusViewer/?webmap=f9a8ae48d60a49f1bd9b16dba0f2c5fe'
                            )
                        ])
            ])
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
            # pb.build_trend(trendChartTitle,
            #                trendChart,
            #                trendCaption,
            #                chapter_dict
            #                ),
            custom_trend,
            custom_infrastructure,
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
