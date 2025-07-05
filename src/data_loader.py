import pandas as pd

def load_streaming_history(filepath):
    return pd.read_json(filepath)

def load_playlist_data(filepath):
    return pd.read_json(filepath)

def load_search_data(filepath):
    return pd.read_json(filepath)
