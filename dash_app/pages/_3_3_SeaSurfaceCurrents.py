import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_3_3

chapter_num = '3.3'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Currents_Tomasz Szumski_ADCP.jpg'
bannerImgCredit = 'Tomasz Szumski'

introText = """
    Ocean currents transport heat, salt, fresh water, carbon and ocean pollutants 
    from one part of the ocean to another and play a key role in determining climate 
    conditions and weather fluctuations. The Atlantic Meridional Overturning Circulation 
    (AMOC) and the North Atlantic Current, which is commonly known as the Gulf Stream, 
    form the main conveyor belt of relatively warm and saline subtropical waters 
    north-eastwards across the Atlantic Ocean. 
        """
bulletPoint1 = """
    Observations of the AMOC since 2004 indicate that it has weakened and it is predicted to continue weakening throughout this century.
        """
bulletPoint2 = """
    The lack of a sustained long-term ocean current monitoring system in Irish waters represents a significant gap in the North-east Atlantic.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """
    Schematic of the general circulation of the upper ocean (0-100m) in the North Atlantic. Ref: ICES Report on Ocean Climate 2018.   
        """

infrastructureText = """
    There are no permanent operational moored current meter arrays in the ocean area adjacent to Ireland. Large scale North Atlantic physical oceanographic studies are conducted annually by combining information from the scientific surveys of multiple countries.   Information on ocean currents is available from numerical models or, in the case of surface currents, from satellite estimations of sea level dynamics.  Validation is an essential step to verify the quality of the numerical models and to identify any limitations. Model validation can only be provided by the In-situ ocean observing system.
Regarding in situ current measurements   made by the Marine Institute, some examples where this is carried out include the Galway Bay Observatory and the M6 buoy. In addition, current measurements are routinely made by several ocean observing initiatives such as  the Argo programme (autonomous drifters; large scale circulation patterns) and deployment of Acoustic Doppler Current Profilers (ADCP ), at localised stations which  collect information on currents for research purposes. 
Globcurrent is an ESA funded project and is the main repository of quantitative estimations of surface currents based on several parameters derived from satellite sensor measurements. 

        """
infrastructureMap = map_3_3()

infoLinks = [
    {'text': 'Surface Currents ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/surface-currents/'},
         {'text': 'Sub-Surface Currents ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/subsurface-currents/ '},
         {'text': 'Holliday, N.P., Bersch, M., Berx, B. et al. (2020) Ocean circulation causes the largest freshening event for 120 years in eastern subpolar North Atlantic,  Nature Vol. 11, 585',
     'url': 'https://doi.org/10.1038/s41467-020-14474-y'},
         {'text': 'Annual ICES Report on Ocean Climate (IROC)',
     'url': 'https://ocean.ices.dk/iroc/#'},
         {'text': 'Information about Euro-Argo',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/oceanography/euro-argo'},
         {'text': 'Globcurrent Information',
     'url': 'http://www.globcurrent.org/'},
         {'text': 'Main ocean current pathways around Ireland available on Ireland´s Marine Atlas',
     'url': 'https://atlas.marine.ie/'},

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
                dbc.Col(className="col-md-10 offset-md-1 text-center",
                        children=[
                            html.H4(
                                className='sr-chart-title',
                                children='General Circulation of Upper Ocean'),
                            html.Img(
                                src=IMAGES_PATH+'OceanicSections/Figure3.6_CurrentLines.png')]
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
                                          trendCaption]
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
