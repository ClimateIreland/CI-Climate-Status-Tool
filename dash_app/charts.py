import pandas as pd
import numpy as np
import datetime
import dateutil
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from settings import *

def stations_map_hovertemplate(df):
    return ['Name: {}<br>'.format(n)+
            'County: {}<br>'.format(cnty)+
            'Type: {}<br>'.format(t)+
            'Station No.: {}<br>'.format(sN)+
            'Open Year: {}<br>'.format(oY)+
            'Close Year: {}<br>'.format(cY)+
            'Height: {:.2f} m<br>'.format(h)+
            # 'Easting: {}<br>'.format(easting)+
            # 'Northing: {}<br>'.format(northing)+
            'Lat: {:.2f} \u00b0<br>'.format(lat)+
            'Lon: {:.2f} \u00b0<br>'.format(lon)+'<extra></extra>'
            for n, t, sN, cnty, oY, cY, h, lat, lon in zip(list(df['name']),
                                                                        list(
                df['Type']),
        list(
                df['Station_Nu']),
        list(
                df['County']),
        list(
                df['Open_Year']),
        list(
                df['Close_Year']),
        list(
                df['Height__m_']),
        # list(
        #         df['Easting']),
        # list(
        #         df['Northing']),
        list(
                df['Latitude']),
        list(
                df['Longitude']),
    )]


