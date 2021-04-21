
import dash_core_components as dcc
import dash_html_components as html
import dash_trich_components as dtc
import dash_bootstrap_components as dbc
from settings import *

import pathlib


def build_banner(bannerImgSrc, bannerImgCredit, chapter_dict):

    return dbc.Container(
        className="sr-banner container-fluid",
        children=[
            html.Img(
                className='sr-banner-img',
                src=bannerImgSrc
            ),
            html.Span(
                className='sr-img-credit',
                children='Credit: ' + bannerImgCredit
            ),
            html.Div(
                className="sr-banner-inner",
                children=[
                    html.H1(
                        className='sr-banner-heading d-none d-md-block',
                        children=chapter_dict['title'],
                        style={'color': chapter_dict['domain-color']}
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(
                                className='',
                                children=html.Img(
                                    className='sr-banner-logo',
                                    src='assets/images/CSRI2020Logo.png'
                                ),)]),
                    dbc.Row(
                        children=[
                            dbc.Col(children=[
                                    html.Img(
                                        src='assets/images/LogoBannerCSRI.png'
                                    ),

                                    ])]),
                    # Remove before release
                    # dbc.Row(
                    #     children=[
                    #         dbc.Col(children=[
                    #             html.Img(
                    #                 className='sr-banner-org-icon2',
                    #                 src='assets/images/UCC_Logo_2018_low.png'
                    #             ),
                    #             html.Img(
                    #                 className='sr-banner-org-icon2',
                    #                 src='assets/images/EPA_logo.gif'
                    #             ),
                    #             html.Img(
                    #                 className='sr-banner-org-icon2',
                    #                 src='assets/images/mi_logo.gif'
                    #             ),
                    #             html.Img(
                    #                 className='sr-banner-org-icon2',
                    #                 src='assets/images/met.ie-logo.gif'
                    #             ),

                    #         ])]),
                    # dbc.Row(
                    #     children=[
                    #         dbc.Col(
                    #             className='col-sm-3 offset-md-1 my-auto text-center',
                    #             children=html.Img(
                    #                 className='sr-banner-org-icon',
                    #                 src='assets/images/UCC_Logo_2018_low.png'
                    #             )
                    #         ),
                    #         dbc.Col(
                    #             className='col-sm-3  my-auto text-center',
                    #             children=html.Img(
                    #                 className='sr-banner-org-icon',
                    #                 src='assets/images/EPA_logo.gif'
                    #             )
                    #         ),
                    #         dbc.Col(
                    #             className='col-sm-3 my-auto text-center',
                    #             children=html.Img(
                    #                 className='sr-banner-org-icon',
                    #                 src='assets/images/mi_logo.gif'
                    #             )
                    #         ),
                    #         dbc.Col(
                    #             className='col-sm-2 my-auto text-center',
                    #             children=html.Img(
                    #                 className='sr-banner-org-icon',
                    #                 src='assets/images/met.ie-logo.gif'
                    #             )
                    #         ),

                    #     ],
                    # )
                ]),
        ])


def build_breadcrumb(chapter_dict):

    return dbc.Container(
        className='sr-page-breadcrumb',
        children=[
            dcc.Link(
                style={'color': chapter_dict['domain-color']},
                children='Climate Ireland',
                href='https://www.climateireland.ie',
                target='_blank'
            ),
            html.Span(
                children=' / ',
            ),
            dcc.Link(
                style={'color': chapter_dict['domain-color']},
                className="sr-return-link",
                children='Climate Status Report',
                href='/dash/'
            ),
            html.Span(
                children=' / ',
            ),
            html.Span(
                style={'color': chapter_dict['domain-color']},
                children=chapter_dict['title'],
            )
        ]
    )


def build_nav(chapter_dict):

    return dbc.Container(
        style={'borderColor': chapter_dict['domain-color'],
               'color': chapter_dict['domain-color']},
        className='sr-page-nav d-none d-md-block',
        children=[
            dbc.Row(
                children=[
                    dbc.Col(className="col-md-3 my-auto",
                            children=[
                                html.A(
                                    className='sr-page-nav-item',
                                    style={
                                        'color': chapter_dict['domain-color']},
                                    children='Trends',
                                    href='#trends'),
                            ]),
                    dbc.Col(className="col-md-3 my-auto",
                            children=[
                                html.A(
                                    className='sr-page-nav-item',
                                    style={
                                        'color': chapter_dict['domain-color']},
                                    children='Infrastructure',
                                    href='#infrastructure'),
                            ]),
                    dbc.Col(className="col-md-3 my-auto",
                            children=[
                                html.A(
                                    className='sr-page-nav-item',
                                    style={
                                        'color': chapter_dict['domain-color']},
                                    children='Further Info',
                                    href='#info'),
                            ]),
                    dbc.Col(className="col-md-3 my-auto",
                            children=[
                                html.A(
                                    className='sr-page-nav-item',
                                    style={
                                        'color': chapter_dict['domain-color']},
                                    children='Report Chapter (pdf)',
                                    href=''),
                            ]),
                ])])


def build_intro(introText, bulletPoints, chapter_dict):

    return dbc.Container(
        style={'borderColor': chapter_dict['domain-color']},
        className='sr-intro',
        children=[
            dbc.Row(
                children=[
                    dbc.Col(className="col-12 col-md-2 offset-md-1 text-center my-auto",
                            children=[
                                html.Img(
                                    className='sr-intro-icon',
                                    src=IMAGES_PATH+'icons/' +
                                    chapter_dict['icon-lg-src']
                                )
                            ]
                            ),
                    dbc.Col(className="col-12 col-md-6 my-auto text-center",
                            children=[
                                html.H1(
                                    className='sr-ecv-heading',
                                    children=chapter_dict['title'],
                                    style={
                                        'color': chapter_dict['domain-color']},
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
                        className='sr-bullet-col',
                        style={
                            'backgroundColor': chapter_dict['domain-bg-color']},
                        children=[
                            html.Ul(
                                className='sr-bullet-ul',
                                children=[
                                    html.Li(
                                        className='',
                                        children=point)
                                    for point in bulletPoints]
                            )
                        ]
                    )]
            ),
            dbc.Row(

                children=[
                    dbc.Col(
                        style={'color': chapter_dict['domain-color']},
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
                style={
                    'backgroundColor': chapter_dict['domain-bg-color']},
                children=[
                    dbc.Col(
                        style={'color': chapter_dict['domain-color']},
                        className='col-xs-6 col-md-2',
                        children='Subdomain:'
                    ),
                    dbc.Col(

                        className='col-xs-6 col-md-10',
                        children=chapter_dict['subdomain']
                    ),
                ]
            ),
            dbc.Row(

                children=[
                    dbc.Col(
                        style={'color': chapter_dict['domain-color']},
                        className='col-xs-6 col-md-2',
                        children='Scientific Area:'
                    ),
                    dbc.Col(
                        className='col-xs-6 col-md-10',
                        children=chapter_dict['scientific-area']
                    ),
                ]
            ),
            dbc.Row(
                style={
                    'backgroundColor': chapter_dict['domain-bg-color']},
                children=[
                    dbc.Col(
                        style={'color': chapter_dict['domain-color']},
                        className='col-xs-6 col-md-2',
                        children='Authors:',
                    ),
                    dbc.Col(
                        className='col-xs-6 col-md-10',
                        children=chapter_dict['authors'],
                    ),
                ]
            ),
        ])


def build_trend(trendChartTitle, trendChart, trendCaption, chapter_dict):

    return dbc.Container(
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
                                    children=trendCaption
                                )]
                            )
                ]
            ),
        ])


def build_infrastructure(infrastructureText, infrastructureMap, chapter_dict):

    return dbc.Container(
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
                    dbc.Col(className="col-12 col-md-6 my-auto",
                            children=[
                                html.P(infrastructureText)]
                            ),
                    dbc.Col(className="col-12 col-md-6 my-auto",
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
        style={'borderColor': chapter_dict['domain-color']},
        children=[
            html.H3(
                className='sr-section-heading',
                children='Further Information',
                style={'color': chapter_dict['domain-color']},
            ),
            html.Ul(
                className='sr-bullet-ul',
                style={'color': chapter_dict['domain-color']},
                children=[html.Li(children=[
                    dcc.Link(
                        className='sr-info-item',
                        style={'color': chapter_dict['domain-color']},
                        children=link['text'],
                        href=link['url'],
                        target='_blank')]) for link in infoLinks])
        ])


def build_nav_carousel(chapter_dict):
    chapter_index = CHAPTERS.index(chapter_dict)
    chapters_before = CHAPTERS[0:chapter_index+1]
    chapters_after = CHAPTERS[chapter_index+1:]
    chapters_sorted = chapters_after+chapters_before

    return dbc.Container(
        className='sr-nav-carousel container-fluid',
        children=[
            dbc.Row(
                dbc.Col(
                    className='text-center',
                    children=[html.H3(
                        className='sr-section-heading mb-0',
                        children='Browse Climate Variables',
                        style={'color': chapter_dict['domain-color']},
                    ),
                        dcc.Link(
                            href='/dash/',
                            className="sr-return-link",
                            style={'color': chapter_dict['domain-color']},
                            children=["Or Return to Index"])
                    ]
                )),
            dbc.Row(
                dbc.Col(
                    dtc.Carousel(
                        className="mt-3",
                        children=[
                            html.Div(
                                className='sr-nav-carosuel-item text-center',
                                children=dcc.Link(
                                    className='sr-nav-carousel-link',
                                    style={
                                        'color': chapter['domain-color'], 'textDecoration':'none'},
                                    href=chapter['href'],
                                    children=[
                                        html.Img(
                                            className='sr-nav-carousel-img',
                                            src=IMAGES_PATH+'icons/'+chapter['icon-lg-src']),
                                        html.Img(
                                            className='sr-nav-carousel-img-hover',
                                            src=IMAGES_PATH+'icons/'+chapter['icon-lg-hover-src']),
                                        html.Div(
                                            children=chapter['title']
                                        )])
                            ) for chapter in CHAPTERS],
                        slides_to_scroll=1,
                        swipe_to_slide=True,
                        autoplay=False,
                        speed=2000,
                        variable_width=False,
                        center_mode=True,
                        responsive=[
                            {
                                'breakpoint': 3000,
                                'settings': {
                                    'initialSlide': chapter_index
                                }
                            },
                            {
                                'breakpoint': 700,
                                'settings': {
                                    'arrows': True,
                                    'slidesToShow': 1,
                                    'initialSlide': chapter_index
                                }
                            }]
                    )))])
