'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")

tix = pd.read_csv('/Users/jack/Downloads/IST 356/assignment-08-JackVsyr/cache/tickets_in_top_locations.csv')
st.title('Top Locations for Parking Tickets in Syracuse')
st.caption('This dashboard shows the tickets that were issued in the top locations with $1,000 or more in total violation amounts.')

locations = tix['location'].unique()
loc = st.selectbox('Select a location:', locations)
if loc:
    Fdf = tix[tix['location'] == loc]
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total tickets issued", Fdf.shape[0])
        fig1, ax1 = plt.subplots()
        ax1.set_title('Tickets by Hour of Day')
        sns.barplot(data=Fdf, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.metric("Total amount", f"$ {Fdf['amount'].sum()}")
        fig2, ax2 = plt.subplots()
        ax2.set_title('Tickets by Day of Week')
        sns.barplot(data=Fdf, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax2)
        st.pyplot(fig2)

    st.map(Fdf[['lat', 'lon']])