import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_24, figure_3_25

chapter_num = '3.11'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Habitats_Tomasz_Szumski_IMG_9140_biodiscovery survey 2014.jpg'
bannerImgCredit = 'Marine Institute'

introText = """
Seaweed, seagrass and coral abundance and condition are good indicators of 
marine health and are essential elements of the marine environment. As well as 
playing a role in the carbon cycle they provide crucial habitats for many fish,
 crustaceans and other species. However, they are under constant transformation
  in response to human activities and global change. 
        """
bulletPoint1 = """
More than 1000 species of algae have been identified in Irish waters, some of 
which are invasive causing economic and environmental impacts.  
        """
bulletPoint2 = """
Seagrass is found close to coasts and is very vulnerable to human actions. 
It is estimated that almost 30% of seagrass meadows globally have died off over
 the last century. Surveys in Ireland since 2006 suggest an increase in the 
 presence of seagrass in most sites monitored. 
        """

bulletPoint3 = """
Deep-water or cold-water corals are found on parts of the continental slope to 
the west of Ireland at water depths ranging between 600 m and 1000 m, and 
worldwide they are found at depths of up to 2000 m.
        """

bulletPoints = [bulletPoint1, bulletPoint2,bulletPoint3]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
As part of Ireland’s monitoring programme under the Water Framework Directive, macroalgae (seaweed) and seagrass communities are used as measures of biological quality and health in estuaries and coastal waters.  Macroalgal quality is assessed   by looking at seaweed diversity on rocky shores, and green algal growth.    Intertidal seagrass communities, which are a protected habitat, have been monitored by the EPA since 2007. 
 As part of a National Parks and Wildfire Service (NPWS) commissioned survey of the abundance and distribution of offshore cold-water reef habitat a set of coral habitat types has been identified on the Irish shelf, based on underwater observations from Remotely Operated Vehicles (ROV). These include cold-water coral reefs, coral gardens and sea-pen fields. Records of the samples have been included in the Vulnerable Marine Ecosystems (VMEs) database of the International Council for the Exploration of the Sea (ICES). 
A number of areas where deep-water corals were identified have been designated as   Special Areas of Conservation (SACs) by the NPWS.   
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Marine Habitat Properties ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/marine-habitats/'},
         {'text': 'WFD coastal sites (Water Quality in Ireland under the Water Framework Directive)',
     'url': 'https://www.catchments.ie/water-quality-in-ireland-2013-2018/ '},
         {'text': 'NPWS Special Areas of Conservation (SAC)',
     'url': 'https://www.npws.ie/protected-sites/sac'},
         {'text': 'ICES Vulnerable Marine Ecosystems',
     'url': 'https://www.ices.dk/marine-data/data-portals/Pages/vulnerable-marine-ecosystems.aspx'},
         {'text': 'de los Santos, Krause-Jensen, D., Alcoverro, T., et al., (2019) Recent trend reversal for declining European seagrass meadows.  Nature Communications Vol. 10, 3356',
     'url': 'https://doi.org/10.1038/s41467-019-11340-4'},
         {'text': 'Wilkes. R, Bennion, M., McQuaid, N., et al. (2017). Intertidal seagrass in Ireland: Pressures, WFD status and an assessment of trace element contamination in intertidal habitats using Zostera noltei, Ecological Indicators Vol. 82, pp 117-130',
     'url': 'https://doi.org/10.1016/j.ecolind.2017.06.036'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Intertidal Seagrass Sites'
trendChart1 = figure_3_24()
trendCaption1 = """
Distribution of intertidal seagrass sites and their trajectories since 2006. 
An increase in the presence of seagrass is observed in most sites, except for 
the Moy estuary, Co. Mayo, and those in Northern Ireland. 
        """

trendChartTitle2 = 'Special Areas of Conservation and Vulnerable Marine Ecosystems'
trendChart2 = figure_3_25()
trendCaption2 = """
Location of the Special Areas of Conservation (SAC) where deep-water corals 
have been identified (pink polygons) and location of vulnerable marine 
ecosystems (VME) as defined by ICES (coloured points). 
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
                                    children=trendChartTitle1),
                                dcc.Graph(
                                    figure=trendChart1,
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
            )])

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
        #     pb.build_infrastructure(infrastructureText,
        #                             infrastructureMap,
        #                             chapter_dict
        #                             ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
