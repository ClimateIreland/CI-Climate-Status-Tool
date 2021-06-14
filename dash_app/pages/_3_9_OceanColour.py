import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_20

chapter_num = '3.9'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Ocean Cover Tomasz Szumski_2.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
    Ocean colour refers to the sunlight reflected from the ocean surface. 
    This particular characteristic contains information on the constituents of the 
    sea water, in particular, phytoplankton pigments such as chlorophyll a (Chl-a), 
    suspended particles and dissolved organic compounds. Ocean colour monitoring 
    provides information on water quality and can assist by providing early warning 
    of potentially harmful phytoplankton blooms and pollution events.
        """
bulletPoint1 = """
    It is estimated that Chl-a concentrations in the North Atlantic have been increasing by 1.1% per year over the last 20 years. 
        """
bulletPoint2 = """
    Maximum Chl-a concentrations are generally reached in the March to May period and minimum values from October to December.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Monhtly Mean Chlorophyll-a Concentration - Irish Shelf'
trendChart = figure_3_20()

trendCaption = """
Monthly mean Chlorophyll-a concentration in the northeast Atlantic. Derived from the NASA Chlorophyll Concentration product determined from MODIS AQUA sensor observations. 
        """

infrastructureText = """
Satellite radiometers are used to observe ocean colour. Sensitive light sensors detect the small amounts of radiation reflected from the ocean surface in many narrow bands in the visible and near infrared spectrum. Analysis of the different amounts of reflectance in each band allows the characterisation of the ocean surface in terms of chlorophyll concentrations or sediment amounts or some specific dissolved organic compounds. 
The Marine Institute routinely obtains information from ESA and NASA on Ocean Colour and sea surface temperature. The chlorophyll-a (Chl-a) and sea surface temperature data provide information for the weekly reports that inform about potential development of toxic and/or harmful phytoplankton blooms. 

        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Ocean Colour ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ocean-colour/'},
         {'text': 'Satellite Ocean Colour: Current Status and Future Perspective, (2019) S, Sathyendranath, S., Ban, Y., et al.,   Frontiers in Marine Science, Ocean Observation, Vol. 6, 485: doi: 10.3389/fmars.2019.00485',
     'url': ''},
         {'text': 'Sathyendranath S., Brewin R.J.W., Brockmann C., et al. (2019) An Ocean-Colour Time Series for Use in Climate Studies: The Experience of the Ocean-Colour Climate Change Initiative (OC-CCI), Sensors, Vol. 19, No. 4285',
     'url': 'https://doi.org/10.3390/s19194285'},
         {'text': '-Von Schuckmann, K., P.-Y. Le Traon, N. Smith et al., (2020) Copernicus Marine Service Ocean State Report, Issue 4, Journal of Operational Oceanography, 13:sup1, s1–s172; ',
     'url': 'https://doi.org/10.1080/1755876X.2020.1785097'},
         {'text': 'MODIS and NASA data via Giovanni from the Goddard Earth Sciences and Information Services Centre',
     'url': 'https://giovanni.gsfc.nasa.gov/giovanni/'},
         {'text': 'Information and data from the Ocean Colour CCI Project',
     'url': 'https://www.oceancolour.org/about'},
         {'text': 'International Ocean Colour Coordinating Group',
     'url': 'https://ioccg.org/'},
         {'text': 'Marine Institute Weekly HAB Bulletin',
     'url': 'https://www.marine.ie/Home/site-area/data-services/interactive-maps/weekly-hab-bulletin'},
         {'text': 'Water Quality in Ireland under the Water Framework Directive',
     'url': 'http://www.epa.ie/pubs/reports/water/waterqua/waterqualityinireland2013-2018.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)


trendCaption2 = """
Average Chlorophyll-a concentration (mg/m3) for (a) March to May 2015 and (b) October to December 2015. Data Source: ESA CCI Ocean Colour Project.
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
                                    children='Average Chlorophyll-a Concentration'),
                                html.Img(src=IMAGES_PATH+'OceanicSections/CCI_OceanColour_2015.png')]
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
