import streamlit as st
import pandas as pd

st.title('Smart DC Power Supply Dashboard')

file_path = 'data/sensor_data.csv'

df = pd.read_csv(file_path)

st.subheader('Latest Sensor Readings')

latest = df.iloc[-1]

st.metric('Voltage (V)', latest['Voltage'])
st.metric('Current (A)', latest['Current'])
st.metric('Temperature (°C)', latest['Temperature'])
st.metric('Power (W)', latest['Power'])
st.metric('Efficiency (%)', latest['Efficiency'])

st.subheader('Voltage Graph')
st.line_chart(df['Voltage'])

st.subheader('Current Graph')
st.line_chart(df['Current'])

st.subheader('Temperature Graph')
st.line_chart(df['Temperature'])

st.subheader('Power Graph')
st.line_chart(df['Power'])

st.subheader('Efficiency Graph')
st.line_chart(df['Efficiency'])

if latest['Temperature'] > 50:
    st.error('Warning: High Temperature Detected!')

if latest['Voltage'] < 10:
    st.warning('Warning: Voltage Drop Detected!')