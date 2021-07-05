import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_3_4, figure_3_5, map_3_2
import copy

chapter_num = '3.2'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Salinity_TomaszSzumski.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
Salinity is defined as the total amount of dissolved salts in water. 
These salts constitute approximately 3.5% of the ocean’s mass. Globally, 
areas that currently have net evaporation are expected to become saltier 
at the ocean surface, while areas with net precipitation, increased river 
un-off and land ice melt are expected to get fresher. Salinity and temperature 
control water density and are key variables for identifying and tracing 
ocean water masses and for understanding ocean physical processes. 
        """
bulletPoint1 = """
Decadal changes have taken place, and an unprecedented reduction in salinity 
levels has been observed in recent years in the North-east Atlantic, based on 
an analysis of 120 years of data.
        """
bulletPoint2 = """
Monitoring of changes in ocean salinity is an indirect method of detecting 
changes in precipitation, evaporation, river run-off and ice melt and therefore
 helps in understanding changes in the Earth’s hydrological cycle.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
Sea surface salinity measurements are made across the Irish Marine Data Buoy 
Observation Network (IMDBON) (orange and pink). Some subsurface salinity in 
Irish waters are made by the Marine Institute at the M6 buoy location (pink), 
at the Smart Bay Observatory (yellow) and since 2008 with underwater autonomous 
profilers as part of the Euro-Argo programme. 
In addition, the Marine Institute routinely collects and archives water 
salinity observations through several initiatives and projects and through 
ships working with CTD profilers . As part of Ireland’s Water Framework 
Directive monitoring programme salinity measurements are made by the 
Environmental Protection Agency in a number of estuaries and nearshore coastal 
waters. 
Sea-surface salinity can be monitored from space at a coarse spatial 
resolution following the launch of the ESA SMOS (Soil Moisture Ocean Salinity) 
mission in 2010 and NASA’s AQUARIUS mission in 2011. Both use sensors that 
detect microwave radiation emitted from the ocean surface from which salinity 
levels can be inferred. In situ measurements are required to validate these 
satellite-derived observations, especially in colder north Atlantic waters 
where there are still significant differences between the satellite derived.
        """
infrastructureMap = map_3_2()

infoLinks = [
    {'text': 'Surface Salinity ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-temperature/'},
         {'text': 'Subsurface Salinity ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/subsurface-salinity/'},
         {'text': 'Holliday, N.P., Bersch, M., Berx, B. et al. (2020) Ocean circulation causes the largest freshening event for 120 years in eastern subpolar North Atlantic. Nature Communications 11, 585: doi: 10.1038/s41467-020-14474-y',
     'url': 'https://www.nature.com/articles/s41467-020-14474-y'},
         {'text': 'Annual ICES Report on Ocean Climate (IROC)',
     'url': 'https://ocean.ices.dk/iroc/'},
         {'text': 'Marine Institute data portal',
     'url': 'http://data.marine.ie/'},
              {'text': 'Information from the Irish Marine Data Buoy Observation Network',
     'url': 'http://www.marine.ie/Home/site-area/data-services/real-time-observations/integrated-marine-observations'},
              {'text': 'Information about Euro-Argo',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/oceanography/euro-argo'},
              {'text': 'Information about Extended Ellett Line',
     'url': 'https://mars.noc.ac.uk/projects/extended-ellet-line'},
              {'text': 'Information about NASA Aquarius',
     'url': 'https://aquarius.oceansciences.org/cgi/gal_smap.htm'},
     {'text': 'Information about ESA SMOS',
     'url': 'https://earth.esa.int/web/guest/missions/esa-operational-eo-missions/smos'},              
     {'text': 'Water Quality in Ireland under the Water Framework Directive',
     'url': 'https://www.epa.ie/publications/monitoring--assessment/freshwater--marine/water-quality-in-ireland-2013-2018.php'},

]


###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)
combined_chapter_dict = copy.copy(chapter_dict)
combined_chapter_dict['title'] = 'Ocean Surface and Subsurface Salinity'

trendChartTitle1 = 'Upper Ocean Salinity - Rockall Trough'
trendChart1 = figure_3_4()
trendCaption1 = """
Mean annual upper ocean (top 800m) salinity in the North Rockall Trough (1975-2018). 
        """

trendChartTitle2 = 'Deep Ocean Salinity - Rockall Trough'
trendChart2 = figure_3_5()
trendCaption2 = """
Mean annual deep ocean salinity, at depths between 1,500 m and 2,000 m, in the North Rockall Trough (1975-2018). 
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
                            combined_chapter_dict
                            ),
            pb.build_breadcrumb(combined_chapter_dict),
            pb.build_nav(combined_chapter_dict),
            pb.build_intro(introText,
                           bulletPoints,
                           combined_chapter_dict
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
