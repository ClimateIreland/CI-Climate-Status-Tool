import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import LandCoverArea1990, LandCoverArea2018, LandCoverTrend, surfaceAirTempStationsMap

chapter=4.6
ecvName='Land Cover'
bannerImgSrc=IMAGES_PATH+'TerrestrialSections/Land_Cover_IMG_1918 Barry O Dwyer.jpg'
bannerImgCredit='Credit: Barry O Dwyer'
ecvIconSrc=IMAGES_PATH+'icons/land-cover.png'

introText="""
        Land cover - the observed (bio)-physical cover on the Earth’s surface, 
        including grassland, forest, built environment, etc. – plays a key role in 
        climate dynamics such as water and energy exchanges between the ground and 
        the atmosphere, and contributes to the capture and release of greenhouse gases and aerosols. 
        """
bulletPoint1="""
        Peatlands represent almost 14% of Irish land cover and are an essential 
        feature in the regulation of the climate by removing carbon.
        """
bulletPoint2="""
        Land cover observations since 1990 show increases in the area covered 
        by artificial surfaces and forests and a decrease in wetland areas which include peatlands.
        """

domain='Terrestrial'
subdomain='Biology'
scientificArea='Biosphere'
authors='Walther C.A. Cámaro García, Ned Dwyer'

trendChartTitle='Percentage of Cumulative Change within Each Class'
trendChart=LandCoverTrend()


trendCaption="""
           CORINE main category distribution over Ireland (% national area) for the CORINE 1990 version (left) and for the CORINE 2018 version (right)
        """

infrastructureText="""
        The CGLS is one of the Copernicus services that provide satellite information that may be 
        used to monitor a number of vegetation parameters around the globe. 
        The global FAPAR dataset available is derived from several satellite sensors. 
        Currently, the CGLS team is updating the dataset based on SENTINEL-3 OLCI and SLSTR 
        sensors as new data sources. Comprehensive analysis of satellite-derived FAPAR 
        spatio-temporal trends for Ireland needs to be carried out. 
        A ground-based observation system should also be considered in order to validate 
        and support the satellite observations. 
        """
infrastructureMap=surfaceAirTempStationsMap()

infoLinks=[{'text':'text', 
            'url':'https://gcos.wmo.int/en/essential-climate-variables/surface-temperature/'},

            ]

chapter_dict=next((item for item in CHAPTERS if item['chapter']==chapter),None)
########################################################################################################################

trendCaption2="""
              Above shows percentage cumulative 
              change within each main category for the five 
              CORINE versions between 1990 and 2018. 

              """


custom_trend = dbc.Container(
        className='sr-trends',
        style={'borderColor':chapter_dict['domain-color']},
        id='trends',
        children=[
        html.H3(
            className='sr-section-heading',
            style={'color':chapter_dict['domain-color']},
            children='Trends and Observations',
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
                                figure=LandCoverArea1990(),
                                config={'displayModeBar': False})]
                            ),
                dbc.Col(className="col-12 col-md-6",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='2018'),
                            dcc.Graph(
                                figure=LandCoverArea2018(),
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
                                children=trendCaption
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
                                children=trendCaption2
                                )]
                            )
                        ]
                    ),
            ])

custom_infrastructure=  dbc.Container(
        className='sr-infrastructure',
        style={'borderColor':chapter_dict['domain-color']},
        id='infrastructure',
        children=[
            html.H3(
                className='sr-section-heading',
                children='Observation Infrastructure',
                style={'color':chapter_dict['domain-color']},
                ),
            dbc.Row(
                children=[
                    dbc.Col(className="col-12 col-md-6 my-auto",
                    children=[
                        html.P(infrastructureText)]
                    ),
                    dbc.Col(className="col-12 col-md-6 my-auto",
                    children=[
                        html.I(
                            style={'position':'relative','float':'right','bottom':'-25px', 'margin-right':'10px'},
                            className='fas fa-arrows-alt '
                            ),
                        html.Iframe(
                            style={'height':'450px','width':'100%', 'border':'none'},
                            src='https://maps.eea.europa.eu/CopernicusViewer/?webmap=f9a8ae48d60a49f1bd9b16dba0f2c5fe'
                    )
                    ])
                    ])
                ])


########################################################################################################################


def create_layout(app):
      return html.Div(
              children=[
        pb.build_banner(ecvName,
                        bannerImgSrc,
                        bannerImgCredit,
                        chapter_dict
                        ),
        pb.build_breadcrumb(ecvName,
        chapter_dict),
        pb.build_nav(chapter_dict),
        pb.build_intro(ecvName,
                       introText,
                       bulletPoint1,
                       bulletPoint2,
                       ecvIconSrc,
                       subdomain,
                       scientificArea,
                       authors,
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
