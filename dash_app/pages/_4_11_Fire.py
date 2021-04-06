import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_4_22

chapter_num = '4.11'
bannerImgSrc = IMAGES_PATH+'TerrestrialSections/Fires_CiaranNugent.jpg'
bannerImgCredit = 'Ciaran Nugent'

introText = """
        Land cover - the observed (bio)-physical cover on the Earth’s surface, 
        including grassland, forest, built environment, etc. 
        – plays a key role in climate dynamics such as water and energy exchanges 
        between the ground and the atmosphere, and contributes to the capture 
        and release of greenhouse gases and aerosols.  
        """
bulletPoint1 = """
        Peatlands represent almost 14% of Irish land cover and are an 
        essential feature in the regulation of the climate by removing carbon
        """
bulletPoint2 = """
        Land cover observations since 1990 show increases in the area covered 
        by artificial surfaces and forests and a decrease in wetland areas which include peatlands.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = 'Very High or Extreme Fire Danger'
trendChart = figure_4_22()

trendCaption = """
Number of days on which the fire index was very high or extreme as 
calculated using data from Dublin airport and Shannon airport synoptic stations (1971–2018).
        """

infrastructureText = """
Data on vegetation fires are generally not compiled centrally by the fire services, however burned area estimates, based on assessments of known fires are generated for reporting by the Department of Agriculture, Fisheries and the Marine (DAFM) to the European Commission annually. 
Daily fire risk is assessed by Met Éireann using meteorological variables derived using the Canadian Fire Weather Index (FWI), and fire danger notices are issued to forestry interests by DAFM throughout the fire season. 
Satellite data are used internationally to make regional and global estimates of fire disturbance and their impact on the atmosphere and some research studies have been carried out on their utility over Ireland, However, frequent cloud cover, the short duration of fire events and low heat signature of typical fires limit detection rates and the small size of many burnt land parcels reduce the usefulness of satellite imagery under Irish conditions. 
        """
infrastructureMap = empty_chart()

infoLinks = [
    {'text': 'Fire ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/fire/'},

     {'text': 'Prat-Guitart, N.; Nugent, C.; Mullen, E.; et al. (2019) Peat Fires of Ireland. In Coal and Peat Fires: A Global Perspective; Stracher, G.B., Prakash, A., Sokol, E.V., Eds.;Elsevier Inc.: Amsterdam, The Netherlands, Vol. 5, pp. 451–482',
     'url': 'https://doi.org/10.1016/C2016-0-02048-X'},

     {'text': 'Annual Reports on Forest Fires in Europe Middle East and North Africa',
     'url': 'https://effis.jrc.ec.europa.eu/reports-and-publications/annual-fire-reports'},

     {'text': 'Global Wildfire Information System',
     'url': 'https://gwis.jrc.ec.europa.eu/apps/gwis_current_situation/'},

     {'text': 'Fire, Land and Atmospheric Remote Sensing of Emissions (FLARES) project',
     'url': 'https://www.ucc.ie/en/eri/projects/flares--fire-land-and-atmospheric-remote-sensing-of-emissions.html'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)


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
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
