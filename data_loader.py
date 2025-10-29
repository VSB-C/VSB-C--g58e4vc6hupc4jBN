# data_loader.py - SIMPELSTE WERKENDE OPLOSSING
import pandas as pd
import streamlit as st

# Verander dit nummer ALLEEN wanneer je data update
DATA_VERSION = 1

@st.cache_data(ttl=1209600, show_spinner="Data wordt geladen...")
def load_all_player_data(_version=DATA_VERSION):
    """
    Simpel, betrouwbaar, controle in jouw handen
    """
    df = pd.read_parquet("df.parquet", engine='pyarrow')
    
    categorical_cols = ['season', 'squadName', 'playerName', 'position', 'competitionName']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
    
    return df