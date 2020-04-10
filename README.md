# How about this weather we're having?

# Background
"Nice weather we're having." Weather frequently comes up in casual conversation. Especially in a place like Colorado where the weather can drastically change over a short period of time. I was interested in looking into weather data to identify patterns and trends between cities in differnent regions. 



# Data
I started by working with a dataset that contains roughly 5 years of hourly measurements of various weather attributes from 30 North American and 6 Israeli cities. The dataset included several csv files, the first includes the latitude and longitude of each of the cities. The file “weather_descriptions”, contains hourly categorical information describing the weather conditions in each city (e.g., light rain, sky is clear, fog, scattered clouds). The other 5 files contain hourly weather measurements such as, temperature, humidity, pressure and wind speed for every city. 

Upon importing the files to dataframes and conducting some exploratory analysis of the data I noticed that the files contained some unexpected data. For example, pressure measurements that exceeded the highest ever recorded and dramatic changes in temperature (over 10 degrees in one hour) during the middle of the night. After filtering the data by year and grouping the dataframes by city I then reoved any unusual outliers (almost 10% of the data points were NaN or an outlier). 



# Visualization 
I started of my data analysis my breaking down the data and first plotting the hourly temperatures in Denvr over a whole year. These hourly measurments show the seasonal fluctuations of temperaure over the year, cooling down during the fall and warming up in the spring. In the graph below the temperatures from San Diego show a less pronunced change in seasons as well as a tighter range of temperatures. 
![city temp](https://github.com/jrp8401/Weather-Capstone/blob/master/img/city_temp_hourly_2013.png)
I then decided to break it down further, looking at the daily average temperature across the year along with the daily min and max temperaute. Agian we can see the jagged and fluctuating range of the Denver weather compared the less dramatic San Diego temperatures. 
![den_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_temp_avg-min-max_2013.png)
![sd_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_temp_avg-min-max_2013.png)
Along with yearly patterns I thought it would be interesting to look closer at seasonal trends. In Denver we can see a more significant shift in temperatures during the fall and spring while in San Diego the difference between seasons is less profound. 
![den_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_seas_temp_avg-min-max_2013.png)
![sd_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_seas_temp_avg-min-max_2013.png)
Since I had 5 years of data I wanted to look at the average tempeatures across the year. 
![den_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/Denver_avg.png)
![sd_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/San%20Diego_avg.png)



# Conclusion
Having lived in Colorado and Southern California, the difference between their respective weather trends is obvious. However I thought it would be interesting to use data to support that claim. 

