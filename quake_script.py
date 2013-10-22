# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib
from pandas import read_json
from pandas import DataFrame
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from mpl_toolkits.basemap import Basemap

# <codecell>

#now, plot the data
def plot_quakes(quakes, box):
    m = Basemap(llcrnrlon=box['llcrnrlon'],llcrnrlat=box['llcrnrlat'],
                urcrnrlon=box['urcrnrlon'],urcrnrlat=box['urcrnrlat'],
                resolution='l',area_thresh=1000.,projection='merc')
    m.drawcountries()
    m.fillcontinents(color='green',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    x, y = m(quakes.Lon, quakes.Lat)
    m.scatter(x, y, s=10*quakes.Magnitude, c=quakes.Depth, zorder=2)
    return m

# <codecell>
# <codecell>

def Milli_to_DateTime(millisec): #converting millsec time data into recognizable time data 
    utc = pytz.utc # setting UTC 
    fmt = '%A, %B %d, %Y %H:%M:%S %Z' #setting output 
    all_converted=range(len(millisec)) #declare variable

    for x in range(0,len(millisec)): #converting all millsec data into recognizable time data
        utc_dt = utc.localize(datetime.utcfromtimestamp(millisec[x]/1000))
        converted=utc_dt.strftime(fmt)
        all_converted[x]=converted #boom! done!
    return(all_converted) #booom returns 

# <codecell>

#DataCleaning function will scrap the data from http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php and save it to your 
#local workspace. Input variable is going to verify which type of data you want to scrap. 
#valid input variables are "past hour", "past day", "past 7days", "past 30days"

def DataCleaning(whichdata): 
    
    if not whichdata in ["past hour", "past day", "past 7days", "past 30days"]: #this if statement will verify if you put valid input or not
        
        print("Invalid input bro, gg. Valid inputs are \"past hour\", \"past day\", \"past 7days\", \"past 30days\"") #error sign!
    
    else:
    
        if whichdata == "past hour": # scrap past hour data
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
            data = read_json(urllib.urlopen(url),typ='series',convert_axes=True, dtype=True,convert_dates=True)
         
        elif whichdata == "past day": # scrap past day data
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
            data = read_json(urllib.urlopen(url),typ='series',convert_axes=True, dtype=True,convert_dates=True)
        
        elif whichdata == "past 7days": # scrap past 7days data
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
            data = read_json(urllib.urlopen(url),typ='series',convert_axes=True, dtype=True,convert_dates=True)
        
        elif whichdata == "past 30days": # scrap past 30days data
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
            data = read_json(urllib.urlopen(url),typ='series',convert_axes=True, dtype=True,convert_dates=True)
            
        
        numbers_of_newdata=data['metadata']['count'] #counting numbers of data 
       
        Src=range(numbers_of_newdata) #declare variables
        Eqid=range(numbers_of_newdata)
        Time=range(numbers_of_newdata)
        Lat=range(numbers_of_newdata)
        Lon=range(numbers_of_newdata)
        Depth=range(numbers_of_newdata)
        Nst=range(numbers_of_newdata)
        Region=range(numbers_of_newdata)
        Magnitude=range(numbers_of_newdata)
    
    
        for x in range(0,numbers_of_newdata) : #read data that we need and save it to corresponding variables in your local repository
            Src[x]      = data['features'][x]['properties']['net']
            Eqid[x]     = data['features'][x]['properties']['code']
            Time[x]     = data['features'][x]['properties']['time']
            Lat[x]      = data['features'][x]['geometry']['coordinates'][1]
            Lon[x]      = data['features'][x]['geometry']['coordinates'][0]
            Depth[x]    = data['features'][x]['geometry']['coordinates'][2]
            Nst[x]      = data['features'][x]['properties']['nst']
            Region[x]   = data['features'][x]['properties']['place']
            Magnitude[x]=data['features'][x]['properties']['mag']
        
        converted_time= Milli_to_DateTime(Time)
        rawdata= {'Src':Src, 'Eqid':Eqid, 'Datetime':converted_time , 'Lat':Lat , 'Lon':Lon ,'Magnitude':Magnitude,'Depth':Depth,'NST': Nst,'Region': Region }
        #making data set by using variables that we obtained
        converted_rawdata=DataFrame(rawdata,columns=['Src','Eqid','Datetime','Lat','Lon','Magnitude','Depth','NST','Region'])
        #converting data set into data frame
        without_NA_data=converted_rawdata.dropna(axis=0, how='any')
        #droppppiiinnnggggg each row if it has at least one na value
    
        if without_NA_data.shape[0] == 0: #checking if the final dataframe is empty
           
            print("Data is not available since each row contains at least one NA. Empty DataFrame! rofl!")

        return(without_NA_data) #returning final dataframe

# <codecell>

DataCleaning("Dayum") #testing for invalid input

# <codecell>

past_hour=DataCleaning("past hour") #this will scrap past hour data and save it to your local worksapce
past_hour

# <codecell>

past_day=DataCleaning("past day") #this will scrap past day data and save it to your local worksapce
past_day

# <codecell>

past_7days=DataCleaning("past 7days") #this will scrap past 7days data and save it to your local worksapce
past_7days[0:30] #printing  first 30 data

# <codecell>

past_30days=DataCleaning("past 30days") #this will scrap past 30days data and save it to your local worksapce
past_30days[0:30] #printing first 30 


Alaska=past_7days[past_7days['Src']=='ak']

# <codecell>

#For alaska
box1 = {'llcrnrlon' : -180, 'llcrnrlat' : 50., 'urcrnrlon' : -120., 'urcrnrlat' : 72}
plot_quakes(Alaska, box1)

# <codecell>

#For any other states

CI=past_7days[past_7days['Src']=='ci']
box1 = {'llcrnrlon' : -130, 'llcrnrlat' :30, 'urcrnrlon' : -70., 'urcrnrlat' : 50}
plot_quakes(CI, box1)

