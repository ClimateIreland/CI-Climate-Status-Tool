import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_2_8

chapter_num = '2.8'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Clouds_madeleineweber_hailshower.jpg'
bannerImgCredit = 'Madeleine Weber'

introText = """
Clouds play an essential role in the Earth’s energy budget, maintaining the 
radiation balance, and are a key component of the Earth’s hydrological cycle. 
They form when water vapour condenses as water droplets or ice crystals in the 
atmosphere. Aerosols in the atmosphere act as condensation nuclei around which 
clouds form. Clouds both cool and warm the Earth’s atmosphere, absorbing heat 
emitted from the surface and radiating it to space. Clouds also generate 
precipitation from water vapour, releasing heat to the atmosphere in the 
process. How clouds respond to changes in the climate 
is complex and it is difficult to determine their net effect on energy balance 
and on the water cycle.
     """
bulletPoint1 = """
Larger numbers of smaller cloud droplets are observed in the presence of 
greater levels of pollution, which translates into clouds that are brighter, 
thus reflecting more sunlight than clean 
clouds.
        """
bulletPoint2 = """
The aerosol profiling and microphysical 
cloud property (ground-based remote sensing) measurements at Mace Head ceased 
in 2020, as ongoing operational funding could not be secured.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Probability Distributions of Cloud Droplet Concentrations (CDNC) - Mace Head'
# trendChart = empty_chart()



infrastructureText = """
A range of cloud properties are observed at the Mace Head Atmospheric Research 
Station, Carna, Co. Galway (black). These include vertical extent 
(cloud base and cloud top), cloud particle phase (liquid, ice), degree of 
adiabaticity, liquid water path and liquid water content, microphysical 
properties such as effective radius, cloud droplet number concentration and 
size distribution. Met Éireann takes hourly manual observations of cloud 
cover, cloud type and cloud height at staffed synoptic weather stations 
(orange and blue). Observations of cloud height and estimated total cloud 
cover are made at a number of automated synoptic stations (blue, red and black). 
A range of satellite sensors are used to collect information related to cloud 
properties. The ESA Climate Change Initiative (CCI) Cloud project provides 
long-term, coherent cloud property data sets based on past, and existing 
European and US satellite missions. 

        """
infrastructureMap = map_2_8()

infoLinks = [
    {'text': 'Clouds Essential Climate Variable (ECV) Factsheet',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/clouds'},
     {'text': 'Information on NUI Galway’s Atmospheric and Environmental Physics Cluster and Mace Head facility',
     'url': 'http://www.macehead.org/'},
     {'text': 'Met Éireann information on data availability',
     'url': 'https://www.met.ie/climate/available-data/'},
     {'text': 'About ESA’s Cloud Climate Change Initiative project',
     'url': 'http://www.esa-cloud-cci.org/?q=about'},
     {'text': 'About EUMETSAT, Europe’s weather satellite programme',
     'url': 'https://www.eumetsat.int/'},
     {'text': 'Preißler, J. et al., 2016. Six years of surface remote sensing of stratiform warm clouds in marine and continental air over Mace Head, Ireland. Journal of Geophysical Research Atmospheres 121: 14538–14557.',
     'url': 'https://doi.org/10.1002/2016JD025360'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption = [
        html.I(className="fas fa-play _up",style={"color": chapter_dict['domain-color']}),
        'Probability distributions of cloud droplet concentrations (CDNC) (a) and Droplet radius (r',
        html.Sub(html.I('eff')),
        """
        ) (b) by air mass transport. Cloud properties in marine (clean) and 
        continental (polluted) air masses are presented with colour bars while clouds 
        in modified air masses are plotted as lines (modified air masses are the 
        mixture of both marine and continental air masses, where mar. mod. - marine m
        odified represents marine air mass with some continental influence and cont. 
        mod. - continental modified - represents continental air mass with some marine 
        influence). Data cover the period (2009 – 2015) at Mace Head.
        """
        ]

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
                                src=IMAGES_PATH+'AtmosphericSections/Figure2.14_DistrbutionCloudDropletConcentrations.png')]
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
