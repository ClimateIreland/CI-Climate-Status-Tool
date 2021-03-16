import pandas as pd
import numpy as np
import datetime
import dateutil
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from settings import *

from pages.cilPlotlyFunctions import cilPrintHTML, cilPieLayoutDict, ciStatusReportTimeSeriesLayoutDict,  cilTimeSeriesStyle, cilColorGradient, cilConfig, cilSlideTimeSeriesLayoutDict, cilSationMapLayoutDict

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

def empty_chart():
        """
        Empty chart used as placeholder for when chart or data is not found,
        or in development.
        """
        noTrace1 = go.Scatter(x=[0,1], 
                             y=[0,1],
                             marker=dict(
                                color='black')
                                )
        noTrace2 = go.Scatter(x=[0,1], 
                              y=[1,0],
                              marker=dict(
                                color='black'))

        empty_chart = go.Figure(data=[noTrace1, noTrace2])
        empty_chart.update_layout(
                    showlegend=False,
                    margin={'t':0, 'b':0}
        )

        empty_chart.add_annotation(
                x=0.5, 
                y=0.8,
                text='Error: Chart or data not found.<br>The chart may still be in development.',
                showarrow=False,
        )
        return empty_chart


def figure_2_1():
    """
    Surface Air Temperature (1900-2019) trend
    """
