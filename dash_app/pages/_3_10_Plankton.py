import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_3_8

chapter_num = '3.10'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Plankton_Marine_Institute_1.ligulodinium polyedrum_2.jpg'
bannerImgCredit = 'Marine Institute'

introText = """
    Plankton are at the base of the marine food web and are classified into two main categories: 
    the phytoplankton formed by free-floating plants and the zooplankton formed mainly 
    by microscopic animals. Changes in plankton affect marine ecosystems, 
    living marine resources used by humans and the carbon cycle. Plankton play a key 
    role in climate regulation, as they sequester CO2 at the surface and transfer 
    it to the deep ocean. 
        """
bulletPoint1 = """
    The  abundance of non-toxic plankton species in the Celtic Sea has been decreasing over time in the period 1958 to 2014.
        """
bulletPoint2 = """
    Since 2010 the presence of some potentially harmful phytoplankton has frequently been detected all year round in Irish waters.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
The Marine Institute has been monitoring phytoplankton since the 1980s.  Phytoplankton analysis has focussed on the phytoplankton populations and dynamics from aquaculture sites around the Irish coastline (blue), with special attention to the harmful and toxic phytoplankton (map 3.8). At well-mixed shallow sites, surface seawater samples are collected while at deeper sites an integrated seawater sample from the water column is collected and analysed on a weekly basis.
As part of the Ireland’s Water Framework Directive monitoring programme, monthly Phytoplankton measurements in coastal waters and seasonal sampling in estuaries have been made (red) by the Marine Institute and EPA. 
Continuous Plankton Recorder (CPR) surveys are established in several areas around the world including the North Atlantic Ocean since 1931. In this area the programme is coordinated by the UK´s Marine Biological Association (MBA) with a set of voluntary observing ships undertaking regular plankton tows. Currently these are the only systematic measurements of zooplankton taken in parts of the Irish Shelf. 
Measurements from a number of satellite sensors that detect radiation reflected from the ocean surface (ocean colour) are used to infer chlorophyll and hence phytoplankton concentrations. Observations are available from various satellite sensors going back to the late 1980s. Currently information on chlorophyll concentrations can be retrieved from the Copernicus Marine service and the ESA-CCI-Ocean Colour project.

        """
infrastructureMap = map_3_8()

infoLinks = [
    {'text': 'Plankton ESSENTIAL CLIMATE VARIABLE (ECV) GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/plankton/'},
         {'text': '-	Edwards, M., Helaouet,P., Alhaija, R.A., et al., (2016) Global Marine Ecological Status Report: results from the global CPR Survey 2014/2015. SAHFOS Technical Report, No. 11: 1-32. Plymouth, U.K. ISSN 1744-0750',
     'url': 'https://www.cprsurvey.org/publications/scientific-reports/ecostatus-reports/'},
         {'text': 'Marine Institute Phytoplankton programme information',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/marine-environment/phytoplankton-monitoring'},
         {'text': 'WFD coastal sites(Water Quality in Ireland under the Water Framework Directive)',
     'url': 'http://www.epa.ie/pubs/reports/water/waterqua/waterqualityinireland2013-2018.html'},
         {'text': 'Information about the MBA CPR Surveys',
     'url': 'https://www.cprsurvey.org/'},
]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendCaption1 = """
Percentage of monthly samples analysed between 1990 – 2018 where Karenia mikimotoi was detected. 
        """

trendCaption2 = """
Annual mean abundance expressed as anomalies above and below the long term mean for a number of plankton life-forms (functional group) from 1958-2014 for the Celtic Sea. Ref: Global Marine Ecological Status Report, results from the global CPR Survey 2014/2015. SAHFOS Technical Report, 11: 1-32.
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
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='Percentage of Coastal Water Containing Harmful Microalga'),
                            html.Img(
                                src=IMAGES_PATH+'OceanicSections/Figure3.22_PercentageMonthlySamplesKareniaMikimotoiDetected..png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
                        children=[
                            html.P(
                                className='sr-chart-caption',
                                children=[html.I(className="fas fa-play _up",
                                                 style={"color": chapter_dict['domain-color']}),
                                          trendCaption1]
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
                                children='Annual Mean Abundance of Plankton in the Celtic Sea'),
                            html.Img(
                                src=IMAGES_PATH+'OceanicSections/Figure3.23_ZooplanktonConcentration.png')]
                        )
            ]
        ),
        dbc.Row(
            children=[
                dbc.Col(className="col-md-10 offset-md-1",
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
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
