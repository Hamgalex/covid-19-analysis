import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


country_wise_latest = pd.read_csv("dataset/country_wise_latest.csv",encoding='utf-8')

st.dataframe(country_wise_latest)