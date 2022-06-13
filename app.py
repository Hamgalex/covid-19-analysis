import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap

country_wise_latest = pd.read_csv("dataset/country_wise_latest.csv",encoding='utf-8')
covid_19_clean_complete = pd.read_csv("dataset/covid_19_clean_complete.csv",encoding='utf-8')
day_wise = pd.read_csv("dataset/day_wise.csv",encoding='utf-8')
usa_county_wise = pd.read_csv("dataset/usa_county_wise.csv",encoding='utf-8')
worldometer_data = pd.read_csv("dataset/worldometer_data.csv",encoding='utf-8')

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
width=8E6, height=8E6,
lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)
# Map (long, lat) to (x, y) for plotting
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12)

st.pyplot(fig)

