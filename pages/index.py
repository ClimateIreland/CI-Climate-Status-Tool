import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def create_layout(app):
        # Page layouts
    return html.Div(children=[
        html.H1(
          className='text-center',
          children='Climate Status Report Ireland'),
            dbc.Row(
            children=[
                dbc.Col(className="col-md-4",
                        children=[html.Ul(
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
                dbc.Col(className="col-md-4",
                        children=[html.Ul(
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
                 dbc.Col(className="col-md-4",
                        children=[html.Ul(
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



