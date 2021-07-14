import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_4, figure_4_5, map_4_4

chapter_num = '4.4'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Soil_Moisture_Ned_DwyerP1090366.JPG'
bannerImgCredit = 'Ned Dwyer'

introText = """
Soil moisture comprises only a tiny percentage of the total global water 
budget, but it has a key role in influencing the hydrological cycle and is a 
major driving force in the soil’s ability to act as a carbon sink or source. 
Soil moisture content refers to the amount of water held in the soil and is 
affected by the soil texture, topography, land cover and weather conditions. 
Both local climate and vegetation influence soil moisture through 
evapotranspiration.
        """
bulletPoint1 = """
Soil moisture is a determinant of the type and conditions of vegetation in a 
region, and it is an important measure for agriculture, as it affects the 
length of the grazing season, grass and crop growth rates and nutrient uptake 
and loss.
        """
bulletPoint2 = """
Soil moisture deficits calculated at Dublin Airport in June and July 2018 were 
the highest since records began in 1981. 
        """
bulletPoint3 = """
In general, the greatest soil moisture deficits are seen in the east and 
south-east of the country.
        """
bulletPoints = [bulletPoint1, bulletPoint2, bulletPoint3]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
There are direct and indirect methodologies to measure soil moisture. However, 
these measurements are only representative of local conditions and direct 
methodologies require intensive labour. Currently in Ireland only indirect 
methods are operationally used. 
Met Éireann has estimated the daily soil moisture deficits (SMD) at many of 
its synoptic stations since 1980. These are modelled values based on 
the difference between rainfall amount and actual evapotranspiration and are 
estimated separately for poorly, moderately and well drained soils.
A number of satellite sensors make broad-scale measurements of soil moisture. 
The ESA CCI Soil Moisture project has developed one of the most comprehensive 
global time series of satellite derived soil moisture.   
        """
infrastructureMap = map_4_4()

infoLinks = [
    {'text': 'Soil Moisture ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/soil-moisture'},
     {'text': 'Schulte, R.P.O. et al., 2005. Predicting the soil moisture conditions of Irish grasslands. Irish Journal of Agricultural and Food Research 44: 95–110',
     'url': 'https://t-stor.teagasc.ie/handle/11019/464'},
     {'text': 'Gruber, A. et al., 2019. Evolution of the ESA CCI Soil Moisture climate data records and their underlying merging methodology. Earth System Science Data 11: 717–739.',
     'url': 'https://doi.org/10.5194/essd-11-717-2019 '},
     {'text': 'Met Éireann historical data',
     'url': 'https://www.met.ie/climate/available-data/historical-data'},
     {'text': 'Met Éireann information on soil moisture deficit estimation',
     'url': 'https://www.met.ie/climate/services/agri-meteorological-data'},
     {'text': 'ESA Climate Change Initiative soil moisture products data',
     'url': 'http://www.esa-soilmoisture-cci.org/'},
     {'text': 'Met Éireann reports 2018 as a summer heatwaves and droughts',
     'url': 'https://www.met.ie/2018-a-summer-of-heat-waves-and-droughts'},
     {'text': 'International Soil Moisture Network',
     'url': 'https://ismn.geo.tuwien.ac.at/en/'},
     {'text': 'The GROW Observatory project',
     'url': 'https://growobservatory.org/'},
     {'text': 'Information about the Joint Working Group on Applied Agricultural Meteorology ',
     'url': 'https://agmet.ie/about/'},
]

###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

trendChartTitle1 = 'Average Daily Soil Moisture Deficits'
trendChart1 = figure_4_4()
trendCaption1 = """
Average daily soil moisture deficit calculated at Valentia Observatory and 
Dublin Airport (1980–2019).
The greatest SMDs, which usually occur in the summer and when sustained can be 
indicative of droughts, generally occur in the east and south-east of the country.  
        """

trendChartTitle2 = 'Mean Monthly Soil Moisture Deficit, SMD - Dublin Airport'
trendChart2 = figure_4_5()
trendCaption2 = """
Mean monthly surface soil moisture deficit as derived from measurements at Dublin 
Airport. The data is presented as percentiles. For example, the 75th 
percentile means that 75% of all the values are below the corresponding values 
and 25% of the values are above it.
The consecutive red values during summer 2018, with June and July being the 
highest values of all in the time series, are in line with the heatwave and 
drought conditions experienced during that summer.
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
