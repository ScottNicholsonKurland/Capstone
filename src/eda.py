import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


df=pd.read_csv('Issued_Construction_Permits.csv')
dfa=df[df['TotalNewAddSQFT']>0]
iris=dfa[['OriginalZip','Longitude','Latitude','TotalNewAddSQFT', 'TotalJobValuation','NumberOfFloors']]
iris['TotalJobValuation']=iris['TotalJobValuation'].str.lstrip('$')
iris.fillna(value=0)
iris['TotalJobValuation']=iris['TotalJobValuation'].astype(float)
iris.dropna(inplace=True)

dfa.info()

dfa.drop(['IssuedInLast30Days','IssuanceMethod','Location','TCAD_ID','CalendarYearIssued','FiscalYearIssued','DayIssued','OriginalState','CouncilDistrict','Jurisdiction'],axis=1,inplace=True)

plt.figure(figsize=(15,6))
zip_counts = dfa['OriginalZip'].value_counts()
ax1 = zip_counts.plot(kind='bar');
labels = []
for i, label in enumerate(zip_counts.index):
    labels.append('{} - ({})'.format(label, zip_counts[label]))
ax1.set_xticklabels(labels);
#Downtown - 78701 - had a tenth the *residential* development of 78702; huh.
dfa['NumberOfFloors'].describe()

plt.figure(figsize=(15,6))
floor_counts = dfa['NumberOfFloors'].value_counts()
ax1 = floor_counts.plot(kind='bar');
labels = []
for i, label in enumerate(floor_counts.index):
    labels.append('{} - ({})'.format(label, floor_counts[label]))
ax1.set_xticklabels(labels);
#Zero-floor projects e.g. parking lots.


plt.figure(figsize=(15,6))
desc_counts = dfa['PermitClass'].value_counts()
ax1 = desc_counts.plot(kind='bar');
labels = []
for i, label in enumerate(desc_counts.index):
    labels.append('{} - ({})'.format(label, desc_counts[label]))
ax1.set_xticklabels(labels);


plt.figure(figsize=(15,6))
jv_counts = dfa['TotalJobValuation'].value_counts()
ax1 = jv_counts.plot(kind='hist');
labels = []
for i, label in enumerate(jv_counts.index):
    labels.append('{} - ({})'.format(label, jv_counts[label]))
ax1.set_xticklabels(labels);
#Most projects are $100k-$250k


dfa['PermitClass'].unique()

print(dfa['HousingUnits'].sum())
dfa.sort_values('HousingUnits', ascending=False)

df['TotalNewAddSQFT'].sum()
#Over eleven million square feet; seems low for over a hundred new people per day,
#but a lot of construction is likely unpermitted and many move into Austin metro
#- 4300 square miles and 2 million people, not Austin, 272 square miles and 950K people.

plt.figure(figsize=(22,11))
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.title('Austin new square footage')
plt.scatter(dfa['Longitude'],dfa['Latitude'], s=dfa['TotalNewAddSQFT']/666,c='g')

''' This uses the Bokeh package so you will have to make sure it is loaded'''

from bokeh.models import (
   GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
 )
from bokeh.io import output_file, show, output_notebook



# Uncomment out this line to work within the jupyter notebook.
# If left commented out map should show in new window

output_notebook()

#creating the plot

## Set up the center point zoom and location for a given map
map_options = GMapOptions(lat=30.307182, lng=-97.76, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=Range1d(), y_range=Range1d(), map_options=map_options
)

plot.title.text = "Austin"

'''
This is someone else's API key so you should get your own at https://console.developers.google.com/apis/

You will need to make sure you have set up the permissions and services so you can use this.

I believe you need at least 
Google Maps JavaScript API
Google Static Maps API
Maybe more'''
plot.api_key = "AIzaSyBl6OOSxtxS7qmNgkm6EXdY6MSdVrHW8h4"



'''Here you will pass a list of the locations you want to show on the graph
The lats and longs are broken up into 2 lists'''
completed_lats = dfa['Latitude'].values
completed_longs = dfa['Longitude'].values
size=(dfa['TotalNewAddSQFT'].values**.333333)/5


'''Setup for displaying the cordinates'''
completed_source = ColumnDataSource( data=dict(
    lat=completed_lats,
    lon=completed_longs,
    alpha=size))

'''The dots are put together and added to the plot'''
completed_dots = Circle(x="lon", y="lat", size='alpha', fill_color="red", fill_alpha=.5, line_color=None)
plot.add_glyph(completed_source, completed_dots)


'''This line setups up what functionality to allow (zoom etc)'''
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

'''Show the map'''
show(plot)