#     data_path = PATH.joinpath('data/Atmospheric_Domain/2.1SurfaceAirTemperature').resolve()
#     xls = pd.ExcelFile(data_path.joinpath('Figure2.1/AnnualMeanSurfaceAirTemperature1900-2019.xlsx'))
    data_path = DATA_PATH+'Atmospheric_Domain/2.1SurfaceAirTemperature/Figure2.1/'
    xls = pd.ExcelFile(data_path+'AnnualMeanSurfaceAirTemperature1900-2019.xlsx')
    dataDF = pd.read_excel(xls, 'Sheet1')
    # remove first row as part of column names, and rename Anom colum
    dataDF=dataDF[1:]
    dataDF=dataDF.rename(columns={'1961-1990 Normal':'Anom'})
    dataDF
   

    # Set the trace for annual mean, sets plot type and configurations
    annualTrace = go.Scatter(x=dataDF.Year, 
                            y=dataDF.Tmean, 
                            name='Annual Mean', 
                            mode='markers',
                            text=dataDF.Anom,
                            marker=cilTimeSeriesStyle()['markerStyleSecondary'],
                            hovertemplate='%{x}<br>' +
                            '<b>Annual</b><br>' +
                            'Tmean: %{y:.2f}\u00b0C<br>' + 
                            'Anomaly: %{text:.2f}\u00b0C<extra></extra>'
                            )
   
    movingAvgTrace = go.Scatter(x=dataDF.Year, 
                            y=dataDF.filter11, 
                            text=dataDF['Std Dev (11 year average)'],
                            name='11 Year Moving Average',
                            mode='lines', # 'line' is default 
                            line_shape = 'spline',
                            line=cilTimeSeriesStyle()['lineStylePrimary'],
                            hovertemplate='%{x}<br>' +
                                    '<b>Moving Average</b><br>' +
                                    'Anomaly: %{y:.2f}\u00b0C<extra></extra>'
                            )

    movingAvgDF=dataDF.loc[dataDF.filter11.notna()]
    linearTrendPoly=np.polyfit(movingAvgDF['Year'],movingAvgDF['filter11'],1 )
    linearTrendY = np.poly1d(linearTrendPoly)(movingAvgDF['Year'])
    linearTrendTrace = go.Scatter(x=movingAvgDF['Year'], 
                            y=linearTrendY, 
                            name='Linear Trend',
                            line=dict(color='#00a4ae',
                                    dash='dash',
                                    width=2),
                            hoverinfo='skip',
    )

    figure_2_1 = make_subplots(specs=[[{'secondary_y': True}]])

    figure_2_1.add_trace(annualTrace,
                secondary_y=True,)
    figure_2_1.add_trace(movingAvgTrace,
                secondary_y=False)
    figure_2_1.add_trace(linearTrendTrace,
                secondary_y=False)
    figure_2_1.update_layout(
                    #    title='<b>Mean Surface Air Temperature (1900-2019)</b>',
                    title_x=0.5, # Centers the title
                    height=450,
                    margin={'t':0, 'b':0,'r':0,'l':0,},  
                    plot_bgcolor='#f7fbfd',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font = dict(
                        family = 'Arial',
                        size = 13,
                        color = '#7f7f7f'
                        ),
                    hovermode='x',
                        legend=dict(
                            orientation='h',
                            #   x=0.1,
                            # y=1.06,
                            bgcolor='rgba(0,0,0,0)',
                            itemclick=False,
                            itemdoubleclick=False,
                                    ), )
    # Update y-axes layout seperatly due to the double y-axis chart
    figure_2_1.update_yaxes(title_text='Difference (\u00b0C) from 1961-1990 Normal',
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

    figure_2_1.update_yaxes(title_text='Mean Annual Temperature (\u00b0C)',
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
    figure_2_1.update_xaxes(
                    title='Year',
                    fixedrange=True, #stops the users being able to zoom
                    tickformat = '000', #number format
                    showspikes = True, #show the spike lines on hover
                    spikethickness=2, #spike line thickness
    #                  linewidth = 2, #width of axis line
    #                  linecolor = '#356b6a'
    ) # colour of axis line

    figure_2_1.add_annotation(x=2015, 
                            y=0.055,
                            text='1961-1990 Normal',
                            showarrow=False,
                            font=dict(
                                color='#E1AF00'),)

    return figure_2_1


def map_2_1():
    """
    Surface Air Temperature infrastructure map
    """
#     data_path = PATH.joinpath('data/Atmospheric_Domain/2.1SurfaceAirTemperature').resolve()
#     stationsDF = pd.read_csv(data_path.joinpath('Map2.1/Map2.1_StationTable.txt'))
    data_path = DATA_PATH+'Atmospheric_Domain/2.1SurfaceAirTemperature/Map2.1/'
    stationsDF = pd.read_csv(data_path+'Map2.1_StationTable.txt')

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
                hovertemplate= '%{text}' +
                'Lat: %{lon}\u00b0<br>' +
                'Lon: %{lat}\u00b0<br>' +
                '<extra></extra>',
    )
    synopticTrend = go.Scattermapbox(
            name='Synoptic',
            lon=synopticDF.Longitude,
            lat=synopticDF.Latitude,
            text=my_text(synopticDF),
            marker=dict(color='Red',
                        size=8),
                hovertemplate= '%{text}' +
                'Lat: %{lon}\u00b0<br>' +
                'Lon: %{lat}\u00b0<br>' +
                '<extra></extra>',
    )
    rainfallTrend = go.Scattermapbox(
            name='Rainfall',
            lon=rainfallDF.Longitude,
            lat=rainfallDF.Latitude,
            text=my_text(rainfallDF),
            marker=dict(color='Blue',
                        size=8),
                hovertemplate= '%{text}' +
                'Lat: %{lon}\u00b0<br>' +
                'Lon: %{lat}\u00b0<br>' +
                '<extra></extra>',
    )
    climateTrend = go.Scattermapbox(
            name='Climate',
            lon=climateDF.Longitude,
            lat=climateDF.Latitude,
            text=my_text(climateDF),
            marker=dict(color='green',
                        size=8),
                hovertemplate= '%{text}' +
                'Lat: %{lon}\u00b0<br>' +
                'Lon: %{lat}\u00b0<br>' +
                '<extra></extra>',
    )

    map_2_1 = go.Figure(
            data=[buoyTrend,synopticTrend, rainfallTrend, climateTrend],
            layout=cilSationMapLayoutDict())
    config={'scrollZoom': True,
            'displayModeBar': False,
            'displaylogo': False}
    map_2_1.update_layout(
            showlegend=True,
            legend=dict(orientation='v', #h for horizontal, 'v' is default
                        title='<b>Station Type</b>',
                        x=0.01)
                        )

    return map_2_1

def figure_3_15():
        """
        Dissolved Oxygen trend
        """

        data_path = DATA_PATH+'Oceanic_Domain/3.7Oxygen/Figure3.15/'
        xls = pd.ExcelFile(data_path+'DO_McSwynes_2019.xlsx')
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
                                colorbar=dict(title='Depth (m)',
                                             tickmode='array',
                                              ticktext=[0, 5, 10, 15, 20, 25, 30],
                                              tickvals=[0, -5, -10, -15, -20,-25, -30]),
                                reversescale=False,
                                
                            ),
                        showlegend=False,
                        hovertemplate='<b>Dissolved Oxygen Saturation: %{y}%</b><br>' +
                        'Date: %{x}<br>' + 
#                         'DO_Saturation.: %{y}%<br>' +
                        'Depth: %{text}m<br><extra></extra>')
        figure_3_15 = go.Figure(data=dissolvedOxygenDateTrace, layout=ciStatusReportTimeSeriesLayoutDict())
        figure_3_15.update_layout(
                yaxis=dict(title='Saturation (%)'),
                xaxis=dict(title='Year'))

        return figure_3_15

def map_3_6():
        """
        Dissolved Oxygen infrastructure map
        """

        data_path = DATA_PATH+'Oceanic_Domain/3.7Oxygen/Map3.6/'
        epaStationsDF = pd.read_csv(data_path+'Map3.6_StationTable_EPA_Stations.txt')
        maceHeadStationsDF = pd.read_csv(data_path+'Map3.6_StationTable_MaceHead.txt')
        MIStationsDF_origin = pd.read_csv(data_path+'Map3.6_StationTable_MI_SurveysStations.txt')
        smartBayStationsDF = pd.read_csv(data_path+'Map3.6_StationTable_SmartBayObservatory.txt')

        epaStationsTrace = go.Scattermapbox(
                name='EPA',
                lon=epaStationsDF.longitude,
                lat=epaStationsDF.latitude,
                text=epaStationsDF.agency,
                marker=dict(color=[stationColor[k] for k in epaStationsDF['agency'].values],
                                size=8),
                        hovertemplate= 'Type: %{text}<br>' +
                        'Lat: %{lon}\u00b0<br>' +
                        'Lon: %{lat}\u00b0<br>' +
                        '<extra></extra>',)
        
        maceHeadStationsTrace = go.Scattermapbox(
        name='Maze Head',
        lon=maceHeadStationsDF.Longitude,
        lat=maceHeadStationsDF.Latitude,
        text=maceHeadStationsDF.Type,
        marker=dict(color=[stationColor[k] for k in maceHeadStationsDF['Type'].values],
                    size=8),
            hovertemplate= 'Type: %{text}<br>' +
            'Lat: %{lon}\u00b0<br>' +
            'Lon: %{lat}\u00b0<br>' +
            '<extra></extra>',)

        MIStationsDF=pd.DataFrame()
        MIStationsDF['Station_Nu']=MIStationsDF_origin.Station.unique()

        for index, row in MIStationsDF.iterrows():
                stationRow=MIStationsDF_origin[MIStationsDF_origin.Station == row['Station_Nu']].iloc[0]
                MIStationsDF.at[index,'Latitude']=stationRow['Latitude']
                MIStationsDF.at[index,'Longitude']=stationRow['Longitude']
                MIStationsDF.at[index,'Type']='MI_Survey'

        MIStationsTrace = go.Scattermapbox(
                name='MI Survey',
                lon=MIStationsDF.Longitude,
                lat=MIStationsDF.Latitude,
                text=MIStationsDF.Type,
                marker=dict(color=[stationColor[k] for k in MIStationsDF['Type'].values],
                        size=8),
                hovertemplate= 'Type: %{text}<br>' +
                'Lat: %{lon}\u00b0<br>' +
                'Lon: %{lat}\u00b0<br>' +
                '<extra></extra>')
        
        smartBayStationsTrace = go.Scattermapbox(
        name='Wave Ride / Smart Bay',
        lon=smartBayStationsDF.Longitude,
        lat=smartBayStationsDF.Latitude,
        text=smartBayStationsDF.Type,
        marker=dict(color=[stationColor[k] for k in smartBayStationsDF['Type'].values],
                    size=8),
            hovertemplate= 'Type: %{text}<br>' +
            'Lat: %{lon}\u00b0<br>' +
            'Lon: %{lat}\u00b0<br>' +
            '<extra></extra>',)
        
        map_3_6 = go.Figure(data=[MIStationsTrace, 
                                                    epaStationsTrace, 
                                                    smartBayStationsTrace,
                                                    maceHeadStationsTrace],
                                               layout=cilSationMapLayoutDict())
        map_3_6.update_layout(
                        mapbox=dict(
                                center=dict(
                                        lat=52.5,
                                        lon=349
                                ),
                                zoom=4,))
        config={'scrollZoom': True,
                'displayModeBar': False,
                'displaylogo': False}
        map_3_6.update_layout(
                        showlegend=True,
                        legend=dict(orientation='v',
                                        title='<b>Station Type</b>',
                                        x=0.01
                                ), )
        return map_3_6

def figure_4_10_1():
        """
        Landcover 1990 Pie
        """
        # data_path = PATH.joinpath('data/Terrestrial_Domain/4.6LandCover').resolve()
        # areaDF = pd.read_excel(data_path.joinpath('Figure4.11/CorineStats_CumulativeChanges.xlsx'), header=0,  skiprows=2, nrows= 6)
        #e6e43b = agri
        #4c52f9 = wetlands
        #5ea32a = forest
        #c4fd89 = semiVeg
        #db2001 = artiSurface
        #72caf0 = waterBodies

        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx') 
        areaDF = pd.read_excel(xls, header=0,  skiprows=2, nrows= 6)
        # Tidy text by wrapping
        areaDF.loc[
                areaDF['Corine L1 Class']=='Semi-Natural & Low Vegetation','Corine L1 Class']='Semi-Natural &<br>Low Vegetation'
        area1990Trace = go.Pie(
                labels=areaDF['Corine L1 Class'], 
                values=areaDF['CLC90 Area(HA)']/1000,
                textinfo='label+percent',
                textposition= 'auto',
                marker=dict(colors=['#db2001',
                                        '#e6e43b',
                                        '#5ea32a',
                                        '#c4fd89',
                                        '#4c52f9',
                                        '#72caf0',]),
                sort=True,
                texttemplate = '<b>%{label}<br>%{percent:.1%}<b>',
                        hovertemplate='<b>%{label}</b><br>' +
                        '%{value:.0f}kHA<br>' +
                        '%{percent:.2%}<extra></extra>',
                )
        figure_4_10_1 = go.Figure(data=[area1990Trace])
        figure_4_10_1.update_layout(
                height=300,
                margin={"b": 0,"r": 0, "l": 0, "t":0},
                font=dict(
                        color = "#7f7f7f"
                        ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False)
        return figure_4_10_1

def figure_4_10_2():
        """
        Landcover 2018 Pie
        """
        # data_path = PATH.joinpath('data/Terrestrial_Domain/4.6LandCover').resolve()
        # areaDF = pd.read_excel(data_path.joinpath('Figure4.11/CorineStats_CumulativeChanges.xlsx'), header=0,  skiprows=2, nrows= 6)
        #e6e43b = agri
        #4c52f9 = wetlands
        #5ea32a = forest
        #c4fd89 = semiVeg
        #db2001 = artiSurface
        #72caf0 = waterBodies

        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx')  
        areaDF = pd.read_excel(xls, header=0,  skiprows=2, nrows= 6)
        # Tidy text by wrapping
        areaDF.loc[
                areaDF['Corine L1 Class']=='Semi-Natural & Low Vegetation','Corine L1 Class']='Semi-Natural &<br>Low Vegetation'
        area2018Trace = go.Pie(labels=areaDF['Corine L1 Class'], 
                values=areaDF['CLC18 Area(HA)']/1000,
                textinfo='label+percent',
                textposition= 'auto',
                # insidetextorientation='radial',
                # textposition= 'inside',
                marker=dict(colors=['#db2001',
                                        '#e6e43b',
                                        '#5ea32a',
                                        '#c4fd89',
                                        '#4c52f9',
                                        '#72caf0',]),
                sort=True,
                texttemplate = '<b>%{label}<br>%{percent:.1%}<b>',
                        hovertemplate='<b>%{label}</b><br>' +
                        '%{value:.0f}kHA<br>' +
                        '%{percent:.2%}<extra></extra>',
                )
        figure_4_10_2 = go.Figure(data=[area2018Trace])
        figure_4_10_2.update_layout(
                height=300,
                margin={"b": 0,"r": 0, "l": 0, "t":0},
                font=dict(
                        color = "#7f7f7f"
                        ),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False)
        return figure_4_10_2

def figure_4_11():
        """
        Landcover time series
        """
        # data_path = PATH.joinpath('data/Terrestrial_Domain/4.6LandCover').resolve()
        # xls = pd.ExcelFile(pd.read_csv(data_path.joinpath('Figure4.11/CorineStats_CumulativeChanges.xlsx')
        # dataDF = xls.parse('Summary', skiprows=2, index_col=None, na_values=['NA'])   
        # 
        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx')  
        cumChangeDF = pd.read_excel(xls, header=0,  skiprows=22, nrows= 6)
        cumChangeDF=cumChangeDF.set_index('Corine L1 Class').T
        cumChangeDF.reset_index(level=0, inplace=True)
        cumChangeNameDict={
                'index': 'Year',
                'Artificial Surfaces' : 'ArtificialSurfacesCumChange',
                'Agricultural Areas' : 'AgriculturalAreasCumChange',
                'Forest' : 'ForestCumChange',
                'Semi-Natural & Low Vegetation' : 'SemiNaturalLowVegetationsCumChange',
                'Wetlands' : 'WetlandsCumChange',
                'Water Bodies' : 'WaterBodiesCumChange',
                 }

        cumChangeDF=cumChangeDF.rename(columns=cumChangeNameDict)

        #e6e43b = agri
        #4c52f9 = wetlands
        #5ea32a = forest
        #c4fd89 = semiVeg
        #db2001 = artiSurface
        #72caf0 = waterBodies

        artificialSurfacesTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.ArtificialSurfacesCumChange, 
                                name='Artificial Surfacese', 
                                mode='lines+markers',
                                marker=dict(color='#db2001',
                                        size=4,
                                        line=dict(color='#db2001',
                                                width=0)),
                                hovertemplate='<b>Artificial Surfacese</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        agriculturalAreasTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.AgriculturalAreasCumChange, 
                                name='Agricultural Areas', 
                                mode='lines+markers',
                                marker=dict(color='#e6e43b',
                                size=4,
                                line=dict(color='#e6e43b',
                                        width=0)),
                                hovertemplate='<b>Agricultural Areas</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        forestTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.ForestCumChange, 
                                name='Forest', 
                                mode='lines+markers',
                                marker=dict(color='#5ea32a',
                                size=4,
                                line=dict(color='#5ea32a',
                                        width=0)), 
                                hovertemplate='<b>Forest</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        semiNaturalLowVegetationsTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.SemiNaturalLowVegetationsCumChange, 
                                name='Semi-Natural & Low Vegetations', 
                                mode='lines+markers',
                                marker=dict(color='#c4fd89',
                                size=4,
                                line=dict(color='#c4fd89',
                                        width=0)),
                                hovertemplate='<b>Semi-Natural & Low Vegetations</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        wetlandsTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.WetlandsCumChange, 
                                name='Wetlands', 
                                mode='lines+markers',
                                marker=dict(color='#4c52f9',
                                                size=4,
                                                line=dict(color='#4c52f9',
                                                        width=0)),
                                hovertemplate='<b>Wetlands</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        waterBodiesTrace = go.Scatter(x=cumChangeDF.Year, 
                                y=cumChangeDF.WaterBodiesCumChange, 
                                name='Water Bodies', 
                                mode='lines+markers',
                                marker=dict(color='#72caf0',
                                size=4,
                                line=dict(color='#72caf0',
                                        width=0)),
                                hovertemplate='<b>Water Bodies</b><br>' +
                                'Year: %{x}<br>' + 
                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

        data=[artificialSurfacesTrace,
                                agriculturalAreasTrace,
                                forestTrace,
                                semiNaturalLowVegetationsTrace,
                                wetlandsTrace,
                                waterBodiesTrace]

        # landcoverCumChangeChart=go.Figure(data=data, layout=cilSlideTimeSeriesLayoutDict())
        # landcoverCumChangeChart.update_layout(
                # title_text='<b>Percentage of Cumulative Change within Each Class</b>',
                                #         height=450,
                                # legend=dict(orientation='h', #h for horizontal, 'v' is default
                                # x=0, 
                                # y=0
                                # ), )
        figure_4_11=go.Figure(data=data)
        figure_4_11.update_layout(
                    height=450,
                    margin={'t':0, 'b':0,'r':0,'l':0,},  
                    plot_bgcolor='#f7fbfd',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font = dict(
                        # family = 'Arial',
                        # size = 13,
                        color = '#7f7f7f'
                        ),
                    hovermode='closest',
                        legend=dict(
                            orientation='h',
                            #   x=0.1,
                            y=-0.15,
                            bgcolor='rgba(0,0,0,0)',
                        #     itemclick=False,
                        #     itemdoubleclick=False,
                                    ), )
        figure_4_11.update_yaxes(title_text='<b>Percentage (%)</b>',
                                tickformat=',.0%',)
        figure_4_11.update_xaxes(title_text='<b>Year</b>')

        return figure_4_11


def figure_4_12():
        """
        FAPAR Trend
        """
        # data_path = PATH.joinpath('data/Terrestrial_Domain/4.7FAPAR').resolve()
        # xls = pd.ExcelFile(data_path.joinpath('Figure4.12/FAPAR_CopernicusLandService_10Days_OverIreland_v2.xlsx'))

        data_path = DATA_PATH+'Terrestrial_Domain/4.7FAPAR/Figure4.12/'
        xls = pd.ExcelFile(data_path+'FAPAR_CopernicusLandService_10Days_OverIreland_v2.xlsx')
        dataDF = pd.read_excel(xls, 'FAPAR_10_Daily_OverIreland')  
        faparDF=pd.DataFrame()
        faparDF['Date']=dataDF['Unnamed: 1'].dt.date
        faparDF['Year']=dataDF['Unnamed: 1'].dt.year
        faparDF['Month']=dataDF['Unnamed: 1'].dt.month
        faparDF['Day']=dataDF['Unnamed: 1'].dt.day
        faparDF['Mean']=dataDF['Mean']
        faparDF['Min']=dataDF['Min']
        faparDF['Max']=dataDF['Max']

        for index, row in faparDF.iterrows():
                if row.Month==1 and row.Day<12:
                        faparDF.at[index,'xAxis']=1
                elif row.Month==1 and row.Day<22:
                        faparDF.at[index,'xAxis']=2
                elif row.Month==1 and row.Day<32:
                        faparDF.at[index,'xAxis']=3
                
                elif row.Month==2 and row.Day<12:
                        faparDF.at[index,'xAxis']=4
                elif row.Month==2 and row.Day<22:
                        faparDF.at[index,'xAxis']=5
                elif row.Month==2 and row.Day<32:
                        faparDF.at[index,'xAxis']=6
                        
                elif row.Month==3 and row.Day<12:
                        faparDF.at[index,'xAxis']=7
                elif row.Month==3 and row.Day<22:
                        faparDF.at[index,'xAxis']=8
                elif row.Month==3 and row.Day<32:
                        faparDF.at[index,'xAxis']=9
                        
                elif row.Month==4 and row.Day<12:
                        faparDF.at[index,'xAxis']=10
                elif row.Month==4 and row.Day<22:
                        faparDF.at[index,'xAxis']=11
                elif row.Month==4 and row.Day<32:
                        faparDF.at[index,'xAxis']=12
                        
                elif row.Month==5 and row.Day<12:
                        faparDF.at[index,'xAxis']=13
                elif row.Month==5 and row.Day<22:
                        faparDF.at[index,'xAxis']=14
                elif row.Month==5 and row.Day<32:
                        faparDF.at[index,'xAxis']=15
                        
                elif row.Month==6 and row.Day<12:
                        faparDF.at[index,'xAxis']=16
                elif row.Month==6 and row.Day<22:
                        faparDF.at[index,'xAxis']=17
                elif row.Month==6 and row.Day<32:
                        faparDF.at[index,'xAxis']=18
                        
                elif row.Month==7 and row.Day<12:
                        faparDF.at[index,'xAxis']=19
                elif row.Month==7 and row.Day<22:
                        faparDF.at[index,'xAxis']=20
                elif row.Month==7 and row.Day<32:
                        faparDF.at[index,'xAxis']=21
                        
                elif row.Month==8 and row.Day<12:
                        faparDF.at[index,'xAxis']=22
                elif row.Month==8 and row.Day<22:
                        faparDF.at[index,'xAxis']=23
                elif row.Month==8 and row.Day<32:
                        faparDF.at[index,'xAxis']=24
                
                elif row.Month==9 and row.Day<12:
                        faparDF.at[index,'xAxis']=25
                elif row.Month==9 and row.Day<22:
                        faparDF.at[index,'xAxis']=26
                elif row.Month==9 and row.Day<32:
                        faparDF.at[index,'xAxis']=27
                        
                elif row.Month==10 and row.Day<12:
                        faparDF.at[index,'xAxis']=28
                elif row.Month==10 and row.Day<22:
                        faparDF.at[index,'xAxis']=29
                elif row.Month==10 and row.Day<32:
                        faparDF.at[index,'xAxis']=30
                        
                elif row.Month==11 and row.Day<12:
                        faparDF.at[index,'xAxis']=31
                elif row.Month==11 and row.Day<22:
                        faparDF.at[index,'xAxis']=32
                elif row.Month==11 and row.Day<32:
                        faparDF.at[index,'xAxis']=33
                        
                elif row.Month==12 and row.Day<12:
                        faparDF.at[index,'xAxis']=34
                elif row.Month==12 and row.Day<22:
                        faparDF.at[index,'xAxis']=35
                elif row.Month==12 and row.Day<32:
                        faparDF.at[index,'xAxis']=36
        my_text=['Date: '+'{}'.format(date)+'<br>'+
         'Min: '+'{}'.format(mn)+'<br>'+
         'Max: '+'{}'.format(mx)+'<br>'
         for date, mn, mx, in zip(list(faparDF['Date']), 
                                  list(faparDF['Min']), 
                                     list(faparDF['Max'])
                                                            )]
        colorscale=[
                # 5% are to be purple
                [0.0, 'rgb(98, 55, 155)'],
                [0.08, 'rgb(98, 55, 155)'],
                # 20% are to be blue
                [0.08, 'rgb(184, 197, 229)'],
                [0.28, 'rgb(184, 197, 229)'],
                # 25% are to be green
                [0.28, 'rgb(166, 206, 93)'],
                [0.507, 'rgb(166, 206, 93)'],
                # 25% are to be yellow
                [0.507, 'rgb(255, 254, 66)'],
                [0.77, 'rgb(255, 254, 66)'],
                # 20% are to be orange
                [0.77, 'rgb(239, 191, 49)'],
                [0.92, 'rgb(239, 191, 49)'],
                # 5% are to be red
                [0.92, 'rgb(219, 32, 1)'],
                [1.0, 'rgb(219, 32, 1)'],
        ]
        date_list=[datetime.date.today()- dateutil.relativedelta.relativedelta(months = x) for x in range(11,-1,-1)]
        month_list=[datetime.date.strftime(x,'%b') for x in date_list]
        faparTrace = go.Heatmap(
                        z=faparDF.Mean,
                        x=faparDF.xAxis,
                        y=faparDF.Year,
                        text=my_text,
        #                     colorscale=['purple', 'lightblue', 'lightgreen', 'yellow', 'lightorange', 'orange','red'],
        #                     colorscale='rdylbu_r',
                        colorscale=colorscale,
                        colorbar=dict(title='Mean (%)',
                                        tickmode='array',
                                        ticktext=['<50', '50-56', '56-65', '65-72', '72-76', '>76'],
                                        tickvals=[0.48, 0.52, 0.59, 0.67, 0.735, 0.77]),
                        hovertemplate='<b>Mean: %{z:.1%}</b><br>' +
                                '%{text}' +
                                '<extra></extra>')

        figure_4_12 = go.Figure(data=faparTrace, layout=ciStatusReportTimeSeriesLayoutDict())
        figure_4_12.update_layout(
                # title_text='<b>10-day average FAPAR over Ireland</b>',
                yaxis=dict(title='Year',
                        nticks=20),
                xaxis=dict(title='Month',
                        ticktext=month_list,
                        showgrid=True, gridwidth=3, gridcolor='black',
                        tickvals=[2,5,8,11,14,17,20,23,26,29,32,35],))
        figure_4_12.add_shape(type='line',
        x0=3.5, y0=1998.6, x1=3.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=6.5, y0=1998.6, x1=6.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=9.5, y0=1998.6, x1=9.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=12.5, y0=1998.6, x1=12.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=15.5, y0=1998.6, x1=15.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=18.5, y0=1998.6, x1=18.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=21.5, y0=1998.6, x1=21.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=24.5, y0=1998.6, x1=24.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=27.5, y0=1998.6, x1=27.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=30.5, y0=1998.6, x1=30.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        figure_4_12.add_shape(type='line',
        x0=33.5, y0=1998.6, x1=33.5, y1=2018.4,
        line=dict(color='White',width=3)
        )
        return figure_4_12













