#!/usr/bin/env python
# coding: utf-8

# ## Observation from the Open City Nature Challange 
# 
# RQ1 
# Can we identify macroscopic laws of citizen science projects so that long term dynamics is different? 
# 
# RQ2 
# How communities are growing in time, what drives their growth if not preferential attachment or exogeneous factors?
# 
# ## Data 
# Muki downloaded all the CNC observations for the bounding box of Europe (metadata below) that includes the geographical locations - it's 62K observations.
# 
# Query quality_grade=any&identifications=any&swlat=35.327868&swlng=-15.438348&nelat=61.352386&nelng=32.898351&projects[]=city-nature-challenge-2019
# Columns id, observed_on_string, observed_on, time_observed_at, time_zone, out_of_range, user_id, user_login, created_at, updated_at, quality_grade, license, url, image_url, sound_url, tag_list, description, id_please, num_identification_agreements, num_identification_disagreements, captive_cultivated, oauth_application_id, place_guess, latitude, longitude, positional_accuracy, geoprivacy, taxon_geoprivacy, coordinates_obscured, positioning_method, positioning_device, species_guess, scientific_name, common_name, iconic_taxon_name, taxon_id, taxon_kingdom_name, taxon_phylum_name, taxon_subphylum_name, taxon_superclass_name, taxon_class_name, taxon_subclass_name, taxon_superorder_name, taxon_order_name, taxon_suborder_name, taxon_superfamily_name, taxon_family_name, taxon_subfamily_name, taxon_supertribe_name, taxon_tribe_name, taxon_subtribe_name, taxon_genus_name, taxon_genushybrid_name, taxon_species_name, taxon_hybrid_name, taxon_subspecies_name, taxon_variety_name, taxon_form_name

# In[1]:



import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import csv


# load data on trajectories, it is very heavy 

df_cit_sci = pd.read_csv('C:/Users/lyubo/Documents/DATA_networks/data_citizen_science/observations-65163_space.csv')

print(df_cit_sci.shape)


# In[2]:


df_cit_sci.head(20)


# In[2]:



print(df_cit_sci.columns)


# ### Plot participants and findings on a map
# 
# From 62246 unique records of users we plot their distribution on a map.

# In[9]:



import math
import matplotlib.pyplot as plt

import seaborn
from mpl_toolkits.basemap import Basemap

# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
# Create a map on which to draw. 
# Use mercator projection, and showing the whole world.

fig, ax = plt.subplots(figsize=(60, 60))

# Berlin Latitude: 52.520008, longitude: 13.404954.
# NYC  40.730610, and the longitude is -73.935242.
# We want to plot only Berlin surrounding areas
m = Basemap(projection='merc',llcrnrlat=49,urcrnrlat=59,llcrnrlon=-8.5,urcrnrlon=3,lat_ts=20,resolution='c')
# Draw coastlines, and the edges of the map. NASA bluemarble
m.shadedrelief() #m.bluemarble()
m.drawcoastlines()
m.drawmapboundary()

# Convert latitude and longitude to x and y coordinates
#TODO: verify if x and y correspond well to lon, lat
x, y = m(list(df_cit_sci["longitude"].astype(float)), list(df_cit_sci["latitude"].astype(float)))

#print(type(x))

# Use matplotlib to draw the points onto the map.
m.scatter(x,y,1,marker='o',color='red')
# Show the plot.
plt.show()


# In[ ]:


# work in progress on 
# visualisation of the spatial patterns over time
# analysis of communities formations and population of the platform over time

