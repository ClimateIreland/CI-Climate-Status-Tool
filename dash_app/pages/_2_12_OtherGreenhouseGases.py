import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, figure_2_22, figure_2_23, figure_2_24, map_2_12

chapter_num = '2.12'
bannerImgSrc = IMAGES_PATH+'AtmosphericSections/Other_GHG_IMG_3709 Hester Whyte.JPG'
bannerImgCredit = 'Hester Whyte'

introText = """
In addition to water vapour, carbon dioxide (CO\u2082) and methane (CH\u2084), 
a number of other gases contribute significantly to the enhanced greenhouse effect.  
These include nitrous oxide (N\u2082O) which has a global warming potential 265 times that of 
CO\u2082 and synthetic gases which are exclusively produced by human activities but have extremely high global warming potentials.
        """
bulletPoint1 = """
        N\u2082O concentrations in the atmosphere are now approximately 20% 
        higher compared to the pre-industrial era.  
        """
bulletPoint2 = """
        Synthetic gasses, which replaced ozone depleting chlorofluorocarbons 
        (CFCs) are increasing steadily in the atmosphere.
        """
bulletPoints = [bulletPoint1, bulletPoint2]

# first chart
trendChartTitle = 'Mean Monthly Nitrous Oxide (N\u2082O) Concentration' #(1978-2018)
trendChart = figure_2_22()
trendCaption = """
Monthly mean N\u2082O concentration observed at Adrigole (1978-1984) and Mace Head Research Station (1987–2018). 
A steady increase is observed, with concentrations now above 330 ppb. 
This is a 20% increase compared to the pre-industrial era when N\u2082O global concentrations were around 270 ppb.
        """
# second chart
trendChartTitle2 = 'Mean Monthly CFC-12 Concentration' #(1978-2018)
trendChart2 = figure_2_23()
trendCaption2 = """
Monthly mean CFC-12 concentration observed at Adrigole (1978-1984) and Mace Head Research Station (1987–2018).  
A steady increase can be observed through the 1980s but, after the adoption of the Montreal Protocol in 1987, 
banning the production and use of CFCs, there was no further increase and levels have been falling since 2004.
        """
# third chart
trendChartTitle3 = 'Mean Monthly HFC-134a Concentration' #(1994-2018)
trendChart3 = figure_2_24()
trendCaption3 = """
Monthly mean HFC-134a concentration observed at Mace Head Research Station (1994-2018).
 This synthetic gas is a good example of the refrigerant products that replaced ozone-depleting CFCs. 
 It is also used in mobile air-conditioning units and as a fire retardant. Its concentration is increasing steadily, 
 as is that of a number of other synthetic gases in the atmosphere.
        """

infrastructureText = """
Greenhouse gas concentrations have been measured routinely at the Mace Head Atmospheric Research Station, 
Carna, Co. Galway (red), since the 1990s. Monitoring of a number of HFC and HCFC compounds started in 1994 
and of PFCs and SF\u2086 in 2004. N\u2082O and CFCs were measured at Adrigole, Co. Cork (blue), from 1978 to 1984.
        """
infrastructureMap = map_2_12()

infoLinks = [
    {'text': 'Carbon Dioxide, Methane & Other Greenhouse Gases ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/ghg/'},
     {'text': 'Simmonds, P.G., M. Rigby, A. McCulloch, et al., (2017) Changing trends and emissions of hydrochlorofluorocarbons (HCFCs) and their hydrofluorocarbon (HFCs) replacements. Atmospheric Chemistry and Physics. Vol. 17, pp. 4641-4655',
     'url': 'https://doi.org/10.5194/acp-17-4641-2017'},
     {'text': 'Information on the Mace Head Facility',
     'url': 'http://www.macehead.org/'},
     {'text': 'GHG observations from Mace Head and other AGAGE observatories',
     'url': 'https://agage.mit.edu/'},
     {'text': 'Information about the Montreal Protocol',
     'url': 'https://www.unenvironment.org/ozonaction/who-we-are/about-montreal-protocol'},
     {'text': 'ESA Sentinel 5P Mission',
     'url': 'https://sentinel.esa.int/web/sentinel/missions/sentinel-5p'},
     {'text': 'NASA’s Aura Spacecraft',
     'url': 'https://aura.gsfc.nasa.gov/omi.html'},
     {'text': 'Integrated Carbon Observation System (ICOS)',
     'url': 'https://www.icos-cp.eu/'},

]


########################################################################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)

custom_trend =  dbc.Container(
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
                                    children=[html.I(className="fas fa-play _up",
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
                                    children=trendChartTitle2),
                                dcc.Graph(
                                    figure=trendChart2,
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
                                            children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption2]
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
                                    children=trendChartTitle3),
                                dcc.Graph(
                                    figure=trendChart3,
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
                                            children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption3]
                                )]
                            )
                ]
            ),
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
            custom_trend,
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
