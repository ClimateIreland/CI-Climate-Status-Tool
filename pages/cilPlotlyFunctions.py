"""

"""

def cilTimeSeriesStyle():
    cilTimeSeriesStyle=dict(lineStylePrimary=dict(color='#00a4ae',
                                                  width=2),
                            lineStyleSecondary = dict(color = '#E1AF00',
                                                      width = 2),
                            markerStylePrimary = dict(color='#00a4ae',
                                                      size=4,
                                                      line=dict(color='#00a4ae',
                                                                width=0)),
                            markerStyleSecondary = dict(color='#E1AF00',
                                                        size=5,
                                                        opacity = 0.5)
                                                        )

    return cilTimeSeriesStyle


def cilTimeSeriesLayoutDict():

    cilTimeSeriesLayoutDict=dict(
                    title_x=0.55, # Centers the title
                    showlegend=True,
                    legend=dict(orientation="h", #h for horizontal, 'v' is default
                                x=0.15, 
                                y=1.08
                                ), 
                    xaxis=dict(showgrid=False),
                    height=500,
                    margin={"t":40, "b":0,"r":0,"l":0,},  
                    plot_bgcolor='#f7fbfd',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font = dict(
                        family = "Arial",
                        size = 13,
                        color = "#7f7f7f")
                        )
    return cilTimeSeriesLayoutDict

def cilSlideTimeSeriesLayoutDict():

    cilSlideTimeSeriesLayoutDict= dict(
                   title_x=0.5, # Centers the title
                   showlegend=True,
                   legend=dict(orientation="h", #h for horizontal, 'v' is default
                               x=0.15, 
                               y=1.08
                              ), 
                   xaxis=dict(showgrid=False),
                   height=380,
                   margin={"t":40, "b":30,"r":0,"l":0,},  
                   plot_bgcolor='#f7fbfd',
                   paper_bgcolor='rgba(0,0,0,0)',
                   font = dict(
                       family = "Arial",
                       size = 13,
                       color = "#7f7f7f")
                    )
    return cilSlideTimeSeriesLayoutDict


def ciStatusReportTimeSeriesLayoutDict():

    ciStatusReportTimeSeriesLayoutDict= dict(
                   title_x=0.5, # Centers the title
                   showlegend=True,
                   legend=dict(orientation="h", #h for horizontal, 'v' is default
                               x=0.15, 
                               y=1.08
                              ), 
                   xaxis=dict(showgrid=False),
                   height=450,
                   margin={"t":40, "b":30,"r":0,"l":0,},  
                   plot_bgcolor='#f7fbfd',
                   paper_bgcolor='rgba(0,0,0,0)',
                   font = dict(
                       family = "Arial",
                       size = 13,
                       color = "#7f7f7f")
                    )
    return ciStatusReportTimeSeriesLayoutDict


def cilBarLayoutDict():

    cilBarLayoutDict=dict(
                    title_x=0.55, # Centers the title
                    height=500,
                    margin={"t":40, "b":0,"r":20,"l":0,},  
                    plot_bgcolor='#f7fbfd',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font = dict(
                        family = "Arial",
                        size = 13,
                        color = "#7f7f7f")
                        )
    return cilBarLayoutDict

def cilSlideMapLayoutDict():

#     mapbox_access_token = open(".mapbox_token").read()
    cilSlideMapLayoutDict = dict(
        title_x=0,
        title_y=1,
        height=400,      
        width=400,
        margin=dict(t=20,b=10,r=0,l=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        xaxis={'title': 'x-axis','fixedrange':True},
        yaxis={'title': 'y-axis','fixedrange':True},
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=53.5,
                lon=352
            ),
            pitch=0,
            zoom=5,
            style="open-street-map" # does not require token
        ),)

    return cilSlideMapLayoutDict

def cilSationMapLayoutDict():

#     mapbox_access_token = open(".mapbox_token").read()
    cilSlideMapLayoutDict = dict(
        title_x=0,
        title_y=1,
        height=400,      
        margin=dict(t=20,b=10,r=0,l=0),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        xaxis={'title': 'x-axis','fixedrange':True},
        yaxis={'title': 'y-axis','fixedrange':True},
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=53.5,
                lon=349
            ),
            pitch=0,
            zoom=5,
            style="open-street-map" # does not require token
        ),)

    return cilSlideMapLayoutDict

def cilSlideMapConfig():
    cilSlideMapConfig = {"scrollZoom": False,
    'displayModeBar': False,
    'displaylogo': False}

    return cilSlideMapConfig



def cilConfig():

    return {'displaylogo': False, 'displayModeBar': False}

def cilColorGradient():
    cil_color_gradient = ['#a6cee3', # light blue
                 '#1f78b4', # dark blue
                 '#b2df8a', # light green
                 '#33a02c', # dark green
                 '#fb9a99', # light red
                 '#e31a1c', # dark red
                 '#fdbf6f', # light orange
                 '#ff7f00', # dark orange
                 '#cab2d6', # light purple
                 '#6a3d9a', # deep purple
                 '#f0f090'] # light yellow

    return cil_color_gradient

def cilPieLayoutDict():
    cil_pie_layout_dict = dict(
            height=380, # chart height 380 + source div height 20 = total height 400 
            title_x=0.5,
            title_y=0.94,
            margin={"b": 0,"r": 0, "l": 0, "t":60},
            font=dict(
                family = "Arial",
                size = 13, 
                color = "#7f7f7f"
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
    )
    return cil_pie_layout_dict


def cilPrintHTML(chart, chartName, sourceList, include_plotlyjs,config):
    """
    Prints plotly charts as HTML, with and without source and with and with plotly script
    """
    sourceString=""
    if len(sourceList) > 0:
        sourceString="Source:"
        i=0
        for source in sourceList:
            if i>0:
                sourceString+=','
            sourceString+=' <a target="_blank" href="{0}">{1}</a>'.format(
                source['url'],
                source['title'])
            i+=1

   
    if include_plotlyjs == False:
        fileNoSource = "../html/" + chartName + "-noSrc.html"
        fileWithSource = "../html/" + chartName + ".html"
        
    else:
        fileNoSource = "../html/" + chartName + "-noSrc-IncludePlolty.html"
        fileWithSource = "../html/" + chartName + "-IncludePlolty.html"
        
    ciLogoSrc="https://www.climateireland.ie/web_resource/images/logos/Climate-Ireland-Logo-RGB.png"
    chartStyle = \
    """
        <style>
            .ls-chart-source-container {
                height:20px;
                display: flex;
                justify-content: flex-end; 
                font-size: 0.75rem; 
                font-family: Arial;
            }

            .ls-chart-logo {
                height:30px;
                margin-left:10px;
                margin-right:10px;
                position:relative;
                bottom:10px
            }

        </style>
    """
    
    sourceDiv = \
    """
    {0}
    <div class="ls-chart-source-container cil-chart-source-container">
    <div class="cil-chart-data-source-container">{1}</div>
    <div class="cil-chart-logo-container"><a target="_blank" href="https://climateireland.ie">
    <img class="ls-chart-logo cil-chart-logo" src="{2}" alt="Climate Ireland"/></a></div>
    </div>
    """.format(chartStyle, sourceString, ciLogoSrc)
    
    chart.write_html(fileNoSource, config=config, include_plotlyjs=include_plotlyjs)
    html = open(fileNoSource, 'r').read()
    position = html.find('</div>') + 6
    htmlNew = html[:position] + "\n" +sourceDiv + html[position:]
    open(fileWithSource, 'w').write(htmlNew)