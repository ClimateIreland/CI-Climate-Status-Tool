import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib
from settings import *

PATH = pathlib.Path(__file__).parent

atmoshpere_chapters = []
ocean_chapters = []
terrestrial_chapters = []


for chapter in CHAPTERS:
    if chapter['domain'] == 'Atmosphere':
        atmoshpere_chapters.append(chapter)
    elif chapter['domain'] == 'Ocean':
        ocean_chapters.append(chapter)
    elif chapter['domain'] == 'Terrestrial':
        terrestrial_chapters.append(chapter)

atmoshpere_chapters_dev = []
ocean_chapters_dev = []
terrestrial_chapters_dev = []
for chapter in CHAPTERS_DEV:
    if chapter['domain'] == 'Atmosphere':
        atmoshpere_chapters_dev.append(chapter)
    elif chapter['domain'] == 'Ocean':
        ocean_chapters_dev.append(chapter)
    elif chapter['domain'] == 'Terrestrial':
        terrestrial_chapters_dev.append(chapter)

intro = dbc.Container(
    children=[
        dbc.Row(
            dbc.Col(
                className='text-center',
                children=[
                    html.Img(

                                className='sr-menu-logo',
                                style={"width": "150px"},
                                src=IMAGES_PATH+'Climate_status.png'
                            ),
                    html.H1("Ireland's Climate Status Tool",
                            style={"color": "rgba(0,10,20,.80)", "marginTop": "30px"})]
            )),
        dbc.Row(
            dbc.Col(
                className='sr-menu-intro-col',
                children=[
                    html.Div(

                        children=[html.P("""
            Ireland's Climate Status Tool provides interactive access to the Climate Status Report Ireland (CSRI) 2020. The CSRI report presents the state of Ireland’s climate based on the collation
            and analysis of almost 50 internationally defined essential climate variables (ECV) observed in the atmospheric,
            oceanic and terrestrial environments. Moreover, it documents the status of Ireland’s climate-observing infrastructure."""),
                                  html.P(children=[
                                      html.Span('The full report is available '),
                                      html.A(
                                          'here.',
                                          target='_blank',
                                          href='https://www.epa.ie/publications/research/climate-change/research-386-the-status-of-irelands-climate-2020',
                                      ),
                                  ]),
                                  ]
                    ),
                    html.Div(
                        className='text-center',
                        children=[
                            html.Img(
                                style={"width": "100%", "maxWidth": "800px"},
                                src=IMAGES_PATH+'ProjectBannerCSRI.png'
                            )],

                    )
                ]

            )

        ),
        dbc.Row(
            dbc.Col(
                html.H3(
                    className='sr-section-title text-center',
                    style={'color': '#08839b'},
                    children='Explore Ireland\'s Essential Climate Variables'
                )
            )

        ), ]
)

menu_graphic_small = dbc.Container(
    id='gcosGraphicSmall',
    className='d-lg-none d-xl-none',
    children=[html.Img(src=IMAGES_PATH+'menu_graphic_small.png')]
)

menu_graphic = dbc.Container(

    id='gcosGraphicMenu',
    className='d-none d-lg-block sr-menu-graphic',
    children=[
        html.Img(
                className='sr-graphic-menu-img',
                src=IMAGES_PATH+'Globe-ECV_Website_1140-708_white.png'
            ),
        html.Div(
            id='uaa-text',
            children='Upper-air Atmosphere'),
        html.Div(
            id='sa-text',
            children='Surface Atmosphere'),
        html.Div(
            id='ac-text',
            children='Atmospheric Composition'),
        html.Div(
            id='ant-text',
            children='Anthroposphere'),
        html.Div(
            id='bio-text',
            children='Biosphere'),
        html.Div(
            id='hyd-text',
            children='Hydrosphere'),
        html.Div(
            id='sop-text',
            children='Surface Ocean Physics'),
        html.Div(
            id='obe-text',
            children='Ocean Biology / Ecosystems'),
        html.Div(
            id='obgc-text',
            children='Ocean Biogeochemistry'),
        html.Div(
            id='ssop-text',
            children='Subsurface Ocean Physics'),
    ] +
    [html.Div(
        id=chapter['id'],
        className="dropdown",
        children=[
            dcc.Link(
                className="sr-graphic-link",
                children=[
                    html.Img(
                        src=IMAGES_PATH+'icons/' +
                             chapter['icon-src'])
                ],
                href=chapter['href']),
            html.Div(
                className="overlay",
                children=[
                    dcc.Link(children=[
                        html.Img(
                            src=IMAGES_PATH+'icons/' +
                                 chapter['icon-hover-src'])
                    ],
                        href=chapter['href'])],),
            html.Div(
                className="dropdown-content",
                children=[
                    dcc.Link(
                        className="sr-graphic-link",
                        style={'color': chapter['domain-color']},
                        children=chapter['title'],
                        href=chapter['href'])
                ]
            )]
    ) for chapter in CHAPTERS
    ] +
    [html.Div(
        id=chapter['id'],
        className="dropdown",
        children=[
            html.Div(children=[
                html.Img(
                    style={"opacity": "0.4"},
                    src=IMAGES_PATH+'icons/' +
                    chapter['icon-src'])
            ],
            ),
            html.Div(
                className="overlay",
                children=[
                    html.Div(children=[
                        html.Img(
                            style={"opacity": "0.4"},
                            src=IMAGES_PATH+'icons/' +
                            chapter['icon-hover-src'])
                    ],
                    )],),
            html.Div(
                className="dropdown-content",
                children=[
                    html.P(
                        style={'color': chapter['domain-color']},
                        children=chapter['title'],
                    ),
                    html.P(
                        style={
                            'color': chapter['domain-color'], "fontStyle": "italic"},
                        children="Coming Soon",
                    ),

                ]
            )]
    ) for chapter in CHAPTERS_DEV
    ]

)

menu_list = dbc.Container(
    className='sr-menu-list',
    children=[dbc.Row(
        children=[
            dbc.Col(className="col-12  col-md-4",
                    children=[html.Ul(
                        className='sr-menu-ul',
                        style={'color': ATMOSPHERE_COLOR},
                        children=[html.Li(html.H4('Atmosphere'))] +
                        [html.Li(children=[dcc.Link(
                            style={'color': ATMOSPHERE_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            children=chapter['title']
                                        )
                                    ]
                                )
                            ],
                            href=chapter['href']
                        )]) for chapter in atmoshpere_chapters] +
                        [html.Li(children=[html.Div(
                            style={'color': ATMOSPHERE_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    style={"opacity": "0.4"},
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            style={"opacity": "0.4"},
                                            children=html.Div(
                                                chapter['title'], title='Coming Soon')
                                        )
                                    ]
                                )
                            ],
                        )]) for chapter in atmoshpere_chapters_dev]
                    )
                    ]),


            ##################################
            dbc.Col(className="col-12  col-md-4",
                    children=[html.Ul(
                        className='sr-menu-ul',
                        style={'color': OCEAN_COLOR},
                        children=[html.Li(html.H4('Ocean'))] +
                        [html.Li(children=[dcc.Link(
                            style={'color': OCEAN_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            children=chapter['title']
                                        )
                                    ]
                                )
                            ],
                            href=chapter['href']
                        )]) for chapter in ocean_chapters] +
                        [html.Li(children=[html.Div(
                            style={'color': OCEAN_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    style={"opacity": "0.4"},
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            style={"opacity": "0.4"},
                                            children=html.Div(
                                                chapter['title'], title='Coming Soon')
                                        )
                                    ]
                                )
                            ],
                        )]) for chapter in ocean_chapters_dev]
                    )
                    ]),
            ######################################
            dbc.Col(className="col-12  col-md-4",
                    children=[html.Ul(
                        className='sr-menu-ul',
                        style={'color': TERRESTRIAL_COLOR},
                        children=[html.Li(html.H4('Terrestrial'))] +
                        [html.Li(children=[dcc.Link(
                            style={'color': TERRESTRIAL_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            children=chapter['title']
                                        )
                                    ]
                                )
                            ],
                            href=chapter['href']
                        )]) for chapter in terrestrial_chapters] +
                        [html.Li(children=[html.Div(
                            style={'color': TERRESTRIAL_COLOR},
                            className='sr-menu-chapter',
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-2 p-0 text-right my-auto',
                                            children=[
                                                html.Img(
                                                    className='sr-menu-list-icon',
                                                    style={"opacity": "0.4"},
                                                    src=IMAGES_PATH+'icons/'+chapter['icon-hover-src']),
                                            ]
                                        ),
                                        dbc.Col(
                                            className='col-10',
                                            style={"opacity": "0.4"},
                                            children=html.Div(
                                                chapter['title'], title='Coming Soon')
                                        )
                                    ]
                                )
                            ],
                        )]) for chapter in terrestrial_chapters_dev]
                    )
                    ]),
        ])
    ])


def create_layout(app):
    # Page layouts
    return html.Div(
        children=[
            intro,
            menu_graphic,
            menu_graphic_small,
            menu_list,
            dbc.Row(
                dbc.Col(
                    className="",
                    children=[
                        html.P(
                            className="sr-gcos-ack",
                            children=[
                                """Graphical elements and icons used in these pages are reproduced with the permission of
                                the World Meteorological Organisation, one of the co-sponsors of GCOS and are in line with 
                                those featured on the """,
                                dcc.Link(
                                    children="GCOS ECV",
                                    href="https://gcos.wmo.int/en/essential-climate-variables",
                                    target="_blank"
                                ),
                                " pages. This application was developed using the open-source ",
                                          dcc.Link(
                                    children="Plotly Dash",
                                    href="https://plotly.com/dash/",
                                    target="_blank"
                                ),
                                ' data visualization framework.'
                                ]
                        ),
                    ]
                )

            )

        ])
