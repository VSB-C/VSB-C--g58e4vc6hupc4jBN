import pandas as pd
import streamlit as st

@st.cache_data(show_spinner="Data wordt geladen...")
def load_all_player_data():
    # GEBRUIK RELATIEF PAD - bestand staat inzelfde repository
    df = pd.read_parquet("df.parquet")
    return df