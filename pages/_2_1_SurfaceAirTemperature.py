import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from charts import surfaceAirTempChart, surfaceAirTempStationsMap

# get relative data folder
PATH = pathlib.Path(__file__).parent
IMAGES_PATH=PATH.joinpath("../assets/images").resolve()


ecvName='Surface Air Temperature'
bannerImgSrc='assets/images/AtmosphericSections/AirTemp_MetEireann.jpg'
bannerImgCredit='Credit: Met Eirean'
ecvIconSrc='assets/images/icons/surface-temperature.png'

introText="""
        Surface air temperature is a key climate indicator and has widespread impacts 
        on natural systems and on human lives and activities. 
        It affects health, agriculture, energy demand and much more. 
        The global mean surface air temperature has increased on average by 0.85°C over 
        the last century, but the rate of warming has nearly doubled since 1975 to 
        almost 1.65°C per century.
        """
bulletPoint1="""
        In Ireland the annual average surface air temperature has increased by 
        approximately 0.9°C over the last 120 years
        """
bulletPoint2="""
        The number of warm spell days across Ireland has slightly 
        increased over the last 60 years.
        """

domain='Atmosphere'
subdomain='Surface'
scientificArea='Energy and Temperature'
authors='Walther C.A. Cámaro García, Ned Dwyer, Keith Lambkin'

trendChartTitle='Mean Surface Air Temperature (1900-2019)'
trendChart=surfaceAirTempChart()

trendCaption="""
        A time series graph of mean annual observed
        temperature for Ireland (1900-2011) (black dots) along 
        with simple statistical fits to the data.
        The left hand axis indicates anomalies (the difference 
        between the mean annual temperature and the 1961-1990 
        normal or reference mean value) and the right-hand axis 
        the mean annual temperature for the period. 
        The red line represents a simple linear trend which has been 
        fitted to the annual anomaly values while the blue curve shows 
        the 11-year moving average.
        """

infrastructureText="""
        Surface air temperature in Ireland is measured at 25 synoptic (red), 
        numerous climatological weather stations (blue) and more recently at weather marine weather 
        buoys (orange). The network of weather stations needs to be maintained and further developed 
        to ensure the future of long-term representative temperature measurements. 
        Difficulties arise because of inhomogeneities due to changes in instrumentation, observer, 
        location and times of observation and new building and tree growth in the vicinity of a station.
        """
infrastructureMap=surfaceAirTempStationsMap()

infoLinks=[{'text':'Surface Temperature ESSENTIAL CLIMATE VARIABLES (ECV). GCOS FACTSHEETS', 
            'url':'https://gcos.wmo.int/en/essential-climate-variables/surface-temperature/'},

            {'text':'ETCCDI/CRD Climate Change Indices. Definiiton of the 27 core indices', 
            'url':'http://etccdi.pacificclimate.org/list_27_indices.shtml'},

            {'text':'Met Eirean information on air temperature in Ireland', 
            'url':'https://www.met.ie/climate/what-we-measure/temperature'},

            {'text':'Met Eirean information on data availability', 
            'url':'https://www.met.ie/climate/available-data/'},
            
            {'text':'Information from the Irish Marine Weather Buoy Network', 
            'url':'http://www.marine.ie/Home/site-area/data-services/real-time-observations/irish-marine-data-buoy-observation-network'},

            {'text':'NOAA BAMS annual State of the Climate reports', 
            'url':'https://www.ncdc.noaa.gov/bams'},

            {'text':'WMO State of the Climate 2020 report', 
            'url':'https://public.wmo.int/en/our-mandate/climate/wmo-statement-state-of-global-climate'}
            ]



########################################################################################################################
domainColor=pb.domainColor(domain)
domainBGColor=pb.domainBGColor(domain)
      

def create_layout(app):
      return html.Div(children=[
        pb.build_banner(domain,
                        ecvName,
                        bannerImgSrc,
                        bannerImgCredit,
                        domainColor,
                        domainBGColor
                        ),
        pb.build_breadcrumb(ecvName, 
                     domainColor,
                     domainBGColor),
        pb.build_nav(domain,
                     domainColor,
                     domainBGColor),
        pb.build_intro(ecvName,
                       introText,bulletPoint1,
                       bulletPoint2,
                       ecvIconSrc,
                       domain,
                       subdomain,
                       scientificArea,
                       authors,
                       domainColor,
                       domainBGColor
                       ),
        pb.build_trend(trendChartTitle,
                       trendChart,
                       trendCaption,
                       domain,
                       domainColor,
                       domainBGColor
                       ),
        pb.build_infrastructure(infrastructureText,
                                infrastructureMap,
                                domain,
                                domainColor,
                                domainBGColor
                                ),
        pb.build_info(infoLinks,
                      domain,
                      domainColor,
                      domainBGColor)
                    ],)
