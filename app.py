import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import chain

country_wise_latest = pd.read_csv("dataset/country_wise_latest.csv",encoding='utf-8')
covid_19_clean_complete = pd.read_csv("dataset/covid_19_clean_complete.csv",encoding='utf-8')
day_wise = pd.read_csv("dataset/day_wise.csv",encoding='utf-8')
usa_county_wise = pd.read_csv("dataset/usa_county_wise.csv",encoding='utf-8')
worldometer_data = pd.read_csv("dataset/worldometer_data.csv",encoding='utf-8')


def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)
    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))
    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
llcrnrlat=-90, urcrnrlat=90,
llcrnrlon=-180, urcrnrlon=180, )
draw_map(m)





st.pyplot(fig)

