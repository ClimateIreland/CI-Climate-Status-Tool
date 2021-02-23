
import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc

import pathlib

def domainColor(domain):
    atmosphereColor='#009fe3'
    oceanColor='#00909e'
    terrestrialColor='#f39200'

    if domain == 'Atmosphere':
        return atmosphereColor
    elif domain == 'Ocean':
         return oceanColor
    elif domain == 'Terrestrial':
         return terrestrialColor
    else:
        return 'black'

def domainBGColor(domain):

    atmosphereBGColor='#e6f5fc'
    oceanBGColor='#e6f3f5'
    terrestrialBGColor='#fef4e6'
    if domain == 'Atmosphere':
        return atmosphereBGColor
    elif domain == 'Ocean':
         return oceanBGColor
    elif domain == 'Terrestrial':
         return terrestrialBGColor
    else:
        return 'white'


def build_banner(domain, ecvName, bannerImgSrc, bannerImgCredit, domainColor,domainBGColor):

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
                    html.H4(
                        className='sr-banner-heading',
                        children=ecvName,
                        style={'color':domainColor}
                    ),
                    html.Img(
                        className='sr-banner-logo',
                        src='assets/images/CSRI_logo_with_partners.png'
                    ),]),
                ])

def build_breadcrumb(ecvName, domainColor,domainBGColor):

    return dbc.Container(
        className='sr-page-breadcrumb',
        children=[
            dcc.Link(
                    style={'color':domainColor},
                    children='Climate Ireland', 
                    href='https://www.climateireland.ie'
                    ),
            html.Span(
                 children=' / ',
            ),
            dcc.Link(
                    style={'color':domainColor},
                    children='Climate Status Report', 
                    href='/'
                    ),
            html.Span(
                 children=' / ',
            ),
            html.Span(
                 style={'color':domainColor},
                 children=ecvName,
            )
            ]             
    )
def build_nav(domain, domainColor,domainBGColor):

    return dbc.Container(
        style={'borderColor':domainColor, 'color':domainColor},
        className='sr-page-nav d-none d-md-block',
        children=[
        dbc.Row(
            children=[
                dbc.Col(className="col-md-3 my-auto",
                        children=[
                            html.A(
                                className='sr-page-nav-item',
                                style={'color':domainColor},
                                children='Observations', 
                                href='#trends'),
                            ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':domainColor},
                            children='Infrastructure',
                            href='#infrastructure'),
                        ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':domainColor},
                            children='Further Info',
                            href='#info'),
                        ]),
                dbc.Col(className="col-md-3 my-auto",
                    children=[
                        html.A(
                            className='sr-page-nav-item',
                            style={'color':domainColor},
                            children='Report Chapter (pdf)',  
                            href=''),
                        ]),
            ])])

def build_intro(ecvName,introText,bulletPoint1,bulletPoint2,ecvIconSrc,domain,subdomain,scientificArea,authors, domainColor,domainBGColor):

    return dbc.Container(
        style={'borderColor':domainColor},
        className='sr-intro',
        children=[
        dbc.Row(
            children=[
                dbc.Col(className="col-md-2 offset-md-1 text-center my-auto",
                        children=[
                            html.Img(
                                className='sr-intro-icon',
                                src=ecvIconSrc
                            )]
                            ),
                dbc.Col(className="col-md-6 my-auto",
                        children=[
                            html.H1(
                                className='sr-ecv-heading',
                                children=ecvName,
                                style={'color':domainColor},
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
                    style={'backgroundColor':domainBGColor},
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
            style={'color':domainColor},
            children=[
                dbc.Col(
                
                    className='col-xs-6 col-md-2',
                    children='Domain:'
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=domain
                ),
            ]
        ),
        dbc.Row(
            style={'color':domainColor},
            children=[
                dbc.Col(
                    style={'backgroundColor':domainBGColor},
                    className='col-xs-6 col-md-2',
                    children='Subdomain:'
                ),
                dbc.Col(
                    style={'backgroundColor':domainBGColor},
                    className='col-xs-6 col-md-10',
                    children=subdomain
                ),
            ]
        ),
        dbc.Row(
            style={'color':domainColor},
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
            style={'color':domainColor},
            children=[
                dbc.Col(
                    className='col-xs-6 col-md-2',
                    children='Authors:',
                    style={'backgroundColor':domainBGColor},
                ),
                dbc.Col(
                    className='col-xs-6 col-md-10',
                    children=authors,
                    style={'backgroundColor':domainBGColor},
                ),
            ]
        ),
            ])

def build_trend(trendChartTitle,trendChart,trendCaption,domain, domainColor,domainBGColor):

    return dbc.Container(
        className='sr-trends',
        style={'borderColor':domainColor},
        id='trends',
        children=[
        html.H3(
            className='sr-section-heading',
            children='Trends and Observations',
            style={'color':domainColor},
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

def build_infrastructure(infrastructureText,infrastructureMap,domain, domainColor,domainBGColor):

    return dbc.Container(
        className='sr-infrastructure',
        style={'borderColor':domainColor},
        id='infrastructure',
        children=[
            html.H3(
                className='sr-section-heading',
                children='Observation Infrastructure',
                style={'color':domainColor},
                ),
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-6 my-auto",
                    children=[
                        html.P(infrastructureText)]
                    ),
                    dbc.Col(className="col-md-6",
                    children=[dcc.Graph(
                    id='StationsMap',
                    figure=infrastructureMap,
                    config={'displayModeBar': False},
                    )])
                    ])
                ])

def build_info(infoLinks, domain,domainColor,domainBGColor):

    return dbc.Container(
        className='sr-info',
        id='info',
        children=[
            html.H3(
                className='sr-section-heading',
                children='Further Information',
                style={'color':domainColor},
                ),
            html.Ul(
                children=[html.Li(children=[
                                dcc.Link(
                                    className='sr-info-item',
                                    children=link['text'], 
                                    href=link['url'],
                                    target='_blank')]) for link in infoLinks])
            ])