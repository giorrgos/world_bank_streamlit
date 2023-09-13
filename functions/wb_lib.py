# -*- coding: utf-8 -*-
"""
Created: 06/08/2023 
author: @George Delis
This is a file containing functions
"""

#-------------------- IMPORTS --------------
import requests
import pandas as pd

#------------------- FUNCTIONS ---------------

def fetch_world_bank_data(country_code, indicator, start_year, end_year):
    base_url = f"http://api.worldbank.org/v2/country/{country_code}/indicator"
    url = f"{base_url}/{indicator}?date={start_year}:{end_year}&format=json"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch data from the World Bank API")

    data = response.json()
    return data

def process_data(data):
    df = pd.DataFrame(data)
    
    # Extracting the 'name' key from the 'country' and 'indicator' columns
    df['country'] = df['country'].apply(lambda x: x['value'] if isinstance(x, dict) else x)
    df['indicator'] = df['indicator'].apply(lambda x: x['value'] if isinstance(x, dict) else x)
    
    # Format the value column
    #df["value"] = df["value"].apply(lambda x: '{:,.0f}'.format(x) if pd.notnull(x) else x)
    
    # Sort the dataframe
    df.sort_values(by='date', ascending=False)

    return df[["country", "date", "indicator", "value"]]

