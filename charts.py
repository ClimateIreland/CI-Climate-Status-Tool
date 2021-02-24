import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from pages.cilPlotlyFunctions import cilPrintHTML, ciStatusReportTimeSeriesLayoutDict,  cilTimeSeriesStyle, cilColorGradient, cilConfig, cilSlideTimeSeriesLayoutDict, cilSationMapLayoutDict

import pathlib


PATH = pathlib.Path(__file__).parent

stationColor = {
    'Buoy':'yellow',
    'Synoptic':'red',
    'Rainfall':'blue',
    'Climate':'green',
    'WaveRide/SmartBayObsCenter':'orange',
    'MI_Survey':'darkblue',
    'EPA':'purple'
}

def surfaceAirTempChart():
    data_path = PATH.joinpath("data/Atmospheric_Domain/2.1SurfaceAirTemperature").resolve()
    xls = pd.ExcelFile(data_path.joinpath('Figure2.1/AnnualMeanSurfaceAirTemperature1900-2019.xlsx'))
    dataDF = pd.read_excel(xls, "Sheet1")
    # remove first row as part of column names, and rename Anom colum
    dataDF=dataDF[1:]
    dataDF=dataDF.rename(columns={"1961-1990 Normal":"Anom"})
    dataDF
   

    # Set the trace for annual mean, sets plot type and configurations
    annualTrace = go.Scatter(x=dataDF.Year, 
                            y=dataDF.Tmean, 
                            name='Annual Mean', 
                            mode='markers',
                            text=dataDF.Anom,
                            marker=cilTimeSeriesStyle()['markerStyleSecondary'],
                            hovertemplate="%{x}<br>" +
                            "<b>Annual</b><br>" +
                            "Tmean: %{y:.2f}\u00b0C<br>" + 
                            "Anomaly: %{text:.2f}\u00b0C<extra></extra>"
                            )
    # Set the trace for movingAvg, sets plot type and configurations
    movingAvgTrace = go.Scatter(x=dataDF.Year, 
                            y=dataDF.filter11, 
                            text=dataDF['Std Dev (11 year average)'],
                            name='11 Year Moving Average',
                            mode='lines', # 'line' is default 
                            line_shape = 'spline',
                            line=cilTimeSeriesStyle()['lineStylePrimary'],
                            hovertemplate="%{x}<br>" +
                                    "<b>Moving Average</b><br>" +
                                    "Anomaly: %{y:.2f}\u00b0C<extra></extra>"
                            )

    movingAvgDF=dataDF.loc[dataDF.filter11.notna()]
    linearTrendPoly=np.polyfit(movingAvgDF["Year"],movingAvgDF["filter11"],1 )
    linearTrendY = np.poly1d(linearTrendPoly)(movingAvgDF["Year"])
    linearTrendTrace = go.Scatter(x=movingAvgDF["Year"], 
                            y=linearTrendY, 
                            name='Linear Trend',
                            line=dict(color='#00a4ae',
                                    dash='dash',
                                    width=2),
                            hoverinfo='skip',
    )

    satChart = make_subplots(specs=[[{"secondary_y": True}]])

    # satChart.add_trace(normalTrace,
    #                secondary_y=False)
    satChart.add_trace(annualTrace,
                secondary_y=True,)
    satChart.add_trace(movingAvgTrace,
                secondary_y=False)
    satChart.add_trace(linearTrendTrace,
                secondary_y=False)
    satChart.update_layout(
                    #    title="<b>Mean Surface Air Temperature (1900-2019)</b>",
                    title_x=0.5, # Centers the title
                    height=450,
                    margin={"t":0, "b":0,"r":0,"l":0,},  
                    plot_bgcolor='#f7fbfd',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font = dict(
                        family = "Arial",
                        size = 13,
                        color = "#7f7f7f"
                        ),
                    hovermode="x",
                        legend=dict(
                            orientation="h",
                            #   x=0.1,
                            # y=1.06,
                            bgcolor='rgba(0,0,0,0)',
                            itemclick=False,
                            itemdoubleclick=False,
    #                        legend=dict(
    #                            title='<b>         Legend</b>',
    #                            orientation="v",
    #                           x=0.01,
    #                           bgcolor='rgba(0,0,0,0)',
    #                           itemclick=False,
    #                           itemdoubleclick=False,
                                    ), )
    # Update y-axes layout seperatly due to the double y-axis chart
    satChart.update_yaxes(title_text="Difference (\u00b0C) from 1961-1990 Normal",
                    secondary_y=False,
                    range=[-0.9,1.3],
                    showgrid=False,
                    dtick=0.5, # dtick sets the distance between ticks
                    tick0=0, # tick0 sets a point to map the other ticks 
                    fixedrange = True,
                    showspikes = True,
                    zeroline = True, #add a zero line 
                    zerolinecolor = '#E1AF00', #colour of zero line 
    #                   linewidth = 2,
    #                   spikethickness = 2,
    #                   linecolor = '#356b6a'
                        )

    satChart.update_yaxes(title_text="Mean Annual Temperature (\u00b0C)",
                    secondary_y=True,
                    range=[8.65,10.85],
                    showgrid=False,
                    dtick=0.5, # dtick sets the distance between ticks
                    tick0=9.55, # tick0 sets a point to map the other ticks 
                    fixedrange = True,
    #                      linewidth = 2,
    #                   spikethickness = 2,
    #                   linecolor = '#356b6a'
                        )
                            
    # X AXIS
    satChart.update_xaxes(
                    title='Year',
                    fixedrange=True, #stops the users being able to zoom
                    tickformat = "000", #number format
                    showspikes = True, #show the spike lines on hover
                    spikethickness=2, #spike line thickness
    #                  linewidth = 2, #width of axis line
    #                  linecolor = '#356b6a'
    ) # colour of axis line

    satChart.add_annotation(x=2015, 
                            y=0.055,
                            text="1961-1990 Normal",
                            showarrow=False,
                            font=dict(
                                color='#E1AF00'),)

    return satChart


def surfaceAirTempStationsMap():
    data_path = PATH.joinpath("data/Atmospheric_Domain/2.1SurfaceAirTemperature").resolve()
    stationsDF = pd.read_csv(data_path.joinpath("Map2.1/Map2.1_StationTable.txt"))

    def my_text(df):
        my_text=['Name: '+'{}'.format(n)+'<br>'+
            'Type: '+'{}'.format(t)+'<br>'+
            'Station No.: '+'{}'.format(sN)+'<br>'+
            'County.: '+'{}'.format(cnty)+'<br>'+
            'Open Year.: '+'{}'.format(oY)+'<br>'+
            'Height: '+'{:.2f}'.format(h)+'m<br>'+
            'Easting: '+'{}'.format(easting)+'<br>'+
            'Northing: '+'{}'.format(northing)+'<br>'
            for n, t, sN, cnty, oY, h, easting, northing in zip(list(df['name']), 
                                        list(stationsDF['Type']), 
                                        list(stationsDF['Station_Nu']), 
                                        list(stationsDF['County']),
                                        list(stationsDF['Open_Year']),
                                        list(stationsDF['Height__m_']),
                                        list(stationsDF['Easting']),
                                        list(stationsDF['Northing']),
                                                                )]
        return my_text

    buoyDF=stationsDF.loc[stationsDF['Type'] == 'Buoy']
    synopticDF=stationsDF.loc[stationsDF['Type'] == 'Synoptic']
    rainfallDF=stationsDF.loc[stationsDF['Type'] == 'Rainfall']
    climateDF=stationsDF.loc[stationsDF['Type'] == 'Climate']

    buoyTrend = go.Scattermapbox(
            name='Buoys',
            lon=buoyDF.Longitude,
            lat=buoyDF.Latitude,
            text=my_text(buoyDF),
            marker=dict(color='Yellow',
                        size=8),
                hovertemplate= "%{text}" +
                "Lat: %{lon}\u00b0<br>" +
                "Lon: %{lat}\u00b0<br>" +
                "<extra></extra>",
    )
    synopticTrend = go.Scattermapbox(
            name='Synoptic',
            lon=synopticDF.Longitude,
            lat=synopticDF.Latitude,
            text=my_text(synopticDF),
            marker=dict(color='Red',
                        size=8),
                hovertemplate= "%{text}" +
                "Lat: %{lon}\u00b0<br>" +
                "Lon: %{lat}\u00b0<br>" +
                "<extra></extra>",
    )
    rainfallTrend = go.Scattermapbox(
            name='Rainfall',
            lon=rainfallDF.Longitude,
            lat=rainfallDF.Latitude,
            text=my_text(rainfallDF),
            marker=dict(color='Blue',
                        size=8),
                hovertemplate= "%{text}" +
                "Lat: %{lon}\u00b0<br>" +
                "Lon: %{lat}\u00b0<br>" +
                "<extra></extra>",
    )
    climateTrend = go.Scattermapbox(
            name='Climate',
            lon=climateDF.Longitude,
            lat=climateDF.Latitude,
            text=my_text(climateDF),
            marker=dict(color='green',
                        size=8),
                hovertemplate= "%{text}" +
                "Lat: %{lon}\u00b0<br>" +
                "Lon: %{lat}\u00b0<br>" +
                "<extra></extra>",
    )

    surfaceTempStationMap = go.Figure(data=[buoyTrend, 
    synopticTrend, 
    rainfallTrend, 
    climateTrend],layout=cilSationMapLayoutDict())
    config={"scrollZoom": True,
            'displayModeBar': False,
            'displaylogo': False}
    surfaceTempStationMap.update_layout(
            showlegend=True,
                        legend=dict(orientation="v", #h for horizontal, 'v' is default
                                    title='<b>Station Type</b>',
                                    x=0.01
                                ), 
    )

    return surfaceTempStationMap

