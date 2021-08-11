import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import figure_4_12


chapter_num = '4.7'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/FAPAR_ Vytenis Malisauskas.jpg'
bannerImgCredit = 'Vytenis Malisauskas'

introText = """
        Radiation from the sun plays an essential role in all biological process on Earth. 
        Part of this radiation is absorbed by vegetation and provides the energy required for growth. 
        This radiation is called FAPAR or the Fraction of Absorbed Photosynthetically Active Radiation. 
        """
bulletPoint1 = """
        The highest photosynthetic activity over Ireland is observed from May to July. 
        Western margins of the country show the lowest values of FAPAR.
        """
bulletPoint2 = """
        A ground-based FAPAR observation system should be considered in order to 
        validate and support satellite observations.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
# domain='Terrestrial'
# subdomain='Biology'
# scientificArea='Biosphere'
# authors='Walther C.A. Cámaro García, Ned Dwyer'

trendChartTitle = 'Mean 10-Day FAPAR - Ireland'
trendChart = figure_4_12()

trendCaption = """
Heat map of 10-day averaged FAPAR over Ireland derived from the Copernicus Global Land Services (CGLS) dataset (1999-2018). 
The data is presented as percentiles calculated using the complete dataset. For example, the 75th percentile means that 75% of all 
the values are below 0.72 and 25% of the values are above it. A seasonal trend is observed, where the highest values occur during summer, 
particularly in June, when vegetation tends to have higher photosynthetic activity, whilst the lowest values are observed during winter months. 
The highest values in the time series are in the summer periods between 2007 and 2009, and between 2013 and 2017.
        """

infrastructureText = """
FAPAR is challenging to measure on the ground in tall and heterogeneous vegetation environments. 
Measurements tend to be made at the local scale and for research studies and are labour intensive. 
There is no long-term in situ FAPAR monitoring programme in Ireland. Regional FAPAR estimates are 
generally based on observations from satellite sensors, which have the ability to measure the visible 
and infrared radiation reflected by the Earth’s surface on a regular basis. The CGLS generates a 
FAPAR dataset as part of a set of vegetation monitoring products.
        """

# no map
# infrastructureMap=surfaceAirTempStationsMap()

infoLinks = [
    {'text': 'FAPAR ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/fapar/'},
    {'text': 'Copernicus Global Land Service (CGLS) data',
     'url': 'https://land.copernicus.eu/global/products/fapar'},
    {'text': 'Copernicus vegetation phenology and productivity product',
     'url': 'https://land.copernicus.eu/pan-european/biophysical-parameters/high-resolution-vegetation-phenology-and-productivity'},
    {'text': 'Joint Research Centre (JRC) FAPAR project',
     'url': 'https://fapar.jrc.ec.europa.eu/Home.php'},
    {'text': 'Sentinel Global Vegetation Index (FAPAR) description',
     'url': 'https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-3-olci/level-2/olci-global-vegetation-index-fapar'},
]

######################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)


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


########################################################################################################################


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
            pb.build_trend(trendChartTitle,
                           trendChart,
                           trendCaption,
                           chapter_dict
                           ),
            # pb.build_infrastructure(infrastructureText,
            #                         infrastructureMap,
            #                         chapter_dict
            #                         ),
            custom_infrastructure,
            pb.build_info(
                infoLinks,
                chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
