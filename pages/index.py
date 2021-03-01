import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib
import page_builder as pb
# from settings import CHAPTERS
from settings import *

PATH = pathlib.Path(__file__).parent
ICONS_PATH=PATH.joinpath("../assets/images/icons").resolve()

menu_list = dbc.Container(
        className='sr-menu-list',
        children=[dbc.Row(
            children=[
                dbc.Col(className="col-12  col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                    style={'color':ATMOSPHERE_COLOR},
                                  children=[html.Li(html.H4('Atmosphere')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-chapter',
                                                children='Surface Air Temperature', 
                                                href='/_2_1_SurfaceAirTemperature'
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Precipitation', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Carbon Dioxide', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Methane', 
                                                    href=''
                                                    )])
                                                    ])
                                                    ]),
                dbc.Col(className="col-12 col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                  style={'color':TERRESTRIAL_COLOR},
                                  children=[html.Li(html.H4('Terrestrial')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-chapter',
                                                children='Landcover', 
                                                href=''
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='FAPAR', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='River Discharge', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Fire Disturbance', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Anthropogenic Greenhouse Gas Emissions', 
                                                    href=''
                                                    )])
                                                    ])
                                                    ]),
                 dbc.Col(className="col-12 col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                  style={'color':OCEAN_COLOR},
                                  children=[html.Li(html.H4('Ocean')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-chapter',
                                                children='Sea Surface Temperature', 
                                                href=''
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Sub-Surface Temperature', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Sea Level', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Inorganic Carbon', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-chapter',
                                                    children='Dissolved Oxygen', 
                                                    href='/_3_7_DissolvedOxygen'
                                                    )])
                                                    ])
                                                    ]),             
                        ])
        ])

menu_graphic = dbc.Container(

        id='gcosGraphicMenu',
        className='d-none d-lg-block',
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
                                    children=chapter['name'],
                            href=chapter['href'])
                            ]
                            ) ]                  
                ) for chapter in CHAPTERS           
                ])
               


def create_layout(app):
        # Page layouts
    return html.Div(children=[
        html.H1(
          className='text-center',
          children='Climate Status Report Ireland'),
        menu_graphic,
        menu_list,

        ])