def dissolvedOxygenTrend():
        data_path = PATH.joinpath("data/Oceanic_Domain/3.7Oxygen").resolve()
        xls = pd.ExcelFile(data_path.joinpath('Figure3.15/DO_McSwynes_2019.xlsx'))
        dataDF = xls.parse('ECWM_Datasonde', skiprows=1, index_col=None, na_values=['NA'])
        dissolvedOxygenDateTrace = go.Scatter(x=dataDF.date_Surveyed, 
                        y=dataDF.DO_saturation, 
                        name='Dissolved Oxygen Saturation', 
                        mode='markers',
                        text=dataDF.Depth_sample,
#                         marker=cilTimeSeriesStyle()['markerStylePrimary'],
                        marker=dict(
                                size=4,
                                color=dataDF.Depth_sample*(-1), #set color equal to a variable
                                colorscale='Viridis', # one of plotly colorscales
                                showscale=True,
                                colorbar=dict(title="Depth (m)",
                                             tickmode="array",
                                              ticktext=[0, 5, 10, 15, 20, 25, 30],
                                              tickvals=[0, -5, -10, -15, -20,-25, -30]),
                                reversescale=False,
                                
                            ),
                        showlegend=False,
                        hovertemplate="<b>Dissolved Oxygen Saturation: %{y}%</b><br>" +
                        "Date: %{x}<br>" + 
#                         "DO_Saturation.: %{y}%<br>" +
                        "Depth: %{text}m<br><extra></extra>")
        dissolvedOxygenDateChart = go.Figure(data=dissolvedOxygenDateTrace, layout=ciStatusReportTimeSeriesLayoutDict())
        dissolvedOxygenDateChart.update_layout(
                yaxis=dict(title="Saturation (%)"),
                xaxis=dict(title="Year"))

        return dissolvedOxygenDateChart

