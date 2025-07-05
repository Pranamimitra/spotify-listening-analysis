import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style="whitegrid")

# Top Artists
def plot_top_artists(df, top_n=5):
    top_artists = df['artist_name'].value_counts().head(top_n).reset_index()
    top_artists.columns = ['artist_name', 'play_count']

    plt.figure(figsize=(8,5))
    sns.barplot(y="artist_name", x="play_count", hue="artist_name", palette="viridis", data=top_artists, legend=False)
    plt.title(f"Top {top_n} Most Played Artists")
    plt.show()

# Top Tracks
def plot_top_tracks(df, top_n=5):
    top_tracks = df['track_name'].value_counts().head(top_n).reset_index()
    top_tracks.columns = ['track_name', 'play_count']

    plt.figure(figsize=(8,5))
    sns.barplot(y="track_name", x="play_count", hue="track_name", palette="magma", data=top_tracks, legend=False)
    plt.title(f"Top {top_n} Most Played Tracks")
    plt.show()

# Listening Heatmap
def plot_listening_heatmap(df):
    heatmap_data = df.groupby(['day_name', 'hour']).size().unstack().fillna(0)
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(day_order)

    plt.figure(figsize=(12,6))
    sns.heatmap(heatmap_data, cmap="YlGnBu")
    plt.title("Listening Heatmap (Hour vs Day)")
    plt.show()

# Artist WordCloud
def plot_artist_wordcloud(df):
    text = " ".join(df['artist_name'])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Artist WordCloud")
    plt.show()

# Playlist Summary
def plot_playlist_summary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(y=df['playlist_name'], x=df['total_tracks'], hue=df['playlist_name'], palette="viridis", legend=False)
    plt.title("Total Tracks per Playlist")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.barplot(y=df['playlist_name'], x=df['total_artists'], hue=df['playlist_name'], palette="cividis", legend=False)
    plt.title("Unique Artists per Playlist")
    plt.show()

# Search Queries
def plot_search_queries(df):
    search_counts = df['search_query'].value_counts().reset_index()
    search_counts.columns = ['search_query', 'count']

    plt.figure(figsize=(8,5))
    sns.barplot(y="search_query", x="count", hue="search_query", palette="crest", data=search_counts, legend=False)
    plt.title("Most Searched Terms")
    plt.show()

# Search Trend Over Time
def search_trend_over_time(df):
    df['search_date'] = pd.to_datetime(df['search_date'])
    daily_counts = df.groupby(df['search_date'].dt.date).size().reset_index()
    daily_counts.columns = ['date', 'search_count']

    plt.figure(figsize=(10,5))
    sns.lineplot(x='date', y='search_count', data=daily_counts)
    plt.title("Search Activity Over Time")
    plt.show()
