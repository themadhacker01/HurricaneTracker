# Load all required packages
import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point
import missingno as msn
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser as wb

# Getting to know the geojson file
country = gpd.geopandas.read_file('data/gz_2010_us_040_00_5m.json')

# Print the first 5 rows in the dataframe
# Alternately, you can use the head() function
# print(country.loc[0:5])

eff_country = country[country['NAME'].isin(['Alaska', 'Hawaii']) == False]

# Plot the geo-dataframe and show it in a browser
# eff_country.plot()

# Shows the matrix plot
plt.show()

florence_data = pd.read_csv('data/hurricane_florence.csv')
# print(florence_data.info())

# Check missing data by plotting num of valid column values
msn.bar(florence_data, figsize=(10,5), fontsize=10)

# Shows the matrix plot
# plt.show()

# View basic statistical info of florence_data
# print(florence_data.describe())

# Dropping columns not required for this project
florence_data = florence_data.drop(['AdvisoryNumber', 'Forecaster', 'Received'], axis=1)
print(florence_data.head())