def dissolvedOxygenStationsMap():
        data_path = PATH.joinpath("data/Oceanic_Domain/3.7Oxygen").resolve()
        epaStationsDF = pd.read_csv(data_path.joinpath("Map3.6/Map3.6_StationTable_EPA_Stations.txt"))
        maceHeadStationsDF = pd.read_csv(data_path.joinpath("Map3.6/Map3.6_StationTable_MaceHead.txt"))
        MIStationsDF_origin = pd.read_csv(data_path.joinpath("Map3.6/Map3.6_StationTable_MI_SurveysStations.txt"))
        smartBayStationsDF = pd.read_csv(data_path.joinpath("Map3.6/Map3.6_StationTable_SmartBayObservatory.txt"))

        epaStationsTrace = go.Scattermapbox(
                name="EPA",
                lon=epaStationsDF.longitude,
                lat=epaStationsDF.latitude,
                text=epaStationsDF.agency,
                marker=dict(color=[stationColor[k] for k in epaStationsDF['agency'].values],
                                size=8),
                        hovertemplate= "Type: %{text}<br>" +
                        "Lat: %{lon}\u00b0<br>" +
                        "Lon: %{lat}\u00b0<br>" +
                        "<extra></extra>",)
        
        maceHeadStationsTrace = go.Scattermapbox(
        name="Maze Head",
        lon=maceHeadStationsDF.Longitude,
        lat=maceHeadStationsDF.Latitude,
        text=maceHeadStationsDF.Type,
        marker=dict(color=[stationColor[k] for k in maceHeadStationsDF['Type'].values],
                    size=8),
            hovertemplate= "Type: %{text}<br>" +
            "Lat: %{lon}\u00b0<br>" +
            "Lon: %{lat}\u00b0<br>" +
            "<extra></extra>",)

        MIStationsDF=pd.DataFrame()
        MIStationsDF['Station_Nu']=MIStationsDF_origin.Station.unique()

        for index, row in MIStationsDF.iterrows():
                stationRow=MIStationsDF_origin[MIStationsDF_origin.Station == row['Station_Nu']].iloc[0]
                MIStationsDF.at[index,'Latitude']=stationRow['Latitude']
                MIStationsDF.at[index,'Longitude']=stationRow['Longitude']
                MIStationsDF.at[index,'Type']='MI_Survey'

        MIStationsTrace = go.Scattermapbox(
                name="MI Survey",
                lon=MIStationsDF.Longitude,
                lat=MIStationsDF.Latitude,
                text=MIStationsDF.Type,
                marker=dict(color=[stationColor[k] for k in MIStationsDF['Type'].values],
                        size=8),
                hovertemplate= "Type: %{text}<br>" +
                "Lat: %{lon}\u00b0<br>" +
                "Lon: %{lat}\u00b0<br>" +
                "<extra></extra>")
        
        smartBayStationsTrace = go.Scattermapbox(
        name="Wave Ride / Smart Bay",
        lon=smartBayStationsDF.Longitude,
        lat=smartBayStationsDF.Latitude,
        text=smartBayStationsDF.Type,
        marker=dict(color=[stationColor[k] for k in smartBayStationsDF['Type'].values],
                    size=8),
            hovertemplate= "Type: %{text}<br>" +
            "Lat: %{lon}\u00b0<br>" +
            "Lon: %{lat}\u00b0<br>" +
            "<extra></extra>",)
        
        dissolvedOxygenStationMap = go.Figure(data=[MIStationsTrace, 
                                                    epaStationsTrace, 
                                                    smartBayStationsTrace,
                                                    maceHeadStationsTrace],
                                               layout=cilSationMapLayoutDict())
        dissolvedOxygenStationMap.update_layout(
                        mapbox=dict(
                                center=dict(
                                        lat=52.5,
                                        lon=349
                                ),
                                zoom=4,))
        config={"scrollZoom": True,
                'displayModeBar': False,
                'displaylogo': False}
        dissolvedOxygenStationMap.update_layout(
                        showlegend=True,
                        legend=dict(orientation="v",
                                        title='<b>Station Type</b>',
                                        x=0.01
                                ), )
        return dissolvedOxygenStationMap











