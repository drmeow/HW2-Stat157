# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib
from pandas import read_json
from pandas import DataFrame

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
data = read_json(urllib.urlopen(url),typ='series',convert_axes=True, dtype=True,convert_dates=True)

numbers_of_newdata=data['metadata']['count']

Src=range(numbers_of_newdata)
Eqid=range(numbers_of_newdata)
Time=range(numbers_of_newdata)
Lat=range(numbers_of_newdata)
Lon=range(numbers_of_newdata)
Depth=range(numbers_of_newdata)
Nst=range(numbers_of_newdata)
Region=range(numbers_of_newdata)
Magnitude=range(numbers_of_newdata)

for x in range(0,numbers_of_newdata) :
    Src[x]      = data['features'][x]['properties']['net']
    Eqid[x]     = data['features'][x]['properties']['code']
    Time[x]     = data['features'][x]['properties']['time']
    Lat[x]      = data['features'][x]['geometry']['coordinates'][1]
    Lon[x]      = data['features'][x]['geometry']['coordinates'][0]
    Depth[x]    = data['features'][x]['geometry']['coordinates'][2]
    Nst[x]      = data['features'][x]['properties']['nst']
    Region[x]   = data['features'][x]['properties']['place']
    Magnitude[x]=data['features'][x]['properties']['mag']

d = {'Src':Src, 'Eqid':Eqid, 'Datetime':Time , 'Lat':Lat , 'Lon':Lon ,'Magnitude':Magnitude,'Depth':Depth,'NST': Nst,'Region': Region }

dc=DataFrame(d,columns=['Src','Eqid','Datetime','Lat','Lon','Magnitude','Depth','NST','Region'])

dc

