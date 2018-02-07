
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


# In[8]:


df=pd.read_csv('Issued_Construction_Permits.csv')


# In[23]:


ls


# In[9]:


dfa=df[df['TotalNewAddSQFT']>0]
iris=dfa[['OriginalZip','Longitude','Latitude','TotalNewAddSQFT', 'TotalJobValuation','NumberOfFloors']]
iris['TotalJobValuation']=iris['TotalJobValuation'].str.lstrip('$')
iris.fillna(value=0)
iris['TotalJobValuation']=iris['TotalJobValuation'].astype(float)
iris.dropna(inplace=True)


# In[ ]:


#dfa['TotalJobValuation']=dfa['TotalJobValuation'].str.lstrip('$')
#dfa.fillna(value=0)
#dfa['TotalJobValuation']=dfa['TotalJobValuation'].astype(float)
#dfa.dropna(inplace=True)


# In[11]:


dfa.groupby(['IssuedDate']).mean()


# In[10]:


dfa.info()


# In[20]:


y=iris['TotalNewAddSQFT']
#y=y.iloc[1:]
x=iris.drop(labels='TotalNewAddSQFT',axis=1)
#x=x.iloc[0:-1]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=28)
rf = RandomForestRegressor()
rf.fit(X_train,y_train)
rf.score(X_test,y_test)


# In[ ]:


dfa.drop(['IssuedInLast30Days','IssuanceMethod','Location','TCAD_ID','CalendarYearIssued','FiscalYearIssued','DayIssued','OriginalState','CouncilDistrict','Jurisdiction'],axis=1,inplace=True)


# Build a random forest to predict total square footage on by month and by zip code basis for 2017 in Austin.

# In[12]:


dfa['IssuedDate']=pd.to_datetime(dfa['IssuedDate'])


# In[21]:


dfa.groupby(['IssuedDate','OriginalZip'])['TotalNewAddSQFT'].mean()
tbz=dfa.groupby(['OriginalZip'])['TotalNewAddSQFT'].sum()
tbz.nlargest(55)


# In[ ]:


dfa.std()


# In[19]:


df.shape


# In[ ]:


plt.figure(figsize=(15,6))
zip_counts = dfa['OriginalZip'].value_counts()
ax1 = zip_counts.plot(kind='bar');
labels = []
for i, label in enumerate(zip_counts.index):
    labels.append('{} - ({})'.format(label, zip_counts[label]))
ax1.set_xticklabels(labels);
#Downtown - 78701 - had a tenth the *residential* development of 78702; huh.


# In[ ]:


plt.figure(figsize=(15,6))
floor_counts = dfa['NumberOfFloors'].value_counts()
ax1 = floor_counts.plot(kind='bar');
labels = []
for i, label in enumerate(floor_counts.index):
    labels.append('{} - ({})'.format(label, floor_counts[label]))
ax1.set_xticklabels(labels);


# What the heck is a zero story project?! And two-story projects are half again as common as one-story.

# In[ ]:


plt.figure(figsize=(15,6))
desc_counts = dfa['PermitClass'].value_counts()
ax1 = desc_counts.plot(kind='bar');
labels = []
for i, label in enumerate(desc_counts.index):
    labels.append('{} - ({})'.format(label, desc_counts[label]))
ax1.set_xticklabels(labels);


# In[ ]:


plt.figure(figsize=(15,6))
jv_counts = dfa['TotalJobValuation'].value_counts()
ax1 = jv_counts.plot(kind='hist');
labels = []
for i, label in enumerate(jv_counts.index):
    labels.append('{} - ({})'.format(label, jv_counts[label]))
ax1.set_xticklabels(labels);
#Most projects are $150k-$250k


# In[ ]:


dfa['PermitClass'].unique()


# In[ ]:


dfa[dfa['Condominium']=='Yes'].count()


# In[ ]:


print(dfa[dfa['Condominium']=='Yes']['TotalNewAddSQFT'].sum())
print(dfa.sort_values('TotalNewAddSQFT', ascending=False))
howmany=dfa['ProjectName'].unique()
howmany.shape


# In[ ]:


print(dfa['OriginalZip'].unique())
dfa.sort_values('HousingUnits', ascending=False)


# In[ ]:


dfa['TotalNewAddSQFT'].sum()
#Over 1.3 billion square feet; seems low for over a hundred new people per day,
#but a lot of construction is likely unpermitted and many move into Austin metro
#- 4300 square miles and 2 million people, not Austin, 272 square miles and 800K people.


# In[ ]:


plt.figure(figsize=(22,11))
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.title('Austin new square footage')
plt.scatter(dfa['Longitude'],dfa['Latitude'], s=dfa['TotalNewAddSQFT']/1000,c='g')


# In[ ]:


''' This uses the Bokeh package so you will have to make sure it is loaded'''

from bokeh.models import (
   GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
 )
from bokeh.io import output_file, show, output_notebook
from bokeh.io import export_png



# Uncomment out this line to work within the jupyter notebook.
# If left commented out map should show in new window

output_notebook()


# In[3]:


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
size=(dfa['TotalNewAddSQFT'].values**.25)/5


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
export_png(plot, filename="plot.png")


# In[ ]:


import scipy.stats as scs
import statsmodels.api as sm
pd.plotting.scatter_matrix(dfa, figsize=(15, 10))
plt.show()


# In[ ]:


dfa.describe().T

