
import pandas as pd 
import streamlit as st
import plotly.express as px  

vehicles = pd.read_csv('../vehicles_us.csv')

# Create one st. header with text
st.title("Vehicles App with Pandas and Plotly")

# Create at least one Plotly Express histogram using st.write or st.plotly_chart
histogram = px.histogram(vehicles, x='price', title='Vehicle Price Distribution')
st.write("Vehicle Price Distribution")
st.plotly_chart(histogram)






