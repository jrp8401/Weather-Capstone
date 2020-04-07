import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime



if __name__ == "__main__":
    #import humidity drop empty 1st row
    df_humid = pd.read_csv('data/humidity.csv')
    df_humid.drop(df_humid.index[0],inplace= True)


    #filter by year
    #datetime cast
    date_end = '2014-01-01 00:00:00'
    date_start = '2013-01-01 00:00:00'
    format_date = '%Y-%m-%d %H:%M:%S'
    date_before = datetime.strptime(date_end, format_date)
    date_after = datetime.strptime(date_start, format_date)
   

    df_humid['datetime']= pd.to_datetime(df_humid['datetime'])

    mask  =(df_humid['datetime']<date_before) & (df_humid['datetime']>=date_after)
    df_humid_2012 = df_humid[mask]

    #filter by Denver
    df_humid_2012 =  df_humid_2012[['datetime','Denver']]

    #df_humid_2012.dropna(inplace=True)
    print(df_humid_2012)
    #calc and plot
    #daily/ monthly mean, max, min 
    df_humid_2012_daily_mean = df_humid_2012.groupby([df_humid_2012['datetime'].dt.date])['Denver'].mean()
    df_humid_2012_monthly_mean = df_humid_2012.groupby([df_humid_2012['datetime'].dt.month])['Denver'].mean()
    #print(df_humid_2012_daily_mean)
    
    #print(df_humid_2012_monthly_mean)
    

    plt.plot(df_humid_2012['datetime'],df_humid_2012['Denver'])
    plt.show()
    
    plt.plot(df_humid_2012)
    
    plt.show()
    plt.plot(df_humid_2012_monthly_mean)
    plt.show()


    #import temp drop empty 1st row
    df_temp = pd.read_csv('data/temperature.csv')
    df_temp.drop(df_temp.index[0],inplace= True)

    #kelvin to f
    temp_columns = list(df_temp)
    for i in temp_columns:
        if i != 'datetime':
            df_temp[i]=df_temp[i].apply(lambda x: x*9/5- 459.67)

    #filter by year
    #datetime cast
    date_end = '2014-01-01 00:00:00'
    date_start = '2013-01-01 00:00:00'
    format_date = '%Y-%m-%d %H:%M:%S'
    date_before = datetime.strptime(date_end, format_date)
    date_after = datetime.strptime(date_start, format_date)
   
    df_temp['datetime']= pd.to_datetime(df_temp['datetime'])

    mask  =(df_temp['datetime']<date_before) & (df_temp['datetime']>=date_after)
    df_temp_2012 = df_temp[mask]
 
    #filter by Denver
    df_temp_2012_Den =  df_temp_2012[['datetime','Denver']]
    

    #calc and plot
    #daily/ monthly mean, max, min 
    df_temp_2012_daily_mean = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.date])['Denver'].mean()
    df_temp_2012_daily_min = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.date])['Denver'].min()
    df_temp_2012_daily_max = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.date])['Denver'].max()
    # print(len(df_temp_2012_daily_min))
    # print(len(df_temp_2012_daily_max))
    # print(df_temp_2012_daily_min.head())
    # print(df_temp_2012_daily_max.head())

    df_temp_2012_monthly_mean = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.month])['Denver'].mean()
    
    df_temp_2012_monthly_min = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.month])['Denver'].min()
    df_temp_2012_monthly_max = df_temp_2012_Den.groupby([df_temp_2012_Den['datetime'].dt.month])['Denver'].max()
    #print(df_temp_2012_monthly_mean)
    # print(df_temp_2012_monthly_min)
    # print(df_temp_2012_monthly_max)

    # plt.plot(df_temp_2012_daily_mean)
    # plt.plot(df_temp_2012_daily_min)
    # plt.plot(df_temp_2012_daily_max)
    # plt.show()
    
    # plt.plot(df_temp_2012_monthly_mean)
    # plt.plot(df_temp_2012_monthly_min)
    # plt.plot(df_temp_2012_monthly_max)
    # plt.show()