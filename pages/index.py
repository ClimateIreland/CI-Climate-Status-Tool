import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib
import page_builder as pb
# from settings import CHAPTERS
from settings import *

PATH = pathlib.Path(__file__).parent
ICONS_PATH=PATH.joinpath("../assets/images/icons").resolve()

atmoshpere_chapters=[]
ocean_chapters=[]
terrestrial_chapters=[]
for chapter in CHAPTERS:
    if chapter['domain'] == 'Atmosphere':
        atmoshpere_chapters.append(chapter)
    elif chapter['domain'] == 'Ocean':
        ocean_chapters.append(chapter)
    elif chapter['domain'] == 'Terrestrial':
        terrestrial_chapters.append(chapter)

menu_list = dbc.Container(
        className='sr-menu-list',
        children=[dbc.Row(
            children=[
                dbc.Col(className="col-12  col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                    style={'color':ATMOSPHERE_COLOR},
                                  children=[html.Li(html.H4('Atmosphere'))]+
                                                    [html.Li(children=[dcc.Link(
                                                style={'color':ATMOSPHERE_COLOR},
                                                className='sr-menu-chapter',
                                                children=chapter['chapter-num'] + ' ' + chapter['title'], 
                                                href=chapter['href']
                                                )]) for chapter in atmoshpere_chapters]
                                                    )
                                                    ]),
       
               dbc.Col(className="col-12  col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                    style={'color':OCEAN_COLOR},
                                  children=[html.Li(html.H4('Ocean'))]+
                                                    [html.Li(children=[dcc.Link(
                                                style={'color':OCEAN_COLOR},
                                                className='sr-menu-chapter',
                                                children=chapter['chapter-num'] + ' ' + chapter['title'], 
                                                href=chapter['href']
                                                )]) for chapter in ocean_chapters]
                                                    )
                                                    ]),
             dbc.Col(className="col-12  col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                    style={'color':TERRESTRIAL_COLOR},
                                  children=[html.Li(html.H4('Terrestrial'))]+
                                                    [html.Li(children=[dcc.Link(
                                                style={'color':TERRESTRIAL_COLOR},
                                                className='sr-menu-chapter',
                                                children=chapter['chapter-num'] + ' ' + chapter['title'], 
                                                href=chapter['href']
                                                )]) for chapter in terrestrial_chapters]
                                                    )
                                                    ]),        
                        ])
        ])

menu_graphic = dbc.Container(

        id='gcosGraphicMenu',
        className='d-none d-lg-block',
        style={'marginTop':'-60px'},
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
            html.Div(
                id='cry-text',
                children='Cryosphere'), 
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
                     ]+
            [html.Div(
                id=chapter['id'],
                className="dropdown",
                children=[
                    dcc.Link(children=[
                            html.Img(src='assets/images/icons/'+chapter['icon-src'])
                            ], 
                            href=chapter['href']),
                    html.Div(
                        className="overlay",
                        children=[
                            dcc.Link(children=[
                                html.Img(src='assets/images/icons/'+chapter['icon-hover-src'])
                                ], 
                                href=chapter['href'])],),
                    html.Div(
                            className="dropdown-content",
                            children=[
                                dcc.Link(
                                    style={'color':chapter['domain-color']},
                                    children=chapter['title'],
                            href=chapter['href'])
                            ]
                            ) ]                  
                ) for chapter in CHAPTERS           
                ])
               


def create_layout(app):
        # Page layouts
    return html.Div(children=[
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
                                className='col-3 col-sm-2 offset-sm-2 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/EPA_logo.gif'
                                )
                                ),
                            dbc.Col(
                                className='col-3 col-sm-2 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/UCC_Logo_2018_low.png'
                                )
                                ),
                            dbc.Col(
                                className='col-3 col-sm-2 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/mi_logo.gif'
                                )
                                ),
                            dbc.Col(
                                className='col-3 col-sm-1 my-auto text-center',
                                children=html.Img(
                                    className='sr-banner-org-icon',
                                    src='assets/images/met.ie-logo.gif'
                                )
                                )
                            ],
                        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    className='menu_intro_textbox',
                    children=[
                        html.P("""
        As an island on the western boundary of Europe facing the Atlantic Ocean Ireland is ideally positioned to 
        measure and assess ongoing climate change. 
        This is achieved through baseline and background measurements of essential climate variables (ECVs).
        """),
                             html.P("""
        The Climate Status Report Ireland 2020 assesses the current state of Irelands climate. 
        The full report can be downladed as pdf here (Link) or can be explored interactively below.
        """),

                    ]
                )
                )

            ),
        dbc.Row(
            dbc.Col(
                html.H3(
                    className='sr-section-title text-center',
                    style={'color':'#08839b'},
                    children='Explore Irelands Essential Climate Variables'
                )
                )

            ),
        menu_graphic,
        menu_list,
        dbc.Row(
            dbc.Col(
                html.P(
                    className='sr-section-title text-center',
                    style={'color':'#08839b'},
                    children='More Chapters in Development'
                )
                )

            ),

        ])



