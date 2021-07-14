import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_17

chapter_num = '4.9'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Biomass-Mihaly Csernus.jpg'
bannerImgCredit = 'Mihaly Csernus'

introText = """
Biomass is any organic or biological material that comes from plants or 
animals. Above-ground biomass includes all biomass stored above the soil in 
both woody and herbaceous living vegetation and is a key parameter for 
understanding the evolution of and changes in the climate system. The process 
of photosynthesis stores carbon in vegetation biomass in a similar amount to 
that stored in the atmosphere and is one of the most visible carbon pools. 
        """
bulletPoint1 = """
The growing stock volume of trees has increased by 38% in Ireland in the period
 between 2006 and 2017.
        """
bulletPoint2 = """
Just under 50% of the trees grown in Ireland are in private ownership and this 
is where the biggest increase in tree volume has occurred thanks to state 
grant aid.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Quantification of above ground biomass is based on the mass of plant material 
and can be inferred from plant volume. These parameters are normally estimated 
from a number of attributes including tree growth and development, the 
diversity of plant species and soil type. Since 2007, the National Forestry 
Service periodically carries out in situ data collection nationwide. The third 
cycle of data collection completed in 2017, which is the most recent, assessed 
a total of 1932 forest plots.  These assessments are essential for the 
development of country-specific models to estimate biomass and hence carbon 
stocks in forest, information that is compiled annually in the National 
Inventory Report. In general, an assessment of above-ground biomass is a 
suitable indicator of other carbon pools with the exception of soils. 
Internationally, remote-sensing data have been used to estimate above ground 
biomass. The ESA Climate Change Initiative (CCI) Biomass project aims to 
provide global maps of above-ground biomass for several periods from the 
1990s, based on optical sensors (e.g. Sentinel 2), radar sensors (ALOS-2) and 
laser sensors (e.g. GEDI LIDAR). 
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Above Ground Biomass ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/biomass/'},
         {'text': 'Green, S., Martin, A., Gharechelou, S., at al., 2019, BRIAR: Biomass Retrieval in Ireland using Active Remote Sensing, Report No. 305, Environmental Protection Agency, Johnstown Castle, Co. Wexford',
     'url': 'https://www.epa.ie/publications/research/climate-change/research-305.php'},
         {'text': 'Black, K., Green, S., Mullooley, G., Poveda, A., 2014, Carbon Sequestration by Hedgerows in the Irtish Landscape, CCRP Report No. 32, Environmental Protection Agency, Johnstown Castle, Co. Wexford',
     'url': 'https://www.epa.ie/publications/research/climate-change/carbon-sequestration-by-hedgerows-in-the-irish-landscape.php'},
         {'text': 'Information about the National Forestry Service',
     'url': 'https://www.agriculture.gov.ie/forestservice/forestservicegeneralinformation/abouttheforestservice/'},
         {'text': 'National Forest statistics and mapping',
     'url': 'https://www.agriculture.gov.ie/forestservice/forestservicegeneralinformation/foreststatisticsandmapping/'},
         {'text': "Ireland's National Forest Inventory information",
     'url': 'https://www.agriculture.gov.ie/nfi/'},
         {'text': 'ESA CCI Biomass Products information',
     'url': 'http://cci.esa.int/biomass'},
         {'text': 'ESA’s Biomass satellite information',
     'url': 'https://www.esa.int/Applications/Observing_the_Earth/The_Living_Planet_Programme/Earth_Explorers/Biomass'},

]


###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Forestry Cover'
trendImg1 = IMAGES_PATH+'TerrestrialSections/IrelandNationalForestOwnership-1.png'
trendCaption1 = """
Map of forest cover in Ireland by ownership, 2017. Ref: National Forestry 
Service. Just over half (50.8%) of forests are in public ownership and the 
remainder (49.2%) are privately owned.
"""

trendChartTitle2 = 'Total Growing Stock Volume by Ownership'
trendChart2 = figure_4_17()
trendCaption2 = """
Total growing stock volume (million m\u00B3) by ownership (2006 to 2017). 
Growing stock volume increased by 38% over the period 2006–2017.
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
                dbc.Col(className="col-md-10 offset-md-1 col-lg-6 offset-lg-3",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children=trendChartTitle1),
                            html.Img(
                                className='w-100',
                                src=trendImg1
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
                                children=trendChartTitle2),
                            dcc.Graph(
                                figure=trendChart2,
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
            custom_trend,
        #     pb.build_trend(trendChartTitle,
        #                    trendChart,
        #                    trendCaption,
        #                    chapter_dict
        #                    ),
            custom_infrastructure,
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
