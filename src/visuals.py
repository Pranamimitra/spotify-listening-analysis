# Existing imports...

def plot_playlist_summary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(y=df['playlist_name'], x=df['track_count'], palette='viridis')
    plt.title('Tracks per Playlist')
    plt.xlabel('Number of Tracks')
    plt.ylabel('Playlist Name')
    plt.savefig("outputs/playlist_summary.png", bbox_inches='tight', dpi=300)
    plt.show()

def plot_search_queries(df, top_n=10):
    top_searches = df['search_query'].value_counts().head(top_n).reset_index()
    top_searches.columns = ['search_query', 'count']
    
    plt.figure(figsize=(8,5))
    sns.barplot(y="search_query", x="count", palette="magma", data=top_searches)
    plt.title(f"Top {top_n} Search Queries")
    plt.xlabel("Count")
    plt.ylabel("Search Term")
    plt.savefig("outputs/top_search_queries.png", bbox_inches='tight', dpi=300)
    plt.show()

def plot_search_hourly_pattern(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df['search_hour'], bins=24, kde=False, color='green')
    plt.title('Searches by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Searches')
    plt.savefig("outputs/search_hourly_pattern.png", bbox_inches='tight', dpi=300)
    plt.show()
