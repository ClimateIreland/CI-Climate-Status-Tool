import pandas as pd
import numpy as np
import datetime
import dateutil
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from settings import *




def stations_map(df):

    def stations_map_hovertemplate(df):
        return ['Name: '+'{}'.format(n)+'<br>' +
                'Type: '+'{}'.format(t)+'<br>' +
                'Station No.: '+'{}'.format(sN)+'<br>' +
                'County.: '+'{}'.format(cnty)+'<br>' +
                'Open Year.: '+'{}'.format(oY)+'<br>' +
                'Height: '+'{:.2f}'.format(h)+'m<br>' +
                'Easting: '+'{}'.format(easting)+'<br>' +
                'Northing: '+'{}'.format(northing)+'<br>'
                'Lat: '+'{:.2f}'.format(lat)+'\u00b0<br>' +
                'Lon: '+'{:.2f}'.format(lon)+'\u00b0<br>' + '<extra></extra>'
                for n, t, sN, cnty, oY, h, easting, northing, lat, lon in zip(list(df['name']),
                                                                            list(
                    df['Type']),
            list(
                    df['Station_Nu']),
            list(
                    df['County']),
            list(
                    df['Open_Year']),
            list(
                    df['Height__m_']),
            list(
                    df['Easting']),
            list(
                    df['Northing']),
            list(
                    df['Latitude']),
            list(
                    df['Longitude']),
        )]

    buoyDF = df.loc[df['Type'] == 'Buoy']
    synopticDF = df.loc[df['Type'] == 'Synoptic']
    rainfallDF = df.loc[df['Type'] == 'Rainfall']
    climateDF = df.loc[df['Type'] == 'Climate']

    buoyTrend = go.Scattermapbox(
        name='Buoys',
        lon=buoyDF.Longitude,
        lat=buoyDF.Latitude,
        marker=dict(color=STATION_COLORS['Buoy'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(buoyDF),
    )
    rainfallTrend = go.Scattermapbox(
        name='Rainfall',
        lon=rainfallDF.Longitude,
        lat=rainfallDF.Latitude,
        marker=dict(color=STATION_COLORS['Rainfall'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(rainfallDF),
    )

    synopticTrend = go.Scattermapbox(
        name='Synoptic',
        lon=synopticDF.Longitude,
        lat=synopticDF.Latitude,
        marker=dict(color=STATION_COLORS['Synoptic'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(synopticDF),
    )

    climateTrend = go.Scattermapbox(
        name='Climate',
        lon=climateDF.Longitude,
        lat=climateDF.Latitude,
        marker=dict(color=STATION_COLORS['Climate'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(climateDF),
    )
    stations_map = go.Figure(
        data=[buoyTrend, synopticTrend, rainfallTrend, climateTrend],
        layout=MAP_LAYOUT)
    
    return stations_map


def empty_chart():
    """
    Empty chart used as placeholder for when chart or data is not found,
    or in development.
    """
    noTrace1 = go.Scatter(x=[0, 1],
                          y=[0, 1],
                          marker=dict(
        color='black')
    )
    noTrace2 = go.Scatter(x=[0, 1],
                          y=[1, 0],
                          marker=dict(
        color='black'))

    empty_chart = go.Figure(data=[noTrace1, noTrace2])
    empty_chart.update_layout(
        showlegend=False,
        margin={'t': 0, 'b': 0}
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

    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.1SurfaceAirTemperature/Figure2.1/'
        xls = pd.ExcelFile(
            data_path+'AnnualMeanSurfaceAirTemperature1900-2019.xlsx')
        dataDF = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()
    # remove first row as part of column names, and rename Anom colum
    dataDF = dataDF[1:]
    dataDF = dataDF.rename(columns={'1961-1990 Normal': 'Anom'})
    dataDF

    movingAvgTrace = go.Scatter(x=dataDF.Year,
                                y=dataDF.filter11,
                                text=dataDF['Std Dev (11 year average)'],
                                name='11 Year Moving Average',
                                mode='lines',  # 'line' is default
                                line_shape='spline',
                                line=dict(color=TIMESERIES_COLOR_PRIMARY,
                                          width=2),
                                hovertemplate='%{x}<br>' +
                                '<b>Moving Average</b><br>' +
                                'Anomaly: %{y:.2f}\u00b0C<extra></extra>'
                                )
    annualTrace = go.Scatter(x=dataDF.Year,
                             y=dataDF.Tmean,
                             name='Annual Mean',
                             mode='markers',
                             text=dataDF.Anom,
                             marker=dict(color=TIMESERIES_COLOR_SECONDARY,
                                         size=5,
                                         opacity=0.5),
                             hovertemplate='%{x}<br>' +
                             '<b>Annual</b><br>' +
                             'Tmean: %{y:.2f}\u00b0C<br>' +
                             'Anomaly: %{text:.2f}\u00b0C<extra></extra>'
                             )

    movingAvgDF = dataDF.loc[dataDF.filter11.notna()]
    linearTrendPoly = np.polyfit(
        movingAvgDF['Year'], movingAvgDF['filter11'], 1)
    linearTrendY = np.poly1d(linearTrendPoly)(movingAvgDF['Year'])
    linearTrendTrace = go.Scatter(x=movingAvgDF['Year'],
                                  y=linearTrendY,
                                  name='Linear Trend',
                                  line=dict(color=TIMESERIES_COLOR_PRIMARY,
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
    figure_2_1.update_layout(TIMESERIES_LAYOUT)
    # Update y-axes layout seperatly due to the double y-axis chart
    figure_2_1.update_yaxes(title_text='Difference (\u00b0C) from 1961-1990 Normal',
                            secondary_y=False,
                            range=[-0.9, 1.3],
                            showgrid=False,
                            dtick=0.5,  # dtick sets the distance between ticks
                            tick0=0,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            showspikes=True,
                            zeroline=True,  # add a zero line
                            zerolinecolor=TIMESERIES_COLOR_SECONDARY
                            )

    figure_2_1.update_yaxes(title_text='Mean Annual Temperature (\u00b0C)',
                            secondary_y=True,
                            range=[8.65, 10.85],
                            showgrid=False,
                            dtick=0.5,  # dtick sets the distance between ticks
                            tick0=9.55,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            #                      linewidth = 2,
                            #                   spikethickness = 2,
                            #                   linecolor = '#356b6a'
                            )

    figure_2_1.update_xaxes(
        title='Year',
        fixedrange=True,  # stops the users being able to zoom
        tickformat='000',  # number format
        showspikes=True,  # show the spike lines on hover
        spikethickness=2,  # spike line thickness
        #                  linewidth = 2, #width of axis line
        #                  linecolor = '#356b6a'
    )  # colour of axis line

    figure_2_1.add_annotation(x=2015,
                              y=0.055,
                              text='1961-1990 Normal',
                              showarrow=False,
                              font=dict(
                                  color=TIMESERIES_COLOR_SECONDARY),)

    return figure_2_1


def map_2_1():
    """
    Surface Air Temperature infrastructure map
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.1SurfaceAirTemperature/Map2.1/'
        df = pd.read_csv(data_path+'Map2.1_StationTable.txt')
    except:
        return empty_chart()
    map_2_1=stations_map(df)
    return map_2_1

def figure_2_9():
    """
    Precipitation Totals and Anomalies Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.5Precipitation/Figure2.9/'
        xls = pd.ExcelFile(
            data_path+'Annual_rainfall_totals_and_anomalies_OverIreland.xlsx')
        dataDF = pd.read_excel(xls, '2010SeasannRR')
    except:
        return empty_chart()

    dataDF.rename(columns={
        "Unnamed: 3": "11 Year Moving Average Totals",
        "Unnamed: 4": "Anomaly",
        "11 year moving average": "11 Year Moving Average Anomaly"
    }, inplace=True)
    movingAverageTotals = dataDF.ANN.rolling(window=11, center=True).mean()
    dataDF["11 Year Average"] = movingAverageTotals

    annualTrace = go.Bar(x=dataDF["years"],
                         y=dataDF["Anomaly"],
                         text=dataDF["ANN"],
                         name='Annual',
                         marker=dict(
        # color="#214a7b", color used in report
        color=TIMESERIES_COLOR_SECONDARY,
        opacity=0.5
    ),
        hovertemplate='%{x}<br>' +
        '<b>Annual</b><br>' +
        'Total: %{text:.2f}mm<br>' +
        'Anomaly: %{y:.2f}mm<extra></extra>'
    )
    movingAverage = go.Scatter(x=dataDF["years"],
                               y=dataDF["11 Year Moving Average Anomaly"],
                               text=dataDF["11 Year Moving Average Totals"],
                               name='11yr Moving Average',
                               mode='lines',  # 'line' is default
                               line_shape='spline',
                               line=dict(
        # color="#fc0d1b", color used in report
        color=TIMESERIES_COLOR_PRIMARY,
        width=2),
        hovertemplate='%{x}<br>' +
        '<b>11yr Moving Average</b><br>' +
        'Total: %{text:.2f}mm<br>' +
        'Anomaly: %{y:.2f}mm<extra></extra>'
    )
    normal = go.Scatter(x=dataDF["years"],
                        y=dataDF["ANNmean"],
                        name='1961-1990 Normal',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(color="#22b2ed",  # color used in report
                                  width=1),
                        hoverinfo='skip',
                        )
    average1990_2019 = go.Scatter(x=dataDF["years"],
                                  y=dataDF["1990-2019 Average"],
                                  name='1990-2019 Average',
                                  mode='lines',  # 'line' is default
                                  line_shape='spline',
                                  line=dict(color="#22b2ed",  # color used in report
                                  dash='dash',
                                  width=1),
                                  hoverinfo='skip',
                                  )
    figure_2_9 = make_subplots(specs=[[{'secondary_y': True}]])
    figure_2_9.add_trace(annualTrace,
                         secondary_y=False,)
    figure_2_9.add_trace(movingAverage,
                         secondary_y=False,)
    figure_2_9.add_trace(normal,
                         secondary_y=True,)

    figure_2_9.add_trace(average1990_2019,
                         secondary_y=False,)

    figure_2_9.update_layout(TIMESERIES_LAYOUT)
    figure_2_9.update_yaxes(title_text='Difference (mm) from 1961-1990 Normal',
                            secondary_y=False,
                            range=[-300, 330],
                            showgrid=False,
                            dtick=100,  # dtick sets the distance between ticks
                            tick0=0,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            showspikes=True,
                            # zeroline=True,  # add a zero line
                            # zerolinecolor=TIMESERIES_COLOR_SECONDARY
                            )
    figure_2_9.update_yaxes(title_text='Annual Rainfall Total (mm)',
                            secondary_y=True,
                            range=[886, 1517],
                            showgrid=False,
                            dtick=100,  # dtick sets the distance between ticks
                            tick0=1186,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            )

    figure_2_9.update_xaxes(
        title='Year',
        fixedrange=True,
        tickformat='000',
        showspikes=True,
        spikethickness=2,
    )
    return figure_2_9

def map_2_5():
    """
    Precipitation infrastructure map
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.5Precipitation/Map2.5/'
        df = pd.read_csv(data_path+'Map2.5_StationTable.txt')
    except:
        return empty_chart()
    map_2_5=stations_map(df)
    return map_2_5

def figure_3_15():
    """
    Dissolved Oxygen trend
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.7Oxygen/Figure3.15/'
        xls = pd.ExcelFile(data_path+'DO_McSwynes_2019.xlsx')
    except:
        return empty_chart()
    dataDF = xls.parse('ECWM_Datasonde', skiprows=1,
                       index_col=None, na_values=['NA'])
    dissolvedOxygenDateTrace = go.Scatter(x=dataDF.date_Surveyed,
                                          y=dataDF.DO_saturation,
                                          name='Dissolved Oxygen Saturation',
                                          mode='markers',
                                          text=dataDF.Depth_sample,
                                          marker=dict(
                                              size=4,
                                              # set color equal to a variable
                                              color=dataDF.Depth_sample*(-1),
                                              colorscale='Viridis',  # one of plotly colorscales
                                              showscale=True,
                                              colorbar=dict(title='Depth (m)',
                                                            tickmode='array',
                                                            ticktext=[
                                                                0, 5, 10, 15, 20, 25, 30],
                                                            tickvals=[0, -5, -10, -15, -20, -25, -30]),
                                              reversescale=False,

                                          ),
                                          showlegend=False,
                                          hovertemplate='<b>Dissolved Oxygen Saturation: %{y}%</b><br>' +
                                          'Date: %{x}<br>' +
                                          #                         'DO_Saturation.: %{y}%<br>' +
                                          'Depth: %{text}m<br><extra></extra>')
    figure_3_15 = go.Figure(
        data=dissolvedOxygenDateTrace, layout=TIMESERIES_LAYOUT)
    figure_3_15.update_layout(
        yaxis=dict(title='Saturation (%)'),
        xaxis=dict(title='Year'))

    return figure_3_15


def map_3_6():
    """
    Dissolved Oxygen infrastructure map
    """

    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.7Oxygen/Map3.6/'
        epaStationsDF = pd.read_csv(
            data_path+'Map3.6_StationTable_EPA_Stations.txt')
        maceHeadStationsDF = pd.read_csv(
            data_path+'Map3.6_StationTable_MaceHead.txt')
        MIStationsDF_origin = pd.read_csv(
            data_path+'Map3.6_StationTable_MI_SurveysStations.txt')
        smartBayStationsDF = pd.read_csv(
            data_path+'Map3.6_StationTable_SmartBayObservatory.txt')
    except:
        return empty_chart()

    epaStationsTrace = go.Scattermapbox(
        name='EPA',
        lon=epaStationsDF.longitude,
        lat=epaStationsDF.latitude,
        text=epaStationsDF.agency,
        marker=dict(color=[STATION_COLORS[k] for k in epaStationsDF['agency'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon}\u00b0<br>' +
        'Lon: %{lat}\u00b0<br>' +
        '<extra></extra>',)

    maceHeadStationsTrace = go.Scattermapbox(
        name='Maze Head',
        lon=maceHeadStationsDF.Longitude,
        lat=maceHeadStationsDF.Latitude,
        text=maceHeadStationsDF.Type,
        marker=dict(color=[STATION_COLORS[k] for k in maceHeadStationsDF['Type'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon}\u00b0<br>' +
        'Lon: %{lat}\u00b0<br>' +
        '<extra></extra>',)

    MIStationsDF = pd.DataFrame()
    MIStationsDF['Station_Nu'] = MIStationsDF_origin.Station.unique()

    for index, row in MIStationsDF.iterrows():
        stationRow = MIStationsDF_origin[MIStationsDF_origin.Station ==
                                         row['Station_Nu']].iloc[0]
        MIStationsDF.at[index, 'Latitude'] = stationRow['Latitude']
        MIStationsDF.at[index, 'Longitude'] = stationRow['Longitude']
        MIStationsDF.at[index, 'Type'] = 'MI_Survey'

    MIStationsTrace = go.Scattermapbox(
        name='MI Survey',
        lon=MIStationsDF.Longitude,
        lat=MIStationsDF.Latitude,
        text=MIStationsDF.Type,
        marker=dict(color=[STATION_COLORS[k] for k in MIStationsDF['Type'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon}\u00b0<br>' +
        'Lon: %{lat}\u00b0<br>' +
        '<extra></extra>')

    smartBayStationsTrace = go.Scattermapbox(
        name='Wave Ride / Smart Bay',
        lon=smartBayStationsDF.Longitude,
        lat=smartBayStationsDF.Latitude,
        text=smartBayStationsDF.Type,
        marker=dict(color=[STATION_COLORS[k] for k in smartBayStationsDF['Type'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon}\u00b0<br>' +
        'Lon: %{lat}\u00b0<br>' +
        '<extra></extra>',)

    map_3_6 = go.Figure(data=[MIStationsTrace,
                              epaStationsTrace,
                              smartBayStationsTrace,
                              maceHeadStationsTrace],
                        layout=MAP_LAYOUT)

    return map_3_6


def figure_4_10_1():
    """
    Landcover 1990 Pie
    """

    #e6e43b = agri
    # 4c52f9 = wetlands
    # 5ea32a = forest
    #c4fd89 = semiVeg
    #db2001 = artiSurface
    # 72caf0 = waterBodies

    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx')
        areaDF = pd.read_excel(xls, header=0,  skiprows=2, nrows=6)
    except:
        return empty_chart()

    # Tidy text by wrapping
    areaDF.loc[
        areaDF['Corine L1 Class'] == 'Semi-Natural & Low Vegetation', 'Corine L1 Class'] = 'Semi-Natural &<br>Low Vegetation'
    area1990Trace = go.Pie(
        labels=areaDF['Corine L1 Class'],
        values=areaDF['CLC90 Area(HA)']/1000,
        textinfo='label+percent',
        textposition='auto',
        marker=dict(colors=['#db2001',
                            '#e6e43b',
                            '#5ea32a',
                            '#c4fd89',
                            '#4c52f9',
                            '#72caf0', ]),
        sort=True,
        texttemplate='<b>%{label}<br>%{percent:.1%}<b>',
        hovertemplate='<b>%{label}</b><br>' +
        '%{value:.0f}kHA<br>' +
        '%{percent:.2%}<extra></extra>',
    )
    figure_4_10_1 = go.Figure(data=[area1990Trace])
    figure_4_10_1.update_layout(
        height=300,
        margin={"b": 0, "r": 0, "l": 0, "t": 0},
        font=CHART_FONT,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False)
    return figure_4_10_1


def figure_4_10_2():
    """
    Landcover 2018 Pie
    """

    #e6e43b = agri
    # 4c52f9 = wetlands
    # 5ea32a = forest
    #c4fd89 = semiVeg
    #db2001 = artiSurface
    # 72caf0 = waterBodies
    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx')
        areaDF = pd.read_excel(xls, header=0,  skiprows=2, nrows=6)
    except:
        return empty_chart()

    # Tidy text by wrapping
    areaDF.loc[
        areaDF['Corine L1 Class'] == 'Semi-Natural & Low Vegetation', 'Corine L1 Class'] = 'Semi-Natural &<br>Low Vegetation'
    area2018Trace = go.Pie(labels=areaDF['Corine L1 Class'],
                           values=areaDF['CLC18 Area(HA)']/1000,
                           textinfo='label+percent',
                           textposition='auto',
                           # insidetextorientation='radial',
                           # textposition= 'inside',
                           marker=dict(colors=['#db2001',
                                               '#e6e43b',
                                               '#5ea32a',
                                               '#c4fd89',
                                               '#4c52f9',
                                               '#72caf0', ]),
                           sort=True,
                           texttemplate='<b>%{label}<br>%{percent:.1%}<b>',
                           hovertemplate='<b>%{label}</b><br>' +
                           '%{value:.0f}kHA<br>' +
                           '%{percent:.2%}<extra></extra>',
                           )
    figure_4_10_2 = go.Figure(data=[area2018Trace])
    figure_4_10_2.update_layout(
        height=300,
        margin={"b": 0, "r": 0, "l": 0, "t": 0},
        font=CHART_FONT,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False)
    return figure_4_10_2


def figure_4_11():
    """
    Landcover time series
    """

    #e6e43b = agri
    # 4c52f9 = wetlands
    # 5ea32a = forest
    #c4fd89 = semiVeg
    #db2001 = artiSurface
    # 72caf0 = waterBodies

    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.6LandCover/Figure4.11/'
        xls = pd.ExcelFile(data_path+'CorineStats_CumulativeChanges.xlsx')
    except:
        return empty_chart()

    cumChangeDF = pd.read_excel(xls, header=0,  skiprows=22, nrows=6)
    cumChangeDF = cumChangeDF.set_index('Corine L1 Class').T
    cumChangeDF.reset_index(level=0, inplace=True)
    cumChangeNameDict = {
        'index': 'Year',
        'Artificial Surfaces': 'ArtificialSurfacesCumChange',
        'Agricultural Areas': 'AgriculturalAreasCumChange',
        'Forest': 'ForestCumChange',
        'Semi-Natural & Low Vegetation': 'SemiNaturalLowVegetationsCumChange',
        'Wetlands': 'WetlandsCumChange',
        'Water Bodies': 'WaterBodiesCumChange',
    }

    cumChangeDF = cumChangeDF.rename(columns=cumChangeNameDict)

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

    data = [artificialSurfacesTrace,
            agriculturalAreasTrace,
            forestTrace,
            semiNaturalLowVegetationsTrace,
            wetlandsTrace,
            waterBodiesTrace]

    figure_4_11 = go.Figure(data=data)
    figure_4_11.update_layout(
        height=450,
        margin={'t': 0, 'b': 0, 'r': 0, 'l': 0, },
        plot_bgcolor='#f7fbfd',
        paper_bgcolor='rgba(0,0,0,0)',
        font=CHART_FONT,
        hovermode='closest',
        legend=dict(
            orientation='h',
            y=-0.15,
            bgcolor='rgba(0,0,0,0)',
        ), )
    figure_4_11.update_yaxes(title_text='<b>Percentage (%)</b>',
                             tickformat=',.0%',)
    figure_4_11.update_xaxes(title_text='<b>Year</b>')

    return figure_4_11


def figure_4_12():
    """
    FAPAR Trend
    """
    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.7FAPAR/Figure4.12/'
        xls = pd.ExcelFile(
            data_path+'FAPAR_CopernicusLandService_10Days_OverIreland_v2.xlsx')
        dataDF = pd.read_excel(xls, 'FAPAR_10_Daily_OverIreland')
    except:
        return empty_chart()

    faparDF = pd.DataFrame()
    faparDF['Date'] = dataDF['Unnamed: 1'].dt.date
    faparDF['Year'] = dataDF['Unnamed: 1'].dt.year
    faparDF['Month'] = dataDF['Unnamed: 1'].dt.month
    faparDF['Day'] = dataDF['Unnamed: 1'].dt.day
    faparDF['Mean'] = dataDF['Mean']
    faparDF['Min'] = dataDF['Min']
    faparDF['Max'] = dataDF['Max']

    for index, row in faparDF.iterrows():
        if row.Month == 1 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 1
        elif row.Month == 1 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 2
        elif row.Month == 1 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 3

        elif row.Month == 2 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 4
        elif row.Month == 2 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 5
        elif row.Month == 2 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 6

        elif row.Month == 3 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 7
        elif row.Month == 3 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 8
        elif row.Month == 3 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 9

        elif row.Month == 4 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 10
        elif row.Month == 4 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 11
        elif row.Month == 4 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 12

        elif row.Month == 5 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 13
        elif row.Month == 5 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 14
        elif row.Month == 5 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 15

        elif row.Month == 6 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 16
        elif row.Month == 6 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 17
        elif row.Month == 6 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 18

        elif row.Month == 7 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 19
        elif row.Month == 7 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 20
        elif row.Month == 7 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 21

        elif row.Month == 8 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 22
        elif row.Month == 8 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 23
        elif row.Month == 8 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 24

        elif row.Month == 9 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 25
        elif row.Month == 9 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 26
        elif row.Month == 9 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 27

        elif row.Month == 10 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 28
        elif row.Month == 10 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 29
        elif row.Month == 10 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 30

        elif row.Month == 11 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 31
        elif row.Month == 11 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 32
        elif row.Month == 11 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 33

        elif row.Month == 12 and row.Day < 12:
            faparDF.at[index, 'xAxis'] = 34
        elif row.Month == 12 and row.Day < 22:
            faparDF.at[index, 'xAxis'] = 35
        elif row.Month == 12 and row.Day < 32:
            faparDF.at[index, 'xAxis'] = 36
    my_text = ['Date: '+'{}'.format(date)+'<br>' +
               'Min: '+'{}'.format(mn)+'<br>' +
               'Max: '+'{}'.format(mx)+'<br>'
               for date, mn, mx, in zip(list(faparDF['Date']),
                                        list(faparDF['Min']),
                                        list(faparDF['Max'])
                                        )]
    colorscale = [
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
    date_list = [datetime.date.today() - dateutil.relativedelta.relativedelta(months=x)
                 for x in range(11, -1, -1)]
    month_list = [datetime.date.strftime(x, '%b') for x in date_list]
    faparTrace = go.Heatmap(
        z=faparDF.Mean,
        x=faparDF.xAxis,
        y=faparDF.Year,
        text=my_text,
        colorscale=colorscale,
        colorbar=dict(title='Mean (%)',
                      tickmode='array',
                      ticktext=['<50', '50-56', '56-65',
                                '65-72', '72-76', '>76'],
                      tickvals=[0.48, 0.52, 0.59, 0.67, 0.735, 0.77]),
        hovertemplate='<b>Mean: %{z:.1%}</b><br>' +
        '%{text}' +
        '<extra></extra>')

    figure_4_12 = go.Figure(data=faparTrace, layout=TIMESERIES_LAYOUT)
    figure_4_12.update_layout(
        # title_text='<b>10-day average FAPAR over Ireland</b>',
        yaxis=dict(
            title='Year',
            nticks=20),
        xaxis=dict(
            title='Month',
            ticktext=month_list,
            showgrid=True, gridwidth=3, gridcolor='black',
            tickvals=[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],))
    figure_4_12.add_shape(
        type='line',
        x0=3.5, y0=1998.6, x1=3.5, y1=2018.4,
        line=dict(color='White', width=3)
    )
    figure_4_12.add_shape(type='line',
                          x0=6.5, y0=1998.6, x1=6.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=9.5, y0=1998.6, x1=9.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=12.5, y0=1998.6, x1=12.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=15.5, y0=1998.6, x1=15.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=18.5, y0=1998.6, x1=18.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=21.5, y0=1998.6, x1=21.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=24.5, y0=1998.6, x1=24.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=27.5, y0=1998.6, x1=27.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=30.5, y0=1998.6, x1=30.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    figure_4_12.add_shape(type='line',
                          x0=33.5, y0=1998.6, x1=33.5, y1=2018.4,
                          line=dict(color='White', width=3)
                          )
    return figure_4_12
