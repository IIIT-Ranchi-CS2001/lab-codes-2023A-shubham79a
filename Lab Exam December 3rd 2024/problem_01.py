import pandas as pd

df = pd.read_csv('AQI_Data.csv')

# finding the average AQI data for different cities
AQI_Data=df["AQI"]
mean_AQI_by_city=df.groupby('City')['AQI'].mean()


highest_city = None
highest_value = -1

lowest_city = None
lowest_value = 100000

# finding min max through traversing the dictionary
for city, avg_aqi in mean_AQI_by_city.items():
    if avg_aqi > highest_value:  
        highest_city = city
        highest_value = avg_aqi
    if avg_aqi < lowest_value: 
        lowest_city = city
        lowest_value = avg_aqi

print(f"City with the highest average AQI: {highest_city} ({highest_value:.2f})")
print(f"City with the lowest average AQI: {lowest_city} ({lowest_value:.2f})")