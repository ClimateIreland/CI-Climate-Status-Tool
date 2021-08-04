import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_25, figure_2_26, map_2_13

chapter_num = '2.13'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Ozone_MetEireann.jpg'
bannerImgCredit = 'Met Éireann'

introText = """
Ozone (O\u2083) is another potent greenhouse gas in terms of radiative forcing.
 The influence of O\u2083 on climate is complex, with different impacts in the upper
  and lower atmosphere. It also has multiple potential environmental and health
   impacts. In the upper atmosphere (stratosphere) it prevents harmful 
   ultraviolet radiation from reaching the Earth’s surface. In the lower 
   atmosphere (troposphere) it is a pollutant, harmful to all living things. 
        """
bulletPoint1 = """
The implementation of the internationally agreed Montreal Protocol (1987) has 
been effective in reducing the production of O\u2083 depleting substances and 
gradually restoring stratospheric O\u2083 concentrations.
        """
bulletPoint2 = """
At Mace Head average annual near-ground O\u2083 amounts increased over the 
period 1987–1997, followed by a step change during 1998/1999 and relatively 
constant levels since then.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
The Environmental Protection Agency (EPA), through the national ambient air 
quality monitoring network, is in charge of the ground based O\u2083 
measurements. 
Eleven of these stations are directly operated by the EPA (green); Valentia 
Observatory, Co. Kerry (red) is operated by Met Éireann;  Mace Head, 
Co. Galway (black) is operated by the National University of Ireland Galway 
(NUI Galway) and the remaining stations are operated by local authorities 
(yellow) or by universities and research initiatives (orange).
Total column and stratospheric O\u2083 has been measured at Valentia Observatory 
since 1993, providing continuous data for more than twenty-five years. These 
measurements are routinely made using equipment carried on weather balloons to 
heights greater than 30 km.
Measurements of O\u2083 from satellites have been made since the 1970s with 
different sensors operating in the ultraviolet, visible and microwave part of 
the spectrum.
        """
infrastructureMap = map_2_13()

infoLinks = [
    {'text': 'Ozone Properties ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS.',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ozone'},
         {'text': 'EPA Air Quality Monitoring Network  information',
     'url': 'https://www.epa.ie/air/quality'},
         {'text': 'National Ambient Air Quality Monitoring Programme 2017-2022',
     'url': 'https://www.epa.ie/publications/monitoring--assessment/air/national-ambient-air-quality-monitoring-programme-2017-2022.php'},
         {'text': 'A description of the Ozone Measurement Programme at Valentia Observatory',
     'url': 'https://www.met.ie/science/valentia/ozone-monitoring'},
         {'text': 'Information on the Mace Head Facility',
     'url': 'http://www.macehead.org'},
         {'text': 'Copernicus Atmospheric Monitoring Service',
     'url': 'https://www.copernicus.eu/en/services/atmosphere'},
         {'text': 'Copernicus Climate Change Service',
     'url': 'https://www.copernicus.eu/en/services/climate-change'},
        {'text': 'ESA Sentinel 5P Mission',
     'url': 'https://earth.esa.int/web/guest/missions/esa-eo-missions/sentinel-5p'},
        {'text': 'NASA Ozone Watch (Ozone Maps)',
     'url': 'https://ozonewatch.gsfc.nasa.gov/monthly/NH.html'},

]


###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Ground-level Ozone Concentration - Mace Head'
trendChart1 = figure_2_25()
trendCaption1 = """
Monthly mean ground-level ozone concentration observed at Mace Head (1987–2018).
 The sharp increase in 1998/1999 has been attributed to large vegetation fires 
 in the northern hemisphere during that period.  
        """

trendChartTitle2 = 'Total Column Ozone Concentration - Valentia'
trendChart2 = figure_2_26()
trendCaption2 = """
Monthly mean total column ozone concentration (in Dobson Units) observed at 
Valentia Observatory (1993–2019). No trend is apparent over the period.  
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
