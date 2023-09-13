"""
A siple streamlit app fetching world bank data

@author: George Delis
@date: 11/08/2023

"""

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# import custom functions
from functions.wb_lib import fetch_world_bank_data, process_data

# Title and header
st.title ("World Bank Data Explorer")
st.header("Make selections to see the equivalent data")

# User input for country code
country_code = st.selectbox('Pick your country',['US','GB', 'GR', 'FR'])
# User input for indicator
indicator = st.selectbox('Pick your indicator',['MS.MIL.XPND.CD','MS.MIL.XPND.GD.ZS', 'MS.MIL.XPND.ZS'])
# User input for start and end year
start_year = st.text_input("Enter the start year (e.g., '2018'):")
end_year = st.text_input("Enter the end year (e.g., '2020'):")


if st.button('Fetch Data'):
    raw_data = fetch_world_bank_data(country_code, indicator, start_year, end_year)

    # Check if the response has expected data
    if len(raw_data) < 2:
        st.write("Error fetching data. Response from World Bank API:", raw_data)
    else:
        processed_data = process_data(raw_data[1])
        st.write(processed_data)
        sns.lineplot(data=processed_data, x='date', y='value')
        st.pyplot(plt)
