# How about this weather we're having?

# Background
"Nice weather we're having." "It's supposed to snow all day tomorrow." Weather frequently comes up in casual conversation. Especially in a place like Colorado where the weather can drastically change over a short period of time. I was interested in looking into weather data to identify patterns and trends. 



# Data
I started by working with a dataset that contains roughly 5 years of hourly measurements of various weather attributes from 30 North American and 6 Israeli cities. The dataset included several csv files, the first includes the latitude and longitude of each of the cities. The file “weather_descriptions”, contains hourly categorical information describing the weather conditions in each city (e.g., light rain, sky is clear, fog, scattered clouds). The other 5 files contain hourly weather measurements such as, temperature, humidity, pressure and wind speed for every city. 

Upon importing the files to dataframes and conducting some exploratory analysis of the data I noticed that the files contained some unexpected data. For example, pressure measurements that exceeded the highest ever recorded and dramatic changes in temperature (over 10 degrees in one hour) during the middle of the night. After grouping the data into data frames by city and filtering by year I cleaned the data of any unusual outliers (almost 10% of the data points). 



# Visualization 
![city temp](https://github.com/jrp8401/Weather-Capstone/blob/master/img/city_temp_hourly_2013.png)

![den_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_temp_avg-min-max_2013.png)
![sd_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_temp_avg-min-max_2013.png)
![den_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_seas_temp_avg-min-max_2013.png)
![sd_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_seas_temp_avg-min-max_2013.png)

![den_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/Denver_avg.png)
![sd_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/San%20Diego_avg.png)




# Conclusion

