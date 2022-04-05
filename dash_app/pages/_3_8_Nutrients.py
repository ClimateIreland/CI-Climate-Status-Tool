import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib
import page_builder as pb
from settings import *
from charts import empty_chart, map_3_7

chapter_num = '3.8'
bannerImgSrc = IMAGES_PATH+'OceanicSections/Nutrients_Tomas Szumski_167.JPG'
bannerImgCredit = 'Tomasz Szumski'

introText = """
The major nutrients, such as dissolved inorganic phosphorus, nitrogen and silicon, 
play a key role in ocean life. They are essential for plant growth (e.g. 
phytoplankton, algae) at the base of the food web and when depleted can limit 
growth. In excess, they can cause eutrophication, whereby accelerated algal 
growth can lead to depletion of oxygen and result in severe ecological harm. 
        """
bulletPoint1 = """
Nutrient concentrations in Irish waters are determined by natural dynamics and 
the seasonal variability in the growth of phytoplankton and macroalgae; they 
are also influenced by riverine and atmospheric inputs from human activities – 
for example agricultural application of fertiliser and municipal waste discharges. 
        """
bulletPoint2 = """
Locations with elevated nitrogen concentrations linked to sources of pollution 
are generally found on the south and east coasts of Ireland.
        """
bulletPoints = [bulletPoint1, bulletPoint2]
trendChartTitle = ''
trendChart = empty_chart()

trendCaption = """

        """

infrastructureText = """
As part of Ireland’s Water Framework Directive monitoring programme, nutrient 
measurements, mainly nitrogen and phosphorus, have been made regularly in 116 
transitional and coastal water bodies (green) since 2007.
The Marine Institute operate a programme to take measurements of nutrients in 
Irish coastal, shelf and offshore waters (orange). 
To assess spatial and temporal trends in surface waters, inorganic nutrients 
are best measured during winter, when nutrient uptake by marine plants is at a 
minimum and there is a well-mixed water column. Since the 1990s, annual 
ship-based surveys, from the RV Celtic Voyager, have sampled for winter 
nutrients initially in the western Irish Sea and gradually extended to cover 
the entire coast and include transects further onto the shelf.  
Additionally, since 2008 on board the RV Celtic Explorer during the annual 
Rockall Ocean Climate hydrographic survey, dissolved inorganic nutrients are 
measured along the Irish shelf (53°N) and to full water depth on a 
cross-section of the Rockall Trough. However, winter sampling has been heavily 
constrained by poor weather conditions during recent years. The 2019 survey was
 during summer months. 
As part of ongoing research projects, observations are made at the Mace Head 
observatory and at the SmartBay Observatory (yellow) with a nitrate sensor 
deployed at the Mace Head mooring (red). 

        """
infrastructureMap = map_3_7()

infoLinks = [
    {'text': 'Nutrients ESSENTIAL CLIMATE VARIABLE (ECV). GCOS FACTSHEETS',
     'url': 'https://gcos.wmo.int/en/essential-climate-variables/nutrients/'},
         {'text': 'Marine Institute Nutrients information',
     'url': 'https://www.marine.ie/Home/site-area/areas-activity/marine-environment/nutrients-and-ocean-acidification-oa'},
         {'text': 'Information about ICES',
     'url': 'https://www.ices.dk/'},
         {'text': 'The GO-SHIP programme',
     'url': 'https://www.go-ship.org/About.html'},
         {'text': 'The Marine Institute operated Research Vessels',
     'url': 'https://www.marine.ie/Home/site-area/infrastructure-facilities/research-vessels/research-vessels'},
         {'text': 'Water Quality in Ireland under the Water Framework Directive',
     'url': 'https://www.epa.ie/publications/monitoring--assessment/freshwater--marine/Water-Quality-in-Ireland-2013-2018-(web).pdf'},

]

###############################################################################
chapter_dict = next(
    (item for item in CHAPTERS if item['chapter-num'] == chapter_num), None)
trendChartTitle1 = "Nitrogen Winter Exceedances Above the Recommended Thresholds"
trendChartTitle2 = ["Mean Winter Surface",html.Br(), "Phosphate"]
trendChartTitle3 = ["Mean Winter Surface",html.Br(), "Total Oxidised Nitrogen"]
trendChartTitle4 = "Deep-water Total Oxidised Nitrogen "
figure_3_17 = IMAGES_PATH+'OceanicSections/NitrogenIrishCoasts.png'
figure_3_18a = IMAGES_PATH+'OceanicSections/Figure3.18_MeanWinterSurface_Phosphate.png'
figure_3_18b = IMAGES_PATH+'OceanicSections/Figure3.18_MeanWinterSurface_TotalOxidisedNitrogen.png'
figure_3_19 = IMAGES_PATH+'OceanicSections/Nutrients_DeepSectionRockall.png'
trendCaption1 = """
Nitrogen winter exceedances above the recommended thresholds (2016-2018). 
Dissolved Inorganic Nitrogen thresholds indicative of status (blue = excellent, 
green = good, yellow = moderate, orange = poor, red = bad). 
Twenty-five percent of the sites, mainly to the south and east, showed excess 
nitrogen concentrations, which can be linked to land-based sources of pollution.
"""
trendCaption2 = """
Mean winter surface phosphate concentration (µmol/L) (2007-2018). Higher 
values are observed to the south and east and particularly in bays and estuaries.
"""
trendCaption3 = """
Mean winter surface total oxidised nitrogen (nitrate 
(NO\u2083) + nitrite (NO\u2082)) concentration (µmol/L) (2007-2018). Higher 
values are observed to the south and east and particularly in bays and estuaries.
"""
trendCaption4 = """
Deep-water total oxidised nitrogen (nitrate + nitrite) concentration (µmol/L) 
section for the Rockall Trough in the winter of 2013 (left), during the annual 
Rockall Ocean Climate survey (right).  The rows of vertical dots represent 
sampling points at different depths (left) and correspond to the blue point 
locations indicated in the red polygon (right).
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
                    dbc.Col(className="col-lg-6 offset-lg-3",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle1),
                                html.Img(
                                    className='w-100',
                                    src=figure_3_17
                                )
                                    ]
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
                                    trendCaption1]
                                )]
                            )
                ]
            ),
                        dbc.Row(
                children=[
                    dbc.Col(className="col-12 col-md-6",
                            children=[
                            html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle2),
                                html.Img(
                                    className='w-100',
                                    src=figure_3_18a
                                ),
                                       html.P(
                                    className='sr-chart-caption',
                                            children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption2]
                                )
                                    ]
                            ),
                  dbc.Col(className="col-12 col-md-6",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle3),
                                html.Img(
                                    className='w-100',
                                    src=figure_3_18b
                                ),
                                html.P(
                                    className='sr-chart-caption',
                                            children=[html.I(className="fas fa-play _up",
                                           style={"color": chapter_dict['domain-color']}),
                                    trendCaption3]
                                )
                                    ]
                            )
                ]
            ),
                        dbc.Row(
                children=[
                    dbc.Col(className="col-12",
                            children=[
                                html.H4(
                                    className='sr-chart-title',
                                    children=trendChartTitle4),
                                html.Img(
                                    className='w-100',
                                    src=figure_3_19
                                )
                                    ]
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
                                    trendCaption4]
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
            custom_trend,
            pb.build_infrastructure(infrastructureText,
                                    infrastructureMap,
                                    chapter_dict
                                    ),
            pb.build_info(infoLinks,
                          chapter_dict),

            pb.build_nav_carousel(chapter_dict)
        ])
