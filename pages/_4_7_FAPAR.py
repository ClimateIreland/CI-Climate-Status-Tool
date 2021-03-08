import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import FAPARTrend, surfaceAirTempStationsMap


chapter_num='4.7'
bannerImgSrc=IMAGES_PATH+'TerrestrialSections/FAPAR_ Vytenis Malisauskas.jpg'
bannerImgCredit='Vytenis Malisauskas'

introText="""
        Radiation from the sun plays an essential role in all biological process on Earth. 
        Part of this radiation is absorbed by vegetation and provides the energy required for growth. 
        This radiation is called FAPAR or the Fraction of Absorbed Photosynthetically Active Radiation. 
        """
bulletPoint1="""
        The highest photosynthetic activity over Ireland is observed from May to July. 
        Western margins of the country show the lowest values of FAPAR.
        """
bulletPoint2="""
        A ground-based FAPAR observation system should be considered in order to 
        validate and support satellite observations.
        """
bulletPoints=[bulletPoint1,bulletPoint2]
# domain='Terrestrial'
# subdomain='Biology'
# scientificArea='Biosphere'
# authors='Walther C.A. Cámaro García, Ned Dwyer'

trendChartTitle='10-day average FAPAR over Ireland'
trendChart=FAPARTrend()

trendCaption="""
           Above shows a heat map of 10-Day averaged FAPAR derived over Ireland using the CGLS dataset. 
           The red colour represents the 10-day periods with the highest values; only 5% of the values 
           are at or above the threshold of 0.76 (the 95th percentile). A seasonal trend is observed,
            where the highest values occur during summer, particularly in June, when vegetation tends 
            to have higher photosynthetic activity, whilst the lowest values are observed during winter months. 
            The highest values in the time series are in the summer periods between 2007 and 2009, and between 2013 and2017. 
        """

infrastructureText="""
        The CGLS is one of the Copernicus services that provide satellite information that may 
        be used to monitor a number of vegetation parameters around the globe. 
        The global FAPAR dataset available is derived from several satellite sensors. Currently, 
        the CGLS team is updating the dataset based on SENTINEL-3 OLCI and SLSTR sensors as new data sources. 
        Comprehensive analysis of satellite-derived FAPAR spatio-temporal trends for Ireland needs to be carried out. 
        A ground-based observation system should also be considered in order to validate and support the satellite observations. 
        """
infrastructureMap=surfaceAirTempStationsMap()

infoLinks=[
        {'text':'FAPAR ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS', 
            'url':'https://gcos.wmo.int/en/essential-climate-variables/fapar/'},
                {'text':'Copernicus Global Land Service (CGLS) data', 
            'url':'https://land.copernicus.eu/global/products/fapar'},
                {'text':'Copernicus vegetation phenology and productivity product', 
            'url':'https://land.copernicus.eu/pan-european/biophysical-parameters/high-resolution-vegetation-phenology-and-productivity'},
                {'text':'Joint Research Centre (JRC) FAPAR project', 
            'url':'https://fapar.jrc.ec.europa.eu/Home.php'},
                {'text':'Sentinel Global Vegetation Index (FAPAR) description', 
            'url':'https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-3-olci/level-2/olci-global-vegetation-index-fapar'},
            ]

######################################################################################################################
chapter_dict=next((item for item in CHAPTERS if item['chapter-num']==chapter_num),None)


custom_infrastructure = dbc.Container(
        className='sr-infrastructure',
        style={'borderColor':chapter_dict['domain-color']},
        id='infrastructure',
        children=[
            html.H3(
                className='sr-section-heading',
                children='Observation Infrastructure',
                style={'color':chapter_dict['domain-color']},
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
