import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib
import page_builder as pb
# from settings import CHAPTERS
from settings import *

PATH = pathlib.Path(__file__).parent
ICONS_PATH = PATH.joinpath("../assets/images/icons").resolve()

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
                    dcc.Link(
                        href='/',
                        children=[
                            html.Img(
                                className='sr-menu-logo',
                                src='assets/images/CSRI2020Logo.png'
                            )])]
            )),
        dbc.Row(
            children=[
                dbc.Col(
                    className='text-center',
                    children=[
                        html.Img(
                            src='assets/images/LogoBannerCSRI.png'
                        ),

                    ])]),
        # dbc.Row(
        #     children=[
        #         dbc.Col(
        #             className='col-3 col-sm-2 offset-sm-2 my-auto text-center',
        #             children=html.Img(
        #                 className='sr-banner-org-icon',
        #                 src='assets/images/UCC_Logo_2018_low.png'
        #             )
        #         ),
        #         dbc.Col(
        #             className='col-3 col-sm-2 my-auto text-center',
        #             children=html.Img(
        #                 className='sr-banner-org-icon',
        #                 src='assets/images/EPA_logo.gif'
        #             )
        #         ),
        #         dbc.Col(
        #             className='col-3 col-sm-2 my-auto text-center',
        #             children=html.Img(
        #                 className='sr-banner-org-icon',
        #                 src='assets/images/mi_logo.gif'
        #             )
        #         ),
        #         dbc.Col(
        #             className='col-3 col-sm-1 my-auto text-center',
        #             children=html.Img(
        #                 className='sr-banner-org-icon',
        #                 src='assets/images/met.ie-logo.gif'
        #             )
        #         ),
        #     ],
        # ),
        dbc.Row(
            dbc.Col(
                className='sr-menu-intro-col',
                children=[
                    html.Div(

                        children=[html.P("""
        The Climate Status Report Ireland 2020 presents the state of Ireland’s climate based on the collation
        and analysis of almost 50 internationally defined essential climate variables (ECV) observed in the atmospheric,
            oceanic and terrestrial environments. Moreover, it documents the status of Ireland’s climate-observing infrastructure.
            The full report can be downloaded as a pdf here (link) or each ECV can be explored interactively below.
            """),
                                  html.P("""
            This work was carried out by the MaREI Centre at University College Cork. This work has been endorsed by GCOS-Ireland and has been co-funded by the Environmental Protection Agency, the Marine Institute and Met Éireann.
            """),

                                  ]
                    ),
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

menu_graphic = dbc.Container(

    id='gcosGraphicMenu',
    className='d-none d-lg-block',
    style={'marginTop': '-50px'},
    children=[
        html.Div(
            id='uaa-text',
            children='Upper-air Atmosphere'),
        html.Div(
            id='sa-text',
            children='Surface Atmosphere'),
        html.Div(
            id='ac-text',
            children='Atmospheric Composition'),
        # html.Div(
        #     id='cry-text',
        #     children='Cryosphere'),
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
            dcc.Link(children=[
                html.Img(src='assets/images/icons/' +
                         chapter['icon-src'])
            ],
                href=chapter['href']),
            html.Div(
                className="overlay",
                children=[
                    dcc.Link(children=[
                        html.Img(src='assets/images/icons/' +
                                 chapter['icon-hover-src'])
                    ],
                        href=chapter['href'])],),
            html.Div(
                className="dropdown-content",
                children=[
                    dcc.Link(
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
                    src='assets/images/icons/' +
                    chapter['icon-src'])
            ],
            ),
            html.Div(
                className="overlay",
                children=[
                    html.Div(children=[
                        html.Img(
                            style={"opacity": "0.4"},
                            src='assets/images/icons/' +
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
                                                    src='assets/images/icons/'+chapter['icon-hover-src']),
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
            menu_list,
            # dbc.Row(
            #     dbc.Col(
            #         children=[
            #             html.P(
            #                 className='sr-section-title text-center',
            #                 style={'color': '#08839b'},
            #                 children='More Chapters in Development'
            #             )])
            # ),
            dbc.Row(
                dbc.Col(
                    className="",
                    children=[
                        html.P(
                            className="sr-gcos-ack",
                            children=[
                                """Graphical elements and icons used in these pages are
                                    reproduced with the permission of GCOS-WMO and are in line with those featured on the """,
                                dcc.Link(
                                    children="GCOS ECV",
                                    href="https://gcos.wmo.int/en/essential-climate-variables",
                                    target="_blank"
                                ),
                                " pages."]
                        ),
                    ]
                )

            ),

        ])
