import pandas as pd
import streamlit as st
file_path = '/Users/carlvansteenbrugge/Documents/Data/Data Platform Essevee/Impect/Data/Alle seizoenen/df.parquet'

@st.cache_data(show_spinner="Data wordt geladen...")
def load_all_player_data():
    df = pd.read_parquet(file_path)
    return df