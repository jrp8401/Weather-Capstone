import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime


def import_weather_data(file_path):
    #import file drops empty 1st row
    df_inter = pd.read_csv(file_path)
    df_inter.drop(df_inter.index[0],inplace= True)
    return df_inter
    
def split_by_date(df_inter,date_start,date_end):
    #datetime cast
    
    format_date = '%Y-%m-%d %H:%M:%S'
    date_before = datetime.strptime(date_end, format_date)
    date_after = datetime.strptime(date_start, format_date)

    df_inter['datetime']= pd.to_datetime(df_inter['datetime'])

    mask  =(df_inter['datetime']<date_before) & (df_inter['datetime']>=date_after)
    return df_inter[mask]

def filter_strange_outliers(df_year,city):
    for i in range(len(df_year[city])-1):
        while i<len(df_year[city])-1 and (abs(df_year.iloc[i][city]-df_year.iloc[i+1][city]))>14:
            df_year.drop(df_year.index[i+1],inplace = True) 
   
if __name__ == "__main__":
    #import weather csv files
    #df_humid= import_weather_data('data/humidity.csv')
    df_temp = import_weather_data('data/temperature.csv')
    #df_pres = import_weather_data('data/pressure.csv')
    #df_wind = import_weather_data('data/wind_speed.csv')
    #df_description = import_weather_data('data/weather_description.csv')
 
    


    #kelvin to f
    temp_columns = list(df_temp)
    for i in temp_columns:
        if i != 'datetime':
            df_temp[i]=df_temp[i].apply(lambda x: x*9/5- 459.67)

   
   
    #filter by year
    df_temps_year=[]

    date_end = '2013-12-01 00:00:00'
    date_start = '2012-12-01 00:00:00'
    for i in range(5):
        df_temps_year.append(split_by_date(df_temp,date_start,date_end))
        
        x=(int(date_end[3])+1)
        datex = list(date_end)
        datex[3]=str(x)
        date_end = "".join(datex)
        x=(int(date_start[3])+1)
        datex = list(date_start)
        datex[3]=str(x)
        date_start = "".join(datex)
        
        
        
    
    

    #df_humid_2012 = split_by_date(df_humid,date_start,date_end)
    #df_pres_2012 = split_by_date(df_pres,date_start,date_end)
    #df_wind_2012 = split_by_date(df_wind,date_start,date_end)
    #df_description_2012 = split_by_date(df_description,date_start,date_end)

    #filter by city
    #df_humid_2012 =  df_humid_2012[['datetime','Denver']]
    df_temp_2012_den =  df_temps_year[0][['datetime','Denver']]
    df_temp_2013_den =  df_temps_year[1][['datetime','Denver']]
    df_temp_2014_den =  df_temps_year[2][['datetime','Denver']]
    df_temp_2015_den =  df_temps_year[3][['datetime','Denver']]
    df_temp_2016_den =  df_temps_year[4][['datetime','Denver']]

   

    df_temp_2012_sd =  df_temps_year[0][['datetime','San Diego']]
    df_temp_2013_sd =  df_temps_year[1][['datetime','San Diego']]
    df_temp_2014_sd =  df_temps_year[2][['datetime','San Diego']]
    df_temp_2015_sd =  df_temps_year[3][['datetime','San Diego']]
    df_temp_2016_sd =  df_temps_year[4][['datetime','San Diego']]

    

    #df_pres_2012 =  df_pres_2012[['datetime','Denver']]
    #df_wind_2012 =  df_wind_2012[['datetime','Denver']]
    #df_description_2012 =  df_description_2012[['datetime','Denver']] 
    #print(df_description_2012['Denver'].unique())

    #drop inaccurate pressures
    #df_pres_2012.drop(df_pres_2012[df_pres_2012['Denver']<990].index,inplace = True)
    #df_pres_2012.drop(df_pres_2012[df_pres_2012['Denver']>1045].index,inplace = True)

    df_temp_2012=df_temp_2012_den.copy()
    filter_strange_outliers(df_temp_2012,'Denver')
    df_temp_2012_daily_mean = df_temp_2012.groupby([df_temp_2012['datetime'].dt.date])['Denver'].mean()

    df_temp_2013=df_temp_2013_den.copy()
    filter_strange_outliers(df_temp_2013,'Denver')
    df_temp_2013_daily_mean = df_temp_2013.groupby([df_temp_2013['datetime'].dt.date])['Denver'].mean()

    df_temp_2014=df_temp_2014_den.copy()
    filter_strange_outliers(df_temp_2014,'Denver')
    df_temp_2014_daily_mean = df_temp_2014.groupby([df_temp_2014['datetime'].dt.date])['Denver'].mean()

    df_temp_2015=df_temp_2015_den.copy()
    filter_strange_outliers(df_temp_2015,'Denver')
    df_temp_2015_daily_mean = df_temp_2015.groupby([df_temp_2015['datetime'].dt.date])['Denver'].mean()

    df_temp_2016=df_temp_2016_den.copy()
    filter_strange_outliers(df_temp_2016,'Denver')
    df_temp_2016_daily_mean = df_temp_2016.groupby([df_temp_2016['datetime'].dt.date])['Denver'].mean()
   


    
    df_temp_y_sd = df_temp_2012_sd.copy()
    filter_strange_outliers(df_temp_y_sd,'San Diego')
    #calc nans    
   
    print(1-(len(df_temp_2012['Denver'].dropna())/len(df_temp_2012_den)))
    print(1-(len(df_temp_2013['Denver'].dropna())/len(df_temp_2013_den)))
    print(1-(len(df_temp_2014['Denver'].dropna())/len(df_temp_2014_den)))
    print(1-(len(df_temp_2015['Denver'].dropna())/len(df_temp_2015_den)))
    print(1-(len(df_temp_2016['Denver'].dropna())/len(df_temp_2016_den)))

    print(1-(len(df_temp_y_sd['San Diego'].dropna())/len(df_temp_2012_sd)))
    
   
    

    

   
    #year of temps by hour
    fig, ax = plt.subplots(2)
    ax[0].title.set_text("Denver temperatures by hour")
    ax[0].plot(df_temp_2012['datetime'],df_temp_2012['Denver'],color = "tab:red")
   
    
    ax[1].title.set_text("San Diego temperatures by hour")
    ax[1].plot(df_temp_2012_sd['datetime'],df_temp_2012_sd['San Diego'],color = "tab:red")
    plt.ylim(-5,100)
    plt.savefig('img/city_temp_hourly_2013')
    plt.show()
    
 
    #calc and plot
    #daily mean, max, min 
    plt.plot(df_temp_2012['datetime'],df_temp_2012['Denver'],color = "tab:red",alpha =.25)
    plt.title("Denver temperatures by hour")
    
    
    
    
    
    df_temp_2012_daily_min = df_temp_2012.groupby([df_temp_2012['datetime'].dt.date])['Denver'].min()
    df_temp_2012_daily_max = df_temp_2012.groupby([df_temp_2012['datetime'].dt.date])['Denver'].max()
   
    plt.plot(df_temp_2012_daily_mean,label="daily mean temperature")
    plt.plot(df_temp_2012_daily_min,label="daily min temperature")
    plt.plot(df_temp_2012_daily_max,label="daily max temperature")
    plt.legend()
    plt.ylim(-5,100) 
    plt.savefig('img/den_temp_avg-min-max_2013')
    plt.show()

    plt.plot(df_temp_2012_sd['datetime'],df_temp_2012_sd['San Diego'],color = "tab:red",alpha =.25)
    plt.title("San Diego temperatures by hour")
    df_temp_2012_daily_mean_sd = df_temp_2012_sd.groupby([df_temp_2012_sd['datetime'].dt.date])['San Diego'].mean()
    df_temp_2012_daily_min_sd = df_temp_2012_sd.groupby([df_temp_2012_sd['datetime'].dt.date])['San Diego'].min()
    df_temp_2012_daily_max_sd = df_temp_2012_sd.groupby([df_temp_2012_sd['datetime'].dt.date])['San Diego'].max()
   
    plt.plot(df_temp_2012_daily_mean_sd,label="daily mean temperature")
    plt.plot(df_temp_2012_daily_min_sd,label="daily min temperature")
    plt.plot(df_temp_2012_daily_max_sd,label="daily max temperature")
    plt.legend()
    plt.ylim(-5,100)
    plt.savefig('img/sd_temp_avg-min-max_2013')
    plt.show()

    #aggregate
    df_temp_2012_daily_mean.rename(index = lambda s: s.strftime('%m-%d'),inplace=True)
    df_temp_2013_daily_mean.rename(index = lambda s: s.strftime('%m-%d'),inplace=True)
    df_temp_2014_daily_mean.rename(index = lambda s: s.strftime('%m-%d'),inplace=True)
    df_temp_2015_daily_mean.rename(index = lambda s: s.strftime('%m-%d'),inplace=True)
    df_temp_2016_daily_mean.rename(index = lambda s: s.strftime('%m-%d'),inplace=True)
    agg_temp = pd.concat([df_temp_2012_daily_mean,df_temp_2013_daily_mean,df_temp_2014_daily_mean,df_temp_2015_daily_mean,df_temp_2016_daily_mean] ,axis =1)
    agg_temp = agg_temp[:-1]
    
    agg_temp['mean'] = agg_temp.mean(axis=1)
    agg_temp.reset_index().plot(x='index',y ='mean')
    plt.savefig('img/den_avg')
    plt.show()
   


    #seasonal
    df_seasons = df_temp_2012.copy()
    df_seasons_sd = df_temp_2012_sd.copy()
    date_end = '2013-03-01 00:00:00'
    date_start = '2012-12-01 00:00:00'
    df_winter_temp  = split_by_date(df_seasons,date_start,date_end)
    df_winter_temp_sd  = split_by_date(df_seasons_sd,date_start,date_end)
    date_end = '2013-06-01 00:00:00'
    date_start = '2013-03-01 00:00:00'
    df_spring_temp  = split_by_date(df_seasons,date_start,date_end)
    df_spring_temp_sd  = split_by_date(df_seasons_sd,date_start,date_end)
    date_end = '2013-09-01 00:00:00'
    date_start = '2013-06-01 00:00:00'
    df_sum_temp  = split_by_date(df_seasons,date_start,date_end)
    df_sum_temp_sd  = split_by_date(df_seasons_sd,date_start,date_end)
    date_end = '2013-12-01 00:00:00'
    date_start = '2013-09-01 00:00:00'
    df_fall_temp_sd  = split_by_date(df_seasons_sd,date_start,date_end)
    df_fall_temp  = split_by_date(df_seasons,date_start,date_end)
    
     
    
    df_winter_temp_mean = df_winter_temp.groupby([df_winter_temp['datetime'].dt.date])['Denver'].mean()
    df_spring_temp_mean = df_spring_temp.groupby([df_spring_temp['datetime'].dt.date])['Denver'].mean()
    df_sum_temp_mean = df_sum_temp.groupby([df_sum_temp['datetime'].dt.date])['Denver'].mean()
    df_fall_temp_mean = df_fall_temp.groupby([df_fall_temp['datetime'].dt.date])['Denver'].mean()

    df_winter_temp_max = df_temp_2012.groupby([df_winter_temp['datetime'].dt.date])['Denver'].max()
    df_winter_temp_min = df_temp_2012.groupby([df_winter_temp['datetime'].dt.date])['Denver'].min()
   
    df_spring_temp_max = df_temp_2012.groupby([df_spring_temp['datetime'].dt.date])['Denver'].max()
    df_spring_temp_min = df_temp_2012.groupby([df_spring_temp['datetime'].dt.date])['Denver'].min()

    df_sum_temp_max = df_temp_2012.groupby([df_sum_temp['datetime'].dt.date])['Denver'].max()
    df_sum_temp_min = df_temp_2012.groupby([df_sum_temp['datetime'].dt.date])['Denver'].min()
    
    df_fall_temp_max = df_temp_2012.groupby([df_fall_temp['datetime'].dt.date])['Denver'].max()
    df_fall_temp_min = df_temp_2012.groupby([df_fall_temp['datetime'].dt.date])['Denver'].min()
   
    fig, axes =plt.subplots(2,2)
    axes[0,0].plot(df_winter_temp_mean)
    axes[0,0].plot(df_winter_temp_max)
    axes[0,0].plot(df_winter_temp_min)
    axes[0,0].set_title('Winter')
    axes[0,1].plot(df_spring_temp_mean) 
    axes[0,1].plot(df_spring_temp_max) 
    axes[0,1].plot(df_spring_temp_min) 
    axes[0,1].set_title('Spring')
    axes[1,0].plot(df_sum_temp_mean)
    axes[1,0].set_title('Summer')
    axes[1,0].plot(df_sum_temp_max)
    axes[1,0].plot(df_sum_temp_min)
    axes[1,1].plot(df_fall_temp_mean)
    axes[1,1].plot(df_fall_temp_max)
    axes[1,1].plot(df_fall_temp_min)
    axes[1,1].set_title('Fall')
    for ax in axes.flatten():
         ax.set_ylim(-5,100)
    plt.savefig('img/den_seas_temp_avg-min-max_2013')
    plt.show()



    df_winter_temp_mean_sd = df_winter_temp_sd.groupby([df_winter_temp_sd['datetime'].dt.date])['San Diego'].mean()
    df_spring_temp_mean_sd = df_spring_temp_sd.groupby([df_spring_temp_sd['datetime'].dt.date])['San Diego'].mean()
    df_sum_temp_mean_sd = df_sum_temp_sd.groupby([df_sum_temp_sd['datetime'].dt.date])['San Diego'].mean()
    df_fall_temp_mean_sd = df_fall_temp_sd.groupby([df_fall_temp_sd['datetime'].dt.date])['San Diego'].mean()

    df_winter_temp_max_sd = df_temp_2012_sd.groupby([df_winter_temp_sd['datetime'].dt.date])['San Diego'].max()
    df_winter_temp_min_sd = df_temp_2012_sd.groupby([df_winter_temp_sd['datetime'].dt.date])['San Diego'].min()
   
    df_spring_temp_max_sd = df_temp_2012_sd.groupby([df_spring_temp_sd['datetime'].dt.date])['San Diego'].max()
    df_spring_temp_min_sd = df_temp_2012_sd.groupby([df_spring_temp_sd['datetime'].dt.date])['San Diego'].min()

    df_sum_temp_max_sd = df_temp_2012_sd.groupby([df_sum_temp_sd['datetime'].dt.date])['San Diego'].max()
    df_sum_temp_min_sd = df_temp_2012_sd.groupby([df_sum_temp_sd['datetime'].dt.date])['San Diego'].min()
    
    df_fall_temp_max_sd = df_temp_2012_sd.groupby([df_fall_temp_sd['datetime'].dt.date])['San Diego'].max()
    df_fall_temp_min_sd = df_temp_2012_sd.groupby([df_fall_temp_sd['datetime'].dt.date])['San Diego'].min()
   
    fig, axes =plt.subplots(2,2)
    axes[0,0].plot(df_winter_temp_mean_sd)
    axes[0,0].plot(df_winter_temp_max_sd)
    axes[0,0].plot(df_winter_temp_min_sd)
    axes[0,0].set_title('Winter')
    axes[0,1].plot(df_spring_temp_mean_sd) 
    axes[0,1].plot(df_spring_temp_max_sd) 
    axes[0,1].plot(df_spring_temp_min_sd) 
    axes[0,1].set_title('Spring')
    axes[1,0].plot(df_sum_temp_mean_sd)
    axes[1,0].set_title('Summer')
    axes[1,0].plot(df_sum_temp_max_sd)
    axes[1,0].plot(df_sum_temp_min_sd)
    axes[1,1].plot(df_fall_temp_mean_sd)
    axes[1,1].plot(df_fall_temp_max_sd)
    axes[1,1].plot(df_fall_temp_min_sd)
    axes[1,1].set_title('Fall')
    for ax in axes.flatten():
         ax.set_ylim(-5,100)
    plt.savefig('img/sd_seas_temp_avg-min-max_2013')     
    plt.show()

   
    
    

