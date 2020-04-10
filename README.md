# How about this weather we're having?

# Background
"Nice weather we're having." Weather frequently comes up in casual conversation. Especially in a place like Colorado where the weather can drastically change over a short period of time. I was interested in looking into weather data to identify patterns and trends between cities in different regions. 



# Data
I started by working with a dataset that contains roughly 5 years of hourly measurements of various weather attributes from 30 North American and 6 Israeli cities. The dataset included several csv files, the first includes the latitude and longitude of each of the cities. The file “weather_descriptions”, contains hourly categorical information describing the weather conditions in each city (e.g., light rain, sky is clear, fog, scattered clouds). The other 5 files contain hourly weather measurements such as, temperature, humidity, pressure and wind speed for every city. 

Upon importing the files to dataframes and conducting some exploratory analysis of the data I noticed that the files contained some unexpected data. For example, pressure measurements that exceeded the highest ever recorded and dramatic changes in temperature (over 10 degrees in one hour) during the middle of the night. After filtering the data by year and grouping the data frames by city I then removed any unusual outliers (almost 10% of the data points were NaN or an outlier). 



# Visualization 
I started my data analysis by breaking down the data and first plotting the hourly temperatures in Denver over a whole year. These hourly measurements show the seasonal fluctuations of temperature over the year, cooling down during the fall and warming up in the spring. In the graph below, the temperatures from San Diego show a less pronounced change in seasons as well as a tighter range of temperatures. 
![city temp](https://github.com/jrp8401/Weather-Capstone/blob/master/img/city_temp_hourly_2013.png)
I then decided to break it down further, looking at the daily average temperature across the year along with the daily min and max temperature. Again we can see the jagged and fluctuating range of the Denver weather compared to the less dramatic San Diego temperatures. 
![den_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_temp_avg-min-max_2013.png)
![sd_temp_avg/min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_temp_avg-min-max_2013.png)
Along with yearly patterns I thought it would be interesting to look closer at seasonal trends. In Denver we can see a more significant shift in temperatures during the fall and spring while in San Diego the difference between seasons is less profound. 
![den_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/den_seas_temp_avg-min-max_2013.png)
![sd_seas_temp_min/max](https://github.com/jrp8401/Weather-Capstone/blob/master/img/sd_seas_temp_avg-min-max_2013.png)
Since I had 5 years of data I wanted to look at the average temperatures across the year. I found the mean temperature for each day of the year then took the average of those temperatures to get the average daily temperature. In the graphs below we can see that daily temperatures in Denver vary more from the average temperature compared to San Diego where the daily weather is usually near the average temperature.  
![den_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/Denver_avg.png)
![sd_temp_avg](https://github.com/jrp8401/Weather-Capstone/blob/master/img/San%20Diego_avg.png)

 City |  Variance from average daily temperature |
| ----------- | ----------- |
| Vancouver | 108.437016 |
| Portland |	115.885443 |
| San Francisco	| 38.630592 | 
| Seattle |	93.180499 |
| Los Angeles	| 55.981205 | 
| San Diego	| 43.936270 |
| Las Vegas |	275.076767 |
| Phoenix	| 217.730430 | 
| Albuquerque |	209.952227 |
| Denver |	237.677658 | 
| San Antonio |	140.089234 |
| Dallas |	198.577960 |
| Houston |	122.060735 |
| Kansas City |	293.165061 |
| Minneapolis |	427.482404 |
| Saint Louis |	290.575655 |
| Chicago |	295.071550 |
| Nashville |	210.602561 |
| Indianapolis |	278.771693 |
| Atlanta	| 165.325437 |
| Detroit | 307.686943 |
| Jacksonville | 89.419098 |
| Charlotte	| 183.097047 |
| Miami	| 26.874393 |
| Pittsburgh |	252.221896 |
| Toronto	| 286.368947 |
| Philadelphia	| 256.063830 |
| New York	| 264.650935 |
| Montreal |	376.453602 |
| Boston |	245.386079 |
| Beersheba	| 79.017834 |
| Tel Aviv District |	98.163350 |
| Eilat	| 160.218980 |
| Haifa |	89.528480 |
| Nahariyya	| 88.939186 |
| Jerusalem	| 96.141791 |






# Conclusion
Having lived in Colorado and Southern California, the difference between their respective weather trends is obvious. However I thought it would be interesting to use data to support that claim. By calculating the daily mean temperatures for a city and comparing them to the average daily temperature I can see how the temperature varies from the average over a year. 

