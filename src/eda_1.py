import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime



if __name__ == "__main__":
    df_temp = pd.read_csv('data/temperature.csv')
    df_temp.drop(df_temp.index[0],inplace= True)
    #print(df_temp.info())
    #pd.plotting.scatter_matrix(df_temp)
     
    #print(df_comp_van_port.head())
    
    #fig, ax = plt.subplots()
    
    
    date_before = '2014-01-01 00:00:00'
    date2 = '2013-01-01 00:00:00'
    format_date = '%Y-%m-%d %H:%M:%S'
    date_before_2013 = datetime.strptime(date_before, format_date)
    date_after = datetime.strptime(date2, format_date)
    df_temp['datetime']= pd.to_datetime(df_temp['datetime'])
    mask  =(df_temp['datetime']<date_before_2013) & (df_temp['datetime']>=date_after)
    df_temp_2012 = df_temp[mask]
    print(df_temp_2012.tail())
    print(df_temp_2012.head())
    #df_comp_van_port = df_temp_2012[['datetime','Vancouver','Portland','Phoenix','Miami','Boston',]]
    #print(df_comp_van_port.info())
    #print(df_comp_van_port.index[-1])
    #pd.plotting.scatter_matrix(df_comp_van_port)

    #df_times = df_temp_2012['datetime']
    #print(df_times.tail())
   #  df = (df_temp_2012['datetime']
   #     .dt.floor('d')
   #     .miin(dropna=True)
   #     .rename_axis('date')
   #     .reset_index(name='count')
   #     .sort_values(by='count',ascending = True))
    #print(df)
    #print (df_temp_2012.sort_values(by = 'datetime',ascending = False))
    plt.plot(df_temp_2012['datetime'],df_temp_2012['Denver'])
    plt.show()

