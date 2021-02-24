import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pathlib
import page_builder as pb

PATH = pathlib.Path(__file__).parent
ICONS_PATH=PATH.joinpath("../assets/images/icons").resolve()

menuItems=[

    # Upper-air Atmoshere
    # {
    #  'id':'uaa-1',
    #  'name':'Lightning', 
    #  'href':'',
    #  'icon-src':'ico-uaa-lightning.png',
    #  'icon-hover-src':'ico-uaa-lightning_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #     {
    #  'id':'uaa-2',
    #  'name':'Clouds', 
    #  'href':'',
    #  'icon-src':'ico-uaa-cloud-properties.png',
    #  'icon-hover-src':'ico-uaa-cloud-properties_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-3',
    #  'name':'Earth Radiation Budget', 
    #  'href':'',
    #  'icon-src':'ico-uaa-earth-radiation-budget.png',
    #  'icon-hover-src':'ico-uaa-earth-radiation-budget_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-4',
    #  'name':'Wind Speed', 
    #  'href':'',
    #  'icon-src':'ico-uaa-lightning.png',
    #  'icon-hover-src':'ico-uaa-windspeed_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-5',
    #  'name':'Upper Air Atmosphere Temperature', 
    #  'href':'',
    #  'icon-src':'ico-uaa-temperature.png',
    #  'icon-hover-src':'ico-uaa-temperature_hover.png',
    #  'domain':'Atmosphere',
    #         },
    #             {
    #  'id':'uaa-6',
    #  'name':'Upper Air Atmosphere Water Vapour', 
    #  'href':'',
    #  'icon-src':'ico-uaa-watervapour.png',
    #  'icon-hover-src':'ico-uaa-watervapour_hover.png',
    #  'domain':'Atmosphere',
    #         },
        # Surface Atmoshere
    #             {
    #  'id':'sa-1',
    #  'name':'Surface Atmosphere Precipitation', 
    #  'href':'',
    #  'icon-src':'ico-sa-precipitation.png',
    #  'icon-hover-src':'ico-sa-precipitation_hover.png',
    #  'domain':'Atmosphere',
            # },
              {
     'id':'sa-5',
     'name':'Surface Temperature', 
     'href':'/_2_1_SurfaceAirTemperature',
     'icon-src':'ico-sa-temperature.png',
     'icon-hover-src':'ico-sa-temperature_hover.png',
     'domain':'Atmosphere',
            },
        # Atmoshperic Composition
        #    {
    #  'id':'ac-2',
    #  'name':'Carbon Dioxide, Methane and other Greenhouse gases', 
    #  'name':'Carbon Dioxide', 
    #  'href':'',
    #  'icon-src':'ico-ac-co2-ghgs.png',
    #  'icon-hover-src':'ico-ac-co2-ghgs_hover.png',
    #  'domain':'Atmosphere',
            # },
    #     {
    # 'id':'ac-4',
    #  'name':'Atmospheric Composition Precursors', 
    #  'name':'Methane', 
    #  'href':'',
    #  'icon-src':'ico-ac-precursors.png',
    #  'icon-hover-src':'ico-ac-precursors_hover.png',
    #  'domain':'Atmosphere',
    #         },
     # Biosphere
         {
     'id':'bio-2',
     'name':'Land Cover', 
     'href':'',
     'icon-src':'ico-bio-land-cover.png',
     'icon-hover-src':'ico-bio-land-cover_hover.png',
     'domain':'Terrestrial',
            },
                 {
     'id':'bio-7',
     'name':'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR)', 
     'href':'',
     'icon-src':'ico-bio-fapr.png',
     'icon-hover-src':'ico-bio-fapr_hover.png',
     'domain':'Terrestrial',
            },

    # Ocean Biogeochemistry

                     {
     'id':'obgc-2',
     'name':'Oxygen', 
     'href':'/_3_7_DissolvedOxygen',
     'icon-src':'ico-obgc-oxygen.png',
     'icon-hover-src':'ico-obgc-oxygen_hover.png',
     'domain':'Ocean',
            }


            ]


menu_list = dbc.Container(
        className='sr-menu-list',
        children=[dbc.Row(
            children=[
                dbc.Col(className="col-12  col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                    style={'color':pb.domainColor('Atmosphere')},
                                  children=[html.Li(html.H4('Atmosphere')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-item',
                                                children='Surface Air Temperature', 
                                                href='/_2_1_SurfaceAirTemperature'
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Precipitation', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Carbon Dioxide', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Methane', 
                                                    href=''
                                                    )])
                                                    ])
                                                    ]),
                dbc.Col(className="col-12 col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                  style={'color':pb.domainColor('Terrestrial')},
                                  children=[html.Li(html.H4('Terrestrial')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-item',
                                                children='Landcover', 
                                                href=''
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='FAPAR', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='River Discharge', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Fire Disturbance', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Anthropogenic Greenhouse Gas Emissions', 
                                                    href=''
                                                    )])
                                                    ])
                                                    ]),
                 dbc.Col(className="col-12 col-md-4",
                        children=[html.Ul(
                                  className='sr-menu-ul',
                                  style={'color':pb.domainColor('Ocean')},
                                  children=[html.Li(html.H4('Ocean')),
                                            html.Li(children=[dcc.Link(
                                                className='sr-menu-item',
                                                children='Sea Surface Temperature', 
                                                href=''
                                                )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Sub-Surface Temperature', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Sea Level', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
                                                    children='Inorganic Carbon', 
                                                    href=''
                                                    )]),
                                            html.Li(children=[
                                                dcc.Link(
                                                    className='sr-menu-item',
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
                id=item['id'],
                className="dropdown",
                children=[
                    dcc.Link(children=[
                            html.Img(src='assets/images/icons/'+item['icon-src'])
                            ], 
                            href=item['href']),
                    html.Div(
                        className="overlay",
                        children=[
                        dcc.Link(children=[
                            html.Img(src='assets/images/icons/'+item['icon-hover-src'])
                            ], 
                            href=item['href'])],),
                html.Div(
                            className="dropdown-content",
                            children=[
                                dcc.Link(
                                    style={'color':pb.domainColor(item['domain'])},
                                    children=item['name'],
                            href=item['href'])
                            ]
                            ) ]                  
                ) for item in menuItems              
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