def stations_map(df):
    buoyDF = df.loc[(df['Type'] == 'Buoy') | (df['Type'] == 'BuoySubSurf')]
    flowDF = df.loc[(df['Type'] == 'Flow')]
    ghgFluxDF = df.loc[(df['Type'] == 'GHG_FLUX_TOWER')]
    epaDF = df.loc[(df['Type'] == 'EPA')]
    nuigDF = df.loc[(df['Type'] == 'NUIG')]
    synopticDF = df.loc[(df['Type'] == 'Synoptic') | (df['Type'] == 'ClosedS')]
    rainfallDF = df.loc[df['Type'] == 'Rainfall']
    climateDF = df.loc[df['Type'] == 'Climate']
    waveRideDF = df.loc[(df['Type'] == 'WaveRide/SmartBayObsCenter') | (df['Type'] == 'WaveRide')]
    tideGaugeDF = df.loc[(df['Type'] == 'TideGauge')]
    elletDF = df.loc[(df['Type'] == 'ExtendedElletLineBuoy')]
    tidbiTDF = df.loc[df['Type'] == 'TidbiT Sea Temperature Station']
    miDF = df.loc[df['Type'] == 'MI_Survey']
    
    tidbiTTrend = go.Scattermapbox(
        name='tidbiT',
        lon=tidbiTDF.Longitude,
        lat=tidbiTDF.Latitude,
        marker=dict(color=STATION_COLORS['TidbiT'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(tidbiTDF),
    )

    miTrend = go.Scattermapbox(
        name='MI_Survey',
        lon=miDF.Longitude,
        lat=miDF.Latitude,
        marker=dict(color='orange',
                    size=7),
        hovertemplate=stations_map_hovertemplate(miDF),
    )

    ghgFluxTrend = go.Scattermapbox(
        name='GHG Flux Tower',
        lon=ghgFluxDF.Longitude,
        lat=ghgFluxDF.Latitude,
        marker=dict(color=STATION_COLORS['GHG_FLUX_TOWER'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(ghgFluxDF),
    )


    nuigTrend = go.Scattermapbox(
        name='NUIG',
        lon=nuigDF.Longitude,
        lat=nuigDF.Latitude,
        marker=dict(color=STATION_COLORS['NUIG'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(nuigDF),
    )

    tideGaugeTrend = go.Scattermapbox(
        name='Tide Gauge',
        lon=tideGaugeDF.Longitude,
        lat=tideGaugeDF.Latitude,
        marker=dict(color=STATION_COLORS['TideGauge'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(tideGaugeDF),
    )

    elletTrend = go.Scattermapbox(
        name='Extended Ellet Line Buoy',
        lon=elletDF.Longitude,
        lat=elletDF.Latitude,
        marker=dict(color=STATION_COLORS['ExtendedElletLineBuoy'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(elletDF),
    )

    epaTrend = go.Scattermapbox(
        name='EPA',
        lon=epaDF.Longitude,
        lat=epaDF.Latitude,
        marker=dict(color=STATION_COLORS['EPA'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(epaDF),
    )

    waveRideTrend = go.Scattermapbox(
        name='WaveRide/SmartBayObsCent',
        lon=waveRideDF.Longitude,
        lat=waveRideDF.Latitude,
        marker=dict(color=STATION_COLORS['WaveRide/SmartBayObsCenter'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(waveRideDF),
    )

    buoyTrend = go.Scattermapbox(
        name='Buoy',
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
        name='Climatological',
        lon=climateDF.Longitude,
        lat=climateDF.Latitude,
        marker=dict(color=STATION_COLORS['Climate'],
                    size=7),
        hovertemplate=stations_map_hovertemplate(climateDF),
    )
    stations_map = go.Figure(
        data=[synopticTrend, 
              climateTrend,
              buoyTrend, 
              epaTrend,
              nuigTrend,
              ghgFluxTrend, 
              rainfallTrend, 
              tidbiTTrend, 
              elletTrend, 
              tideGaugeTrend,
              waveRideTrend,
              miTrend],
        layout=MAP_LAYOUT)
    stations_map.update_layout(
        mapbox=dict(bearing=0,
                center=dict(
                    lat=54,
                    lon=349
                ),
                pitch=0,
                zoom=4.2)
    )
    
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
                                'Anomaly: %{y:.2f} \u00b0C<extra></extra>'
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
                             'Tmean: %{y:.2f} \u00b0C<br>' +
                             'Anomaly: %{text:.2f} \u00b0C<extra></extra>'
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
        'Total: %{text:.2f} mm<br>' +
        'Anomaly: %{y:.2f} mm<extra></extra>'
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
        'Total: %{text:.2f} mm<br>' +
        'Anomaly: %{y:.2f} mm<extra></extra>'
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

def figure_2_18():
    """
    Monthly CO2 Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.10CarbonDioxide/Figure2.18/'
        xls = pd.ExcelFile(
            data_path+'MonthlyMeanConcentrationOfCarbonDioxide_MaunaLoa_MaceHead2018.xlsx')
        dataDF = pd.read_excel(xls, 'co2_mm_mlo')
    except:
        return empty_chart()

    dataDF.rename(columns = {
        "Unnamed: 0":"Date"
    }, inplace = True)
    dataDF = dataDF.iloc[:, 0:5]

    MaunaLoa = go.Scatter(x=dataDF["Date"],
                     y=dataDF["Mauna Loa (Hawaii)"],
                     name='Mauna Loa (Hawaii)',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Mauna Loa (Hawaii)</b><br>' +
                            'CO\u2082: %{y:.2f} ppm<extra></extra>' 
                            )

    MaceHead = go.Scatter(x=dataDF["Date"],
                     y=dataDF["Mace Head"],
                     name='Mace Head',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_SECONDARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Mace Head</b><br>' +
                            'CO\u2082: %{y:.2f} ppm<extra></extra>' 
                            )

    figure_2_18 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_2_18.add_trace(MaunaLoa,
                secondary_y=False,)

    figure_2_18.add_trace(MaceHead,
                secondary_y=False,)

    figure_2_18.update_layout(TIMESERIES_LAYOUT)

    figure_2_18.update_yaxes(title_text='CO\u2082 Concentration (ppm)',
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_2_18.update_xaxes(title_text='Year',
                            range=['1955-01-01', '2020-01-01'],
                            tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )

    return figure_2_18

def map_2_10():
    """
    CO2 infrastructure map
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.10CarbonDioxide/Map2.10/'
        df = pd.read_csv(data_path+'Map2.10_StationTable.txt')
    except:
        return empty_chart()
    map_2_10=stations_map(df)
    return map_2_10

def figure_2_20():
    """
    CH4 Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.11Methane/Figure2.20/'
        xls = pd.ExcelFile(
            data_path+'MonthlyMeanMethaneConcentration_MaceHead_2018.xlsx')
        dataDF = pd.read_excel(xls, 'MHD-gcmd')
    except:
        return empty_chart()

    dataDF.rename(columns = {
        "Unnamed: 0":"Date",
        "Unnamed: 2":"MovingAverage"
        }, inplace = True)
    dataDF = dataDF.iloc[:, 0:3]

    MonthlyMean = go.Scatter(x=dataDF["Date"],
                     y=dataDF["CH4"],
                     name='Monthly Mean',
                     mode='markers',
                     marker=dict(color=TIMESERIES_COLOR_SECONDARY,
                                size=5,
                                opacity=0.5),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Mean</b><br>' +
                            'CH\u2084: %{y:.2f} ppb<extra></extra>' 
                            )

    MovingAverage = go.Scatter(x=dataDF["Date"],
                     y=dataDF["MovingAverage"],
                     name='12 Month Moving Average',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Moving Avaerge</b><br>' +
                            'CH\u2084: %{y:.2f}ppb<extra></extra>' 
                            )

    figure_2_20 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_2_20.add_trace(MonthlyMean,
                secondary_y=False,)

    figure_2_20.add_trace(MovingAverage,
                secondary_y=False,)

    figure_2_20.update_layout(TIMESERIES_LAYOUT)

    figure_2_20.update_yaxes(title_text='CH\u2084 Concentration (ppb)',
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_2_20.update_xaxes(title_text='Year',
                            range=['1985-01-01', '2020-12-31'],
                            tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )

    return figure_2_20

def map_2_11():
    """
    CH4 infrastructure map
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.11Methane/Map2.11/'
        df = pd.read_csv(data_path+'Map2.11_StationTable.txt')
    except:
        return empty_chart()
    map_2_11=stations_map(df)
    return map_2_11

def figure_2_22():
    """
    Monthly N2O Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.12OtherGHGs/Figure2.22/'
        xls = pd.ExcelFile(
            data_path+'Monthly_Mean_N20.xlsx')
        dataDF = pd.read_excel(xls, 'Sheet1', header = None, skiprows=[0,1,2])
    except:
        return empty_chart()

    dataDF.rename(columns = {
        0:"Date",
        1:"N2O"
        }, inplace = True)
    dataDF = dataDF.iloc[:, 0:2]

    MonthlyMean = go.Scatter(x=dataDF["Date"],
                     y=dataDF["N2O"],
                     name='Monthly Mean',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Mean</b><br>' +
                            'N\u2082O: %{y:.2f}ppb<extra></extra>' 
                            )

    figure_2_22 = make_subplots(specs=[[{'secondary_y': False}]])
    figure_2_22.add_trace(MonthlyMean,
            secondary_y=False,)
    figure_2_22.update_layout(TIMESERIES_LAYOUT)
    figure_2_22.update_yaxes(title_text='N\u2082O Concentration (ppb)',
                         showgrid=False,
                         fixedrange=True,
                         showspikes=True,
                        )
    figure_2_22.update_xaxes(title_text='Year',
                         range=['1978-01-01', '2020-06-30'],
                         tickformat="%Y",
                         showspikes=True,  
                         spikethickness=2
                        )

    return figure_2_22

def figure_2_23():
    """
    Monthly CFC-12 Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.12OtherGHGs/Figure2.23/'
        xls = pd.ExcelFile(
            data_path+'Monthly_Mean_CFC12.xlsx')
        dataDF = pd.read_excel(xls, 'Sheet1', header = None, skiprows=[0,1,2])
    except:
        return empty_chart()

    dataDF.rename(columns = {
        0:"Date",
        1:"CFC-12"
        }, inplace = True)
    dataDF = dataDF.iloc[:, 0:2]

    MonthlyMean = go.Scatter(x=dataDF["Date"],
                     y=dataDF["CFC-12"],
                     name='Monthly Mean',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Mean</b><br>' +
                            'CFC-12: %{y:.2f}ppt<extra></extra>' 
                            )

    figure_2_23 = make_subplots(specs=[[{'secondary_y': False}]])
    figure_2_23.add_trace(MonthlyMean,
                secondary_y=False,)
    figure_2_23.update_layout(TIMESERIES_LAYOUT)
    figure_2_23.update_yaxes(title_text='CFC-12 Concentration (ppt)',
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_2_23.update_xaxes(title_text='Year',
                            range=['1978-01-01', '2020-06-30'],
                            tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_2_23

def figure_2_24():
    """
    Monthly HFC-134a Trend
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.12OtherGHGs/Figure2.24/'
        xls = pd.ExcelFile(
            data_path+'Monthly_MeanHFC134a.xlsx')
        dataDF = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()

    dataDF.rename(columns = {
        "MONTH":"Date"
        }, inplace = True)
    dataDF = dataDF.iloc[:, 0:2]

    MonthlyMean = go.Scatter(x=dataDF["Date"],
                     y=dataDF["HFC-134a"],
                     name='Monthly Mean',
                     line_shape='spline',
                     line=dict(
                            # color="#fc0d1b", color used in report
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Mean</b><br>' +
                            'HFC-134a: %{y:.2f}ppt<extra></extra>' 
                            )

    figure_2_24 = make_subplots(specs=[[{'secondary_y': False}]])
    figure_2_24.add_trace(MonthlyMean,
                secondary_y=False,)


    figure_2_24.update_layout(TIMESERIES_LAYOUT)

    figure_2_24.update_yaxes(title_text='HFC-134a Concentration (ppt)',
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_2_24.update_xaxes(title_text='Year',
                            range=['1994-01-01', '2020-06-30'],
                            tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_2_24

def map_2_12():
    """
    Other GHGs infrastructure map
    """
    try:
        data_path = DATA_PATH+'Atmospheric_Domain/2.12OtherGHGs/Map2.12/'
        df = pd.read_csv(data_path+'Map2.12_StationTable.txt')
    except:
        return empty_chart()
    map_2_12=stations_map(df)
    return map_2_12

def figure_3_1():
    """
    Sea Surface Temperature Totals and Anomalies Trend
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.1OceanSurfaceSubsurfaceTemperature/Figure3.1/'
        xls = pd.ExcelFile(
            data_path+'MeanAnnualSeaSurfaceTemperature_Anomalies_MalinHead.xlsx')
        df = pd.read_excel(xls, 'MALIN_Timeseries')
    except:
        return empty_chart()

    movingAverageTotals = df.temperature.rolling(window=5, center=True).mean() 
    df["5 Year Moving Average - Mean"]=movingAverageTotals


    annualTrace = go.Bar(x=df["year"],
                        y=df["Calculated Anomalies"],
                        text=df["temperature"],
                        name='Annual',
                        marker=dict(
                                # color="#214a7b", color used in report
                                color=TIMESERIES_COLOR_SECONDARY,
                                opacity=0.5
                                ),
                        hovertemplate='%{x}<br>' +
                                '<b>Annual</b><br>' +
                                'Total: %{text:.2f} \u00b0C<br>' +
                                'Anomaly: %{y:.2f} \u00b0C<extra></extra>'
                                )
    movingAverage = go.Scatter(x=df["year"],
                        y=df["5 year moving average"],
                        text=df["5 Year Moving Average - Mean"],
                        name='5yr Moving Average',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(
                                # color="#fc0d1b", color used in report
                                color=TIMESERIES_COLOR_PRIMARY,
                                width=2),
                        hovertemplate='%{x}<br>' +
                                '<b>5yr Moving Average</b><br>' +
                                'Total: %{text:.2f} \u00b0C<br>' +
                                'Anomaly: %{y:.2f} \u00b0C<extra></extra>'
                                )
    normal = go.Scatter(x=df["year"],
                        y=df["Unnamed: 5"],
                        name='1981-2010 Normal',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(color="#fdbf2d", #color used in report
                                width=1),
                        hoverinfo='skip',
                                )

    figure_3_1 = make_subplots(specs=[[{'secondary_y': True}]])
    figure_3_1.add_trace(annualTrace,
                secondary_y=False,)
    figure_3_1.add_trace(movingAverage,
                secondary_y=False,)
    figure_3_1.add_trace(normal,
                secondary_y=True,)
    figure_3_1.update_layout(TIMESERIES_LAYOUT)
    figure_3_1.update_yaxes(title_text='Difference (\u00b0C) from 1981-2010 Normal',
                            secondary_y=False,
                            range=[-1, 1],
                            showgrid=False,
                            dtick=0.25,  # dtick sets the distance between ticks
                            tick0=0,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            showspikes=True,
                            # zeroline=True,  # add a zero line
                            # zerolinecolor=TIMESERIES_COLOR_SECONDARY
                            )
    figure_3_1.update_yaxes(title_text='Sea Surface Temperature (\u00b0C)',
                        secondary_y=True,
                        range=[9.5, 11.6],
                        showgrid=False,
                        dtick=0.5,  # dtick sets the distance between ticks
                        tick0=10.6,  # tick0 sets a point to map the other ticks
                        fixedrange=True,
                        )
    figure_3_1.update_xaxes(
        title='Year',
        fixedrange=True,
        tickformat='000',  
        showspikes=True,  
        spikethickness=2, 
        ) 
    
    return figure_3_1

def figure_3_3():
    """
    Sea Subsurface Temperature Totals and Anomalies Trend
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.1OceanSurfaceSubsurfaceTemperature/Figure3.3/'
        xls = pd.ExcelFile(
            data_path+'SubSurfaceTemperature_Anomalies_Rockall.xlsx')
        df = xls.parse('Depth_Rockall', skiprows=20, index_col=None, na_values=['NA'])
    except:
        return empty_chart()
    annualTrace = go.Bar(x=df["Decimal Year"],
                     y=df["Temperature Anomaly °C"],
                     text=df["Temperature °C"],
                     name='Annual',
                     marker=dict(
                            # color="#214a7b", color used in report
                            color=TIMESERIES_COLOR_SECONDARY,
                            opacity=0.5
                            ),
                     hovertemplate='%{x}<br>' +
                            '<b>Annual</b><br>' +
                            'Total: %{text:.2f} \u00b0C<br>' +
                            'Anomaly: %{y:.2f} \u00b0C<extra></extra>'
                            )
    movingAverage = go.Scatter(x=df["Decimal Year"],
                        y=df["5 year moving average"],
                        #  text=df["5 Year Moving Average - Mean"],
                        name='5yr Moving Average',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(
                                # color="#fc0d1b", color used in report
                                color=TIMESERIES_COLOR_PRIMARY,
                                width=2),
                        hovertemplate='%{x}<br>' +
                                '<b>5yr Moving Average</b><br>' +
                                # 'Total: %{text:.2f} \u00b0C<br>' +
                                'Anomaly: %{y:.2f} \u00b0C<extra></extra>'
                                )
    normal = go.Scatter(x=df["Decimal Year"],
                        y=df["1981-2010 (Normalized)"],
                        name='1981-2010 Normal',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(color="#fdbf2d", #color used in report
                                width=1),
                        hoverinfo='skip',
                                )

    figure_3_3 = make_subplots(specs=[[{'secondary_y': True}]])
    figure_3_3.add_trace(annualTrace,
                secondary_y=False,)
    figure_3_3.add_trace(movingAverage,
                secondary_y=False,)
    figure_3_3.add_trace(normal,
                secondary_y=True,)

    figure_3_3.update_layout(TIMESERIES_LAYOUT)
    figure_3_3.update_yaxes(title_text='Difference (\u00b0C) from 1981-2010 Normal',
                            secondary_y=False,
                            range=[-0.25, 0.45],
                            showgrid=False,
                            dtick=0.05,  # dtick sets the distance between ticks
                            tick0=0,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            showspikes=True,
                            # zeroline=True,  # add a zero line
                            # zerolinecolor=TIMESERIES_COLOR_SECONDARY
                            )
    figure_3_3.update_yaxes(title_text='Sea Sub-surface Temperature (\u00b0C)',
                            secondary_y=True,
                            range=[3.93, 4.59],
                            showgrid=False,
                            dtick=0.1,  # dtick sets the distance between ticks
                            tick0=4.17,  # tick0 sets a point to map the other ticks
                            fixedrange=True,
                            )

    figure_3_3.update_xaxes(
        title='Year',
        fixedrange=True,
        tickformat='000',  
        showspikes=True,  
        spikethickness=2, 
    ) 

    return figure_3_3


def map_3_1():
    """
    Ocean Surface and Subsurface Temperature infrastructure map
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.1OceanSurfaceSubsurfaceTemperature/Map3.1/'
        stationsDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_MI.txt')

        rockallDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_RockallTroughSection.txt')
        tidbiDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_TidbiT.txt')
    except:
        return empty_chart()
    tidbiDFNew=pd.DataFrame(columns=rockallDF.columns)
    tidbiDFNew['name']=tidbiDF["localId"]
    tidbiDFNew['Latitude']=tidbiDF["latitude"]
    tidbiDFNew['Longitude']=tidbiDF["longitude"]
    tidbiDFNew['Open_Year']=pd.to_datetime(tidbiDF["beginLifes"]).dt.year
    tidbiDFNew['Close_Year']=pd.to_datetime(tidbiDF["endLifespa"]).dt.year
    tidbiDFNew['Type']=tidbiDF["datasetNam"]
    combinedDF = pd.concat([stationsDF,rockallDF, tidbiDFNew])
    map_3_1a=stations_map(combinedDF)
    return map_3_1a

def map_3_1a():
    """
    Sea Surface Temperature infrastructure map
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.1OceanSurfaceSubsurfaceTemperature/Map3.1/'
        stationsDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_MI.txt')

        rockallDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_RockallTroughSection.txt')
        tidbiDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_TidbiT.txt')
    except:
        return empty_chart()
    tidbiDFNew=pd.DataFrame(columns=rockallDF.columns)
    tidbiDFNew['name']=tidbiDF["localId"]
    tidbiDFNew['Latitude']=tidbiDF["latitude"]
    tidbiDFNew['Longitude']=tidbiDF["longitude"]
    tidbiDFNew['Open_Year']=pd.to_datetime(tidbiDF["beginLifes"]).dt.year
    tidbiDFNew['Close_Year']=pd.to_datetime(tidbiDF["endLifespa"]).dt.year
    tidbiDFNew['Type']=tidbiDF["datasetNam"]
    combinedDF = pd.concat([stationsDF, tidbiDFNew])
    map_3_1=stations_map(combinedDF)
    return map_3_1

def figure_3_7_1():
    """
    Sea Level Malin Head
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Figure3.7/'
        xls = pd.ExcelFile(
            data_path+'malinHead.xlsx')
        df = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()
    monthlyTrace = go.Scatter(x=df["Date"],
                     y=df["MonthlyAverage_m"],
                    #  text=dataDF["11 Year Moving Average Totals"],
                     name='Malin Head',
                     connectgaps=False,
                     mode='lines',  # 'line' is default
                     line_shape='spline',
                     line=dict(
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Average: %{y:.2f} m<extra></extra></b>'
                            )

    figure_3_7_1 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_3_7_1.add_trace(monthlyTrace,
                secondary_y=False,)

    figure_3_7_1.update_layout(TIMESERIES_LAYOUT)

    figure_3_7_1.update_yaxes(title_text='Sea Level (metres) relative to OD Malin',
                            range=[-0.45, 0.45],
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_3_7_1.update_xaxes(title_text='Year',
                            range=['2004-01-01', '2020-06-30'],
    #                          tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_3_7_1

def figure_3_7_2():
    """
    Sea Level Ballyglass
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Figure3.7/'
        xls = pd.ExcelFile(
            data_path+'ballyglass.xlsx')
        df = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()
    monthlyTrace = go.Scatter(x=df["Date"],
                     y=df["MonthlyAverage_m"],
                    #  text=dataDF["11 Year Moving Average Totals"],
                     name='Ballyglass',
                     connectgaps=False,
                     mode='lines',  # 'line' is default
                     line_shape='spline',
                     line=dict(
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Average: %{y:.2f} m<extra></extra></b>'
                            )

    figure_3_7_2 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_3_7_2.add_trace(monthlyTrace,
                secondary_y=False,)

    figure_3_7_2.update_layout(TIMESERIES_LAYOUT)

    figure_3_7_2.update_yaxes(title_text='Sea Level (metres) relative to OD Malin',
                            range=[-0.45, 0.45],
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_3_7_2.update_xaxes(title_text='Year',
                            range=['2004-01-01', '2020-06-30'],
    #                          tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_3_7_2

def figure_3_7_3():
    """
    Sea Level Castletownbare
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Figure3.7/'
        xls = pd.ExcelFile(
            data_path+'castletownbare.xlsx')
        df = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()
    monthlyTrace = go.Scatter(x=df["Date"],
                     y=df["MonthlyAverage_m"],
                    #  text=dataDF["11 Year Moving Average Totals"],
                     name='Castletownbare',
                     connectgaps=False,
                     mode='lines',  # 'line' is default
                     line_shape='spline',
                     line=dict(
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Average: %{y:.2f} m<extra></extra></b>'
                            )

    figure_3_7_3 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_3_7_3.add_trace(monthlyTrace,
                secondary_y=False,)

    figure_3_7_3.update_layout(TIMESERIES_LAYOUT)

    figure_3_7_3.update_yaxes(title_text='Sea Level (metres) relative to OD Malin',
                            range=[-0.45, 0.45],
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_3_7_3.update_xaxes(title_text='Year',
                            range=['2004-01-01', '2020-06-30'],
    #                          tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_3_7_3

def figure_3_7_4():
    """
    Sea Level Howth Harbour
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Figure3.7/'
        xls = pd.ExcelFile(
            data_path+'howthHarbour.xlsx')
        df = pd.read_excel(xls, 'Sheet1')
    except:
        return empty_chart()
    monthlyTrace = go.Scatter(x=df["Date"],
                     y=df["MonthlyAverage_m"],
                    #  text=dataDF["11 Year Moving Average Totals"],
                     name='Howth Harbour',
                     connectgaps=False,
                     mode='lines',  # 'line' is default
                     line_shape='spline',
                     line=dict(
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                      hovertemplate='%{x}<br>' +
                            '<b>Monthly Average: %{y:.2f} m<extra></extra></b>'
                            )

    figure_3_7_4 = make_subplots(specs=[[{'secondary_y': False}]])

    figure_3_7_4.add_trace(monthlyTrace,
                secondary_y=False,)

    figure_3_7_4.update_layout(TIMESERIES_LAYOUT)

    figure_3_7_4.update_yaxes(title_text='Sea Level (metres) relative to OD Malin',
                            range=[-0.45, 0.45],
                            showgrid=False,
                            fixedrange=True,
                            showspikes=True,
                            )
    figure_3_7_4.update_xaxes(title_text='Year',
                            range=['2004-01-01', '2020-06-30'],
    #                          tickformat="%Y",
                            showspikes=True,  
                            spikethickness=2
                            )
    return figure_3_7_4

def map_3_1b():
    """
    Sea Subsurface Temperature infrastructure map
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.1OceanSurfaceSubsurfaceTemperature/Map3.1/'
        stationsDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_MI.txt')
        stationsDF_subsurface = stationsDF[stationsDF['name'].isin(['M6_Buoy', 'SmartBay Wave Buoy'])]

        rockallDF = pd.read_csv(
                    data_path+'Map3.1_StationTable_RockallTroughSection.txt')
        # tidbiDF = pd.read_csv(
        #             data_path+'Map3.1_StationTable_TidbiT.txt')
    except:
        return empty_chart()

    combinedDF = pd.concat([stationsDF_subsurface,rockallDF])
    map_3_1b=stations_map(combinedDF)
    return map_3_1b

def figure_3_8():
    """
    Sea Level Dublin Port 
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Figure3.8/'
        xls = pd.ExcelFile(
            data_path+'dub_all_1938_to_2016_v2.xlsx')
        df = pd.read_excel(xls, 'dub_all_1938_to_2016')
        df.rename(columns = {
            "Unnamed: 3":"Date",
            "Unnamed: 10":"AnnualDate",
            "Unnamed: 11":"AnnualAverage"
            }, inplace = True)
    except:
        return empty_chart()
    monthlyTrace = go.Scatter(x=df["Date"],
                     y=df["Msl_OD_Malin"],
                     name='Monthly Average',
                    mode='markers',
                    marker=dict(color=TIMESERIES_COLOR_SECONDARY,
                                size=5,
                                opacity=0.5),
                    hovertemplate='%{x}<br>' +
                            '<b>Monthly Average</b><br>' +
                            'Mean Sea Level: %{y:.2f} m<extra></extra>'
                            )
    annualTrace = go.Scatter(x=df["AnnualDate"],
                        y=df["AnnualAverage"],
                        name='Annual Average',
                        mode='lines',  # 'line' is default
                        line_shape='spline',
                        line=dict(
                                color=TIMESERIES_COLOR_PRIMARY,
                                width=2),
                        hovertemplate='%{x}<br>' +
                                '<b>Annual Average</b><br>' +
                                'Mean Sea Level: %{y:.2f} m<extra></extra>'
                                )
    figure_3_8=go.Figure(data=[monthlyTrace, annualTrace], layout=TIMESERIES_LAYOUT)
    figure_3_8.update_layout(
        yaxis=dict(title='Sea Level (m) relative to OD Malin'),
        xaxis=dict(title='Date'),
        hovermode='closest')
    return figure_3_8

def map_3_4():
    """
    Sea Level infrastructure map
    """
    try:
        data_path = DATA_PATH+'Oceanic_Domain/3.4SeaLevel/Map3.4/'
        tidalGaugeDF = pd.read_csv(
                data_path+'Map3.4_StationTable_IrishNationalTideGaugeNetwork.txt')
    except:
        return empty_chart()
    stationColumns=['FID', 'County', 'Station_Nu', 'name', 'Height__m_', 'Easting',
       'Northing', 'Latitude', 'Longitude', 'Open_Year', 'Close_Year', 'Type']
    tidalGaugeDFNew=pd.DataFrame(columns=stationColumns)
    tidalGaugeDFNew['name']=tidalGaugeDF["Station_Na"]
    tidalGaugeDFNew['Latitude']=tidalGaugeDF["Latitude"]
    tidalGaugeDFNew['Longitude']=tidalGaugeDF["Longitude"]
    tidalGaugeDFNew['Easting']=tidalGaugeDF["Easting"]
    tidalGaugeDFNew['Northing']=tidalGaugeDF["Northing"]
    tidalGaugeDFNew['Station_Nu']=tidalGaugeDF["Station_No"]
    tidalGaugeDFNew['Body_Respo']=tidalGaugeDF["Body_Respo"]
    tidalGaugeDFNew['Type']="TideGauge"
    df=tidalGaugeDFNew
    miDF = df.loc[(df['Body_Respo'] == 'MI')]
    opwDF = df.loc[(df['Body_Respo'] == 'OPW')]
    epaDF = df.loc[(df['Body_Respo'] == 'EPA')]
    pcDF = df.loc[df['Body_Respo'].isin(['POC', 'SFPC','LHC','BHC','DLPC'])]
    laDF = df.loc[df['Body_Respo'].isin(['Cork City Council', 'Dublin City Council'])]
    miTrend = go.Scattermapbox(
        name='Marine Institute',
        lon=miDF.Longitude,
        lat=miDF.Latitude,
        marker=dict(color='blue',
                    size=7),
        hovertemplate='Maintainer: '+ miDF.Body_Respo + '<br>'+
                     stations_map_hovertemplate(miDF),
    )
    opwTrend = go.Scattermapbox(
            name='OPW',
            lon=opwDF.Longitude,
            lat=opwDF.Latitude,
            marker=dict(color='yellow',
                        size=7),
            hovertemplate='Maintainer: '+ opwDF.Body_Respo + '<br>'+
                        stations_map_hovertemplate(opwDF),
        )

    pcTrend = go.Scattermapbox(
            name='Port Company',
            lon=pcDF.Longitude,
            lat=pcDF.Latitude,
            marker=dict(color='brown',
                        size=7),
            hovertemplate='Maintainer: '+ pcDF.Body_Respo + '<br>'+
                        stations_map_hovertemplate(pcDF),
        )
    laTrend = go.Scattermapbox(
            name='Local Authority',
            lon=laDF.Longitude,
            lat=laDF.Latitude,
            marker=dict(color='orange',
                        size=7),
            hovertemplate='Maintainer: '+ laDF.Body_Respo + '<br>'+
                        stations_map_hovertemplate(laDF))
    map_3_4 = go.Figure(
            data=[miTrend,
                opwTrend,
                pcTrend,
                laTrend
                ],
            layout=MAP_LAYOUT)
    map_3_4.update_layout(
            mapbox=dict(bearing=0,
                    center=dict(
                        lat=54,
                        lon=349
                    ),
                    pitch=0,
                    zoom=4.2))
    return map_3_4

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
                                          hovertemplate='%{x}<br>' +
                                          '<b>Dissolved Oxygen</b><br>' +
                                          'Saturation: %{y} %<br>' +
                                          'Depth: %{text} m<br><extra></extra>')
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
        epaStationsDF_origin = pd.read_csv(
            data_path+'Map3.6_StationTable_EPA_Stations.txt')
        maceHeadStationsDF = pd.read_csv(
            data_path+'Map3.6_StationTable_MaceHead.txt')
        miStationsDF_origin = pd.read_csv(
            data_path+'Map3.6_StationTable_MI_SurveysStations.txt')
        smartBayStationsDF = pd.read_csv(
            data_path+'Map3.6_StationTable_SmartBayObservatory.txt')
    except:
        return empty_chart()
    columns=['FID', 'County', 'Station_Nu', 'name', 'Height__m_', 'Easting',
       'Northing', 'Latitude', 'Longitude', 'Open_Year', 'Close_Year', 'Type']
    epaStationsDF=pd.DataFrame(columns=columns)
    epaStationsDF['Station_Nu']=epaStationsDF_origin['Station_Co']
    epaStationsDF['Latitude']=epaStationsDF_origin['latitude']
    epaStationsDF['Longitude']=epaStationsDF_origin['longitude']
    epaStationsDF['Type']='EPA'
    miStationsDF=pd.DataFrame(columns=columns)

    miStationsDF['Station_Nu']=miStationsDF_origin.Station.unique()

    for index, row in miStationsDF.iterrows():
    #     print(row['Latitude'])
        stationRow=miStationsDF_origin[miStationsDF_origin.Station == row['Station_Nu']].iloc[0]
        miStationsDF.at[index,'Latitude']=stationRow['Latitude']
        miStationsDF.at[index,'Longitude']=stationRow['Longitude']
        miStationsDF.at[index,'Type']='MI_Survey'

    combinedDF = pd.concat([epaStationsDF,smartBayStationsDF,maceHeadStationsDF, miStationsDF])
    map_3_6=stations_map(combinedDF)

    return map_3_6

def map_3_6_old():
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
        'Lat: %{lon} \u00b0<br>' +
        'Lon: %{lat} \u00b0<br>' +
        '<extra></extra>',)

    maceHeadStationsTrace = go.Scattermapbox(
        name='Mace Head',
        lon=maceHeadStationsDF.Longitude,
        lat=maceHeadStationsDF.Latitude,
        text=maceHeadStationsDF.Type,
        marker=dict(color=[STATION_COLORS[k] for k in maceHeadStationsDF['Type'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon} \u00b0<br>' +
        'Lon: %{lat} \u00b0<br>' +
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
        'Lat: %{lon} \u00b0<br>' +
        'Lon: %{lat} \u00b0<br>' +
        '<extra></extra>')

    smartBayStationsTrace = go.Scattermapbox(
        name='Wave Ride / Smart Bay',
        lon=smartBayStationsDF.Longitude,
        lat=smartBayStationsDF.Latitude,
        text=smartBayStationsDF.Type,
        marker=dict(color=[STATION_COLORS[k] for k in smartBayStationsDF['Type'].values],
                    size=7),
        hovertemplate='Type: %{text}<br>' +
        'Lat: %{lon} \u00b0<br>' +
        'Lon: %{lat} \u00b0<br>' +
        '<extra></extra>',)

    map_3_6 = go.Figure(data=[MIStationsTrace,
                              epaStationsTrace,
                              smartBayStationsTrace,
                              maceHeadStationsTrace],
                        layout=MAP_LAYOUT)

    return map_3_6

def map_3_6_new():
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
    
    map_3_6 = 6
    return map_3_6

def map_4_1():
    """
    River Discharge infrastructure map
    """
    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.1RiverDischarge/Map4.1/'
        df = pd.read_csv(data_path+'Map4.1_StationTable_RiverDischargeStations.txt', delimiter = ",")
        dfString=df.astype(str)
        dfString['Type']='Flow'
    except:
        return empty_chart()

    flowTrend = go.Scattermapbox(
        name='Flow',
        lon=dfString.Longitude,
        lat=dfString.Latitude,
        marker=dict(color=STATION_COLORS['Flow'],
                    size=7),
        hovertemplate='Station: ' + dfString.Station_Na +
                '<br>Station No.: ' + dfString.STATION_NU +
                '<br>River: '+ dfString.River_Name +
                '<br>Catchment: '+ dfString.Catchment +
                '<br>Lat: %{lat:.2f}'+
                '<br>Lon: %{lon:.2f}<extra></extra>',)

    map_4_1=go.Figure(
        data=[flowTrend],
        layout=MAP_LAYOUT)
    map_4_1.update_layout(
        mapbox=dict(bearing=0,
                center=dict(
                    lat=54,
                    lon=349
                ),
                pitch=0,
                zoom=4.2)
    )
    return map_4_1

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
        hovertemplate= '1990<br>' +
        '<b>%{label}</b><br>' +
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
                           hovertemplate= '2018<br>' +
                           '<b>%{label}</b><br>' +
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
                                         hovertemplate='%{x}<br>' +
                                         '<b>Artificial Surfacese</b><br>' +
                                         'Cumalitive Change.: %{y:.2%}<extra></extra>')

    agriculturalAreasTrace = go.Scatter(x=cumChangeDF.Year,
                                        y=cumChangeDF.AgriculturalAreasCumChange,
                                        name='Agricultural Areas',
                                        mode='lines+markers',
                                        marker=dict(color='#e6e43b',
                                                    size=4,
                                                    line=dict(color='#e6e43b',
                                                              width=0)),
                                        hovertemplate='%{x}<br>' +
                                        '<b>Agricultural Areas</b><br>' +
                                        'Cumalitive Change.: %{y:.2%}<extra></extra>')

    forestTrace = go.Scatter(x=cumChangeDF.Year,
                             y=cumChangeDF.ForestCumChange,
                             name='Forest',
                             mode='lines+markers',
                             marker=dict(color='#5ea32a',
                                         size=4,
                                         line=dict(color='#5ea32a',
                                                   width=0)),
                             hovertemplate='%{x}<br>' +
                             '<b>Forest</b><br>' +
                             'Cumalitive Change.: %{y:.2%}<extra></extra>')

    semiNaturalLowVegetationsTrace = go.Scatter(x=cumChangeDF.Year,
                                                y=cumChangeDF.SemiNaturalLowVegetationsCumChange,
                                                name='Semi-Natural & Low Vegetations',
                                                mode='lines+markers',
                                                marker=dict(color='#c4fd89',
                                                            size=4,
                                                            line=dict(color='#c4fd89',
                                                                      width=0)),
                                                hovertemplate='%{x}<br>' +
                                                '<b>Semi-Natural & Low Vegetations</b><br>' +
                                                'Cumalitive Change.: %{y:.2%}<extra></extra>')

    wetlandsTrace = go.Scatter(x=cumChangeDF.Year,
                               y=cumChangeDF.WetlandsCumChange,
                               name='Wetlands',
                               mode='lines+markers',
                               marker=dict(color='#4c52f9',
                                           size=4,
                                           line=dict(color='#4c52f9',
                                                     width=0)),
                               hovertemplate='%{x}<br>' +
                               '<b>Wetlands</b><br>' +
                               'Cumalitive Change.: %{y:.2%}<extra></extra>')

    waterBodiesTrace = go.Scatter(x=cumChangeDF.Year,
                                  y=cumChangeDF.WaterBodiesCumChange,
                                  name='Water Bodies',
                                  mode='lines+markers',
                                  marker=dict(color='#72caf0',
                                              size=4,
                                              line=dict(color='#72caf0',
                                                        width=0)),
                                  hovertemplate='%{x}<br>' +
                                  '<b>Water Bodies</b><br>' +
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
    figure_4_11.update_yaxes(title_text='Cumulative Change (%)',
                             tickformat=',.0%',)
    figure_4_11.update_xaxes(title_text='Year')

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
    my_text = ['{}<br>'.format(date)+
               'Min: {:.1%}<br>'.format(mn)+
               '<b>Mean: {:.1%}</b><br>'.format(mean)+
               'Max: {:.1%}<br>'.format(mx)
               for date, mean, mn,mx, in zip(list(faparDF['Date']),
                                             list(faparDF['Mean']),
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
        hovertemplate='%{text}' +
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

def figure_4_22():
    """
    Fire Index
    """
    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.11Fire/Figure4.22/'
        xls = pd.ExcelFile(
            data_path+'Figure4.22_FireIndex.xlsx')
        df = pd.read_excel(xls, 'May_Sep')
    except:
        return empty_chart()
    
    dublinTrace = go.Scatter(x=df["year"],
                     y=df["mycount"],
                     name='Dublin Airport',
                     mode='lines',  # 'line' is default
                     line=dict(
                            color=TIMESERIES_COLOR_PRIMARY,
                            width=2),
                     hovertemplate='%{x}<br>' +
                            '<b>Dublin Airport</b><br>' +
                            'Days: %{y}<extra></extra>'
                            )
    shannonTrace = go.Scatter(x=df["year"],
                        y=df["mycount.1"],
                        name='Shannon Airport',
                        mode='lines',  # 'line' is default
                        line=dict(
                                color=TIMESERIES_COLOR_SECONDARY,
                                width=2),
                        hovertemplate='%{x}<br>' +
                                '<b>Shannon Airport</b><br>' +
                                'Days: %{y}<extra></extra>'
                                )
    figure_4_22=go.Figure(data=[dublinTrace, shannonTrace], layout=TIMESERIES_LAYOUT)
    figure_4_22.update_layout(
        yaxis=dict(title='Number of Days'),
        xaxis=dict(title='Year')
    )
    return figure_4_22

def figure_4_27():
    """
    Anthropogenic Greenhouse Gas Emissions
    """
    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.14AnthropogenicGreenhouseGasEmissions/Figure4.27/'
        xls = pd.ExcelFile(
            data_path+'NIR_GHG_Emissions_CSRI2020.xlsx')
        df = pd.read_excel(xls, 'Figure 2.1')
    except:
        return empty_chart()
    df = df.drop(columns=['Unnamed: 0', 
                          'Unnamed: 31',
                          'Unnamed: 32',
                          'Unnamed: 33',
                            ])
    df.loc[1,'Total GHG emissions by sector (kt CO2e)']='Year'
    df1=df.T
    new_header = df1.iloc[0]#grab the first row for the header
    df1 = df1[1:] #take the data less the header row
    df1.columns = new_header #set the header row as the df header

    energyTrace=go.Bar(
    name="Energy",
    x=df1.Year,
    y=df1["Energy"]/1000,
        text=df1['Energy']*100/df1['Total '],
    marker_color="#5182bb",
    hovertemplate='%{x}<br>' +
    '<b>Energy</b><br>' +
    '%{y:.2f}kTCO\u2082eq<br>' +
    '%{text:.2f} %</sub><extra></extra>'
                            )

    agricultureTrace=go.Bar(
        name="Agriculture",
        x=df1.Year,
        y=df1["Agriculture "]/1000,
            text=df1['Agriculture ']*100/df1['Total '],
        marker_color="#fdbf2d",
        hovertemplate=  '%{x}<br>' +
        '<b>Agriculture</b><br>' +
        '%{y:.2f}kTCO\u2082eq<br>' +
        '%{text:.2f} %</sub><extra></extra>'
                                )

    landuseTrace=go.Bar(
        name="Land-Use Change and Forestry (LULUCF)",
        x=df1.Year,
        y=df1["Land-Use Change and Forestry (LULUCF)"]/1000,
            text=df1["Land-Use Change and Forestry (LULUCF)"]*100/df1['Total '],
        marker_color="#3dca3f",
        hovertemplate='%{x}<br>' +
        '<b>Land-Use Change and Forestry</b><br>' +
        '%{y:.2f}kTCO\u2082eq<br>' +
        '%{text:.2f} %</sub><extra></extra>'
                                )
    industryTrace=go.Bar(
        name="Industrial Processes and Product Use (IPPU)",
        x=df1.Year,
        y=df1["Industrial Processes and Product Use (IPPU)"]/1000,
        text=df1["Industrial Processes and Product Use (IPPU)"]*100/df1['Total '],
        marker_color="#fc0d1b",
        hovertemplate='%{x}<br>' +
        '<b>Industrial Processes and Product Use (IPPU)</b><br>' +
        '%{y:.2f}kTCO\u2082eq<br>' +
        '%{text:.2f} %</sub><extra></extra>'
                                )

    wasteTrace=go.Bar(
        name="Waste",
        x=df1.Year,
        y=df1['Waste ']/1000,
        text=df1['Waste ']*100/df1['Total '],
        marker_color="#262626",
        hovertemplate='%{x}<br>' +
        '<b>Agriculture</b><br>' +
        '%{y:.2f}kTCO\u2082eq<br>' +
        '%{text:.2f} %</sub><extra></extra>'
                                )
    figure_4_27=go.Figure(data=[energyTrace,
                                agricultureTrace,
                                landuseTrace,
                                industryTrace,
                                wasteTrace],
                          layout=TIMESERIES_LAYOUT)
    figure_4_27.update_layout(
        barmode='stack',
        yaxis=dict(title='kilotonnes CO\u2082 eq'),
        xaxis=dict(title='Year')
        )

    return figure_4_27

def map_4_5():
    """
    Anthropogenic Greenhouse Gas Emissions infrastructure map
    """

    try:
        data_path = DATA_PATH+'Terrestrial_Domain/4.14AnthropogenicGreenhouseGasEmissions/Map4.5/'
        df = pd.read_csv(data_path+'Map4.5_StationTable_GHG.txt', delimiter = ",")
        df = df.rename(columns={'Height_m_': 'Height__m_'})
    except:
        return empty_chart()

    map_4_5=stations_map(df)
    return map_4_5