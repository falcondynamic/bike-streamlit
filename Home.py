import streamlit as st
import pandas as pd
import requests

st.header("My Bike Price Prediction App")

length_fork_mm = st.sidebar.slider("Length of Fork mm", min_value=30, max_value=200, value=30, step=1)
battery_wh = st.sidebar.slider("Battery Wh", min_value=0, max_value=1000, value=0, step=1)
frame_material = st.sidebar.selectbox("Frame Material", ('Aluminium', 'Carbon', 'Aluminium-Carbon', 'Diamant', 'Aluminium-Stahl'))
number_of_gears = st.sidebar.slider("Number of Gears", min_value=1, max_value=30, value=1, step=1)
category = st.sidebar.selectbox("Category", ('Trekking', 'City', 'MTB_Hardtail', 'MTB_Fully'))
manufacturer = st.sidebar.selectbox("Manufacturer", (  'Kalkhoff', 'CUBE',
                                                                                'Haibike',
                                                                                'Hercules',
                                                                                'Winora',
                                                                                'SCOTT',
                                                                                'corratec',
                                                                                'Diamant',
                                                                                'GHOST',
                                                                                'Specialized',
                                                                                'Cannondale',
                                                                                'Canyon'))


my_params = {
    "length_fork_mm": length_fork_mm,
    "battery_wh": battery_wh,
    "frame_material": frame_material,
    "number_of_gears": number_of_gears,
    "category": category,
    "manufacturer": manufacturer
}

df = pd.DataFrame.from_dict([my_params])


st.header("The configuration of your e-bike is below!")
st.table(df)

st.subheader("Press predict if configuration is okay!!!")

if st.button("Predict"):
    response = requests.get(f"https://bike-api-kmqz.onrender.com/prediction/{length_fork_mm}/{battery_wh}/{frame_material}/{number_of_gears}/{category}/{manufacturer}").json()
    st.success(f"The price of your e-bike is {response["unit"]}{response['prediction']}")