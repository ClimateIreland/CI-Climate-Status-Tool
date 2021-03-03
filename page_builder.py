
import dash_core_components as dcc
import dash_html_components as html
import dash_trich_components as dtc
import dash_bootstrap_components as dbc
from settings import *

import pathlib

# def domainColor(domain):
#     if domain == 'Atmosphere':
#         return ATMOSPHERE_COLOR
#     elif domain == 'Ocean':
#          return OCEAN_COLOR
#     elif domain == 'Terrestrial':
#          return TERRESTRIAL_COLOR
#     else:
#         return 'black'

# def domainBGColor(domain):
#     if domain == 'Atmosphere':
#         return ATMOSPHERE_BG_COLOR
#     elif domain == 'Ocean':
#          return OCEAN_BG_COLOR
#     elif domain == 'Terrestrial':
#          return TERRESTRIAL_BG_COLOR
#     else:
#         return 'white'


def build_banner(ecvName, bannerImgSrc, bannerImgCredit, chapter_dict):

    return dbc.Container(
        className="sr-banner container-fluid",
        children=[
            html.Img(
                className='sr-banner-img',
                src=bannerImgSrc
            ),
            html.P(
                className='sr-img-credit',
                children=bannerImgCredit
            ),
            html.Div(
                className="sr-banner-inner",
                children=[
                    html.H1(
                        className='sr-banner-heading d-none d-md-block',
                        children=ecvName,
                        style={'color':chapter_dict['domain-color']}
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                className='',
                                children=
                                html.Img(
                                    className='sr-banner-logo',
                                    src='assets/images/CSRI2020Logo.png'
                                ),)]),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                className='col-sm-3 offset-md-1 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/EPA_logo.gif'
                                )
                                ),
                            dbc.Col(
                                className='col-sm-3 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/UCC_Logo_2018_low.png'
                                )
                                ),
                            dbc.Col(
                                className='col-sm-3 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/mi_logo.gif'
                                )
                                ),
                            dbc.Col(
                                className='col-sm-2 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/met.ie-logo.gif'
                                )
                                )
                            ],
                        )
                    ]),
                ])

def build_breadcrumb(ecvName, chapter_dict):

    return dbc.Container(
        className='sr-page-breadcrumb',
        children=[
            dcc.Link(
                    style={'color':chapter_dict['domain-color']},
                    children='Climate Ireland', 
                    href='https://www.climateireland.ie',
                    target='_blank'
                    ),
            html.Span(
                 children=' / ',
            ),
            dcc.Link(
                    style={'color':chapter_dict['domain-color']},
                    children='Climate Status Report', 
                    href='/'
                    ),
            html.Span(
                 children=' / ',
            ),
            html.Span(
                 style={'color':chapter_dict['domain-color']},
                 children=ecvName,
            )
            ]             
    )

def build_nav(chapter_dict):

    return dbc.Container(
        style={'borderColor':chapter_dict['domain-color'], 'color':chapter_dict['domain-color']},
        className='sr-page-nav d-none d-md-block',
        children=[
        dbc.Row(
            children=[
                dbc.Col(className="col-md-3 my-auto",
                        children=[
                            html.A(
                                className='sr-page-nav-item',
                                style={'color':chapter_dict['domain-color']},
                                children='Observations', 
                                href='#trends'),
                            ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':chapter_dict['domain-color']},
                            children='Infrastructure',
                            href='#infrastructure'),
                        ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':chapter_dict['domain-color']},
                            children='Further Info',
                            href='#info'),
                        ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':chapter_dict['domain-color']},
                            children='Report Chapter (pdf)',  
                            href=''),
                        ]),
            ])])

def build_intro(ecvName,introText,bulletPoint1,bulletPoint2,ecvIconSrc,subdomain,scientificArea,authors, chapter_dict):

    return dbc.Container(
        style={'borderColor':chapter_dict['domain-color']},
        className='sr-intro',
        children=[
        dbc.Row(
            children=[
                dbc.Col(className="col-12 col-md-2 offset-md-1 text-center my-auto",
                        children=[
                            html.Img(
                                className='sr-intro-icon',
                                src=ecvIconSrc
                            )]
                            ),
                dbc.Col(className="col-12 col-md-6 my-auto text-center",
                        children=[
                            html.H1(
                                className='sr-ecv-heading',
                                children=ecvName,
                                style={'color':chapter_dict['domain-color']},
                            )]
                            ),

                        ]
                    ),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.P(
                            children=introText
                        )
                    ]

                )
            ]

        ),
        dbc.Row(
            children=[
                dbc.Col(
            children=[
                html.Ul(
                    className='sr-bullet-ul',
                    style={'backgroundColor':chapter_dict['domain-bg-color']},
                    children=[
                        html.Li(className='mb-4',
                        children=bulletPoint1),
                        html.Li(className='',
                        children=bulletPoint2),
                        ]
                        )
                    ]
                )]

        ),
        dbc.Row(
            style={'color':chapter_dict['domain-color']},
            children=[
                dbc.Col(
                
                    className='col-xs-6 col-md-2',
                    children='Domain:'
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=chapter_dict['domain']
                ),
            ]
        ),
        dbc.Row(
            style={'color':chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    style={'backgroundColor':chapter_dict['domain-bg-color']},
                    className='col-xs-6 col-md-2',
                    children='Subdomain:'
                ),
                dbc.Col(
                    style={'backgroundColor':chapter_dict['domain-bg-color']},
                    className='col-xs-6 col-md-10',
                    children=subdomain
                ),
            ]
        ),
        dbc.Row(
            style={'color':chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    className='col-xs-6 col-md-2',
                    children='Scientific Area:'
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=scientificArea
                ),
            ]
        ),
        dbc.Row(
            style={'color':chapter_dict['domain-color']},
            children=[
                dbc.Col(
                    className='col-xs-6 col-md-2',
                    children='Authors:',
                    style={'backgroundColor':chapter_dict['domain-bg-color']},
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=authors,
                    style={'backgroundColor':chapter_dict['domain-bg-color']},
                ),
            ]
        ),
            ])

def build_trend(trendChartTitle,trendChart,trendCaption, chapter_dict):

    return dbc.Container(
        className='sr-trends',
        style={'borderColor':chapter_dict['domain-color']},
        id='trends',
        children=[
        html.H3(
            className='sr-section-heading',
            style={'color':chapter_dict['domain-color']},
            children='Trends and Observations',
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
                                children=trendCaption
                                )]
                            )
                        ]
                    ),
            ])

def build_infrastructure(infrastructureText,infrastructureMap,chapter_dict):

    return dbc.Container(
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
                    dbc.Col(className="col-12 col-md-6 my-auto",
                    children=[
                        html.P(infrastructureText)]
                    ),
                    dbc.Col(className="col-12 col-md-6",
                    children=[dcc.Graph(
                    id='StationsMap',
                    figure=infrastructureMap,
                    config={'displayModeBar': False},
                    )])
                    ])
                ])

def build_info(infoLinks, chapter_dict):

    return dbc.Container(
        className='sr-info',
        id='info',
        style={'borderColor':chapter_dict['domain-color']},
        children=[
            html.H3(
                className='sr-section-heading',
                children='Further Information',
                style={'color':chapter_dict['domain-color']},
                ),
            html.Ul(
                children=[html.Li(children=[
                                dcc.Link(
                                    
                                    className='sr-info-item',
                                    style={'color':chapter_dict['domain-color']},
                                    children=link['text'], 
                                    href=link['url'],
                                    target='_blank')]) for link in infoLinks])
            ])

def build_nav_carousel(chapter_dict):
    return dbc.Container(
        className='sr-nav-carousel container-fluid',
        children=[
            dbc.Row(
                dbc.Col(
                    className='text-center',
                    children=[
                        dcc.Link(
                            href='/',
                            children=[
                                html.Img(
                                    className='sr-nav-carousel-logo',
                                    src='assets/images/CSRI2020Logo.png'
                                    )])]
                                    )),
            dbc.Row(
                dbc.Col(
                    dtc.Carousel(
                        children=[
                            html.Div(
                                className='sr-nav-carosuel-item text-center',
                                children=dcc.Link(
                                        className='sr-nav-carousel-link',
                                        style={'color':item['domain-color'],'textDecoration':'none'},
                                        href=item['href'],
                                        children=[
                                            html.Img(
                                                className='sr-nav-carousel-img',
                                                src='assets/images/icons/'+item['icon-src']),
                                            html.Img(
                                                className='sr-nav-carousel-img-hover',
                                                src='assets/images/icons/'+item['icon-hover-src']),
                                            html.Div(
                                                children=item['name']
                                                )])
                            ) for item in CHAPTERS],
                            slides_to_scroll=1,
                            swipe_to_slide=True,
                            autoplay=False,
                            speed=2000,
                            variable_width=False,
                            center_mode=True,
                            responsive=[
                            {
                                'breakpoint': 600,
                                'settings': {
                                    'arrows': True,
                                    'slidesToShow': 1,
                                }
                            }]
                        )))])