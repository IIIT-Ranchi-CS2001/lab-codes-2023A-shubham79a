import pandas as pd
import numpy as np
df = pd.read_csv('AQI_Data.csv')

# a
# using head find first five rows
first_five_row=df.head()
print("First five row of data: \n",first_five_row)

#b
# using tail find last five rows
last_six_row=df.tail(6)
print("Last six row of data: \n",last_six_row)

#c
# using info() function to get information about the data
summary_data=df.describe()
print("Summary of data ",summary_data)

#d
# creating list for different columns
PM2_data=df["PM2.5"]
PM10_data=df["PM10"]
AQI_Data=df["AQI"]

# grouping by City and finding mean AQI , M2.5 and PM10 
mean_AQI=df.groupby('City')['AQI'].mean()
mean_PM2=df.groupby('City')['PM2.5'].mean()
mean_PM10=df.groupby('City')['PM10'].mean()


print("Mean of AQI data across different city: \n",mean_AQI)
print("Mean of PM2.5 data across different city: \n",mean_PM2)
print("Mean of PM10 data across different city: \n",mean_PM10)

