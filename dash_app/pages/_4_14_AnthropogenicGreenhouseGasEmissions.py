import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_27, map_4_5

chapter_num = '4.14'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/GHG_EMissions_Metro Centric.jpg'
bannerImgCredit = 'Metro Centric'

introText = """
        Greenhouse gas emissions including carbon dioxide (CO\u2082), methane (CH\u2084), 
        and nitrous oxide (N\u2082O) from human (anthropogenic) activities such as 
        fossil fuel use, industry, agriculture and the waste sector continue to increase globally.  
        These gases reside in the atmosphere for a period from decades to thousands of years 
        and the increase in their concentrations is a cause of increase in surface temperature and climate change.       
        """
bulletPoint1 = """
        In 2018 in Ireland emissions from fossil fuel energy use were 18% higher 
        than in 1990 with emissions from agriculture having increased 2%.  
        Combined these represent over 87% of total emissions.
        """
bulletPoint2 = """
        Nitrous oxide emissions decreased by 10% over the period, mainly because of 
        reductions of synthetic fertiliser and animal manure use in agriculture.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'National Greenhouse Gas Emissions' #1990-2018
trendChart = figure_4_27()

trendCaption = """
National total Greenhouse Gas emissions by IPCC sectors (1990 – 2018).  
In 2018, total emissions of greenhouse gases were just over 65 ktCO\u2082 equivalent, 
which is 8% higher than emissions in 1990. An increasing trend in overall emissions 
is observed between 1990 and 2001, after which they slowly declined.
        """

trendChartTitle2 = 'Annual Cumulative CO\u2082 Flux - Dripsey, Co. Cork' 
trendChart2 = IMAGES_PATH+'TerrestrialSections/CO2_DripseyGrassland.png'

trendCaption2 = """
Above shows the cumulative CO\u2082 fluxes measured at the Dripsey grassland site for 
the period 2002–2012 when the flux tower was active. Negative values represent a 
net uptake of CO\u2082 (sink). This demonstrates that the grassland site was a net sink 
for CO\u2082 over the course of each year. However, there is seasonal variability. 
In the growing season (approximately March to September; day 60–250) there is a 
significant uptake of CO\u2082, whereas in the dormant season (approximately October to February), 
the grasslands are a source of CO\u2082.
"""
infrastructureText = """
Direct measurements of anthropogenic GHG emissions for Ireland, like many other countries, are limited. 
National estimations for reporting to the UNFCCC are based on a set of detailed guidelines provided by 
the Intergovernmental Panel on Climate Change (IPCC), the UN body for assessing the science related to climate change.  
At the local scale flux towers based on the eddy covariance method  are the most widely used approach to 
directly observing GHG fluxes between ecosystems and the atmosphere. As part of an EPA- and subsequently 
Council for Forest Research and Development-funded research project in the 2000s, GHG flux eddy covariance 
towers operated at Dripsey, Co. Cork (grassland and forest), Glencar, Co. Kerry (blanket peatland) and Wexford, Co. Wexford (grassland). 
These platforms are no longer operational. 
        """
infrastructureMap = map_4_5()

infoLinks = [
    {'text': 'Anthropogenic Greenhouse Gas Emissions  ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ghg-fluxes/'},

     {'text': 'Kiely, G., Leahy, P., Lewis, C., et al.,  (2018),  GHG Fluxes from Terrestrial Ecosystems in Ireland, EPA Report 227',
     'url': 'http://www.epa.ie/pubs/reports/research/climate/Research_Report_227.pdf'},

     {'text': 'Ireland’s National Inventory Report 2020',
     'url': 'http://www.epa.ie/pubs/reports/air/airemissions/ghg/nir2020/NIR%202020_Merge_finalv2.pdf'},


     {'text': 'Fluxnet information',
     'url': 'https://fluxnet.ornl.gov/fluxnetdb'},

     {'text': 'ICOS information',
     'url': 'https://www.icos-ri.eu/greenhouse-gases'},

     {'text': 'ESA’s Greenhouse Gases Climate Change Initiative',
     'url': 'http://cci.esa.int/ghg'},

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
                                style={"width":"100%","max-width":"800px"},
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
