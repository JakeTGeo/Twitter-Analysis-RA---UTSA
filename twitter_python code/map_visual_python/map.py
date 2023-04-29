import pandas as pd
import numpy as np
import xlsxwriter
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon


cols = [3,4,5,6] # cols == id, text, geobox1, gb2, gb3, gb4, year, day, month, sentiment value

gb1 = []
gb2 = []
gb3 = []
gb4 = []

df = pd.read_excel('parsed_twt_data.xlsx', usecols=cols)

id_tweet = df.to_numpy()

for item in id_tweet:   
    gb1.append(item[0])
    gb2.append(item[1])
    gb3.append(item[2])
    gb4.append(item[3])
    

lat_list =  []
long_list = []
coord_list = []

for i in range(len(gb1)):
    latitude = (gb2[i]+gb4[i])/2
    longitude = (gb1[i]+gb3[i])/2
    lat_list.append(latitude)
    long_list.append(longitude)
    coord_list.append(str(latitude) + "," + str(longitude))


ecuador_map = gpd.read_file(r'/home/jake/twitter_quarto/stanford-sb978rn7613-shapefile/sb978rn7613.shp')
fig,ax = plt.subplots(figsize = (15,15))
ecuador_map.plot(ax = ax)
geometry = [Point(xy) for xy in zip(long_list,lat_list)]
geo_df = gpd.GeoDataFrame(geometry = geometry)
print(geo_df)
g = geo_df.plot(ax = ax, markersize = 20, color = 'red',marker = '*',label = 'Ecuador')
plt.show()
