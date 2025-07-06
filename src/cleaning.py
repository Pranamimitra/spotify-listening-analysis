import pandas as pd

def clean_streaming_data(df):
    df.rename(columns={'artistName': 'artist_name', 'trackName': 'track_name', 'endTime': 'played_at'}, inplace=True)
    df['played_at'] = pd.to_datetime(df['played_at'])
    df['date'] = df['played_at'].dt.date
    df['hour'] = df['played_at'].dt.hour
    df['day_name'] = df['played_at'].dt.day_name()
    return df

def clean_playlist_data(df):
    df.rename(columns={
        'name': 'playlist_name',
        'description': 'playlist_description',
        'numberOfFollowers': 'followers',
        'items': 'track_count'
    }, inplace=True)
    return df

def clean_search_data(df):
    df.rename(columns={'searchTime': 'search_time', 'searchQuery': 'search_query'}, inplace=True)
    df['search_time'] = df['search_time'].str.replace(r'\[UTC\]', '', regex=True)
    df['search_time'] = pd.to_datetime(df['search_time'], utc=True, format='mixed')
    df['search_date'] = df['search_time'].dt.date
    df['search_hour'] = df['search_time'].dt.hour
    df['search_day'] = df['search_time'].dt.day_name()
    return df
