# git_txt_extended

# Define a dictionary to store artist data
artist_data = {
    'Nasty C': {
        'project_name': 'Zulu Man With Some Power',
        'release_month': 'August',
        'streams': {
            'Spotify': 5000000,
            'SoundCloud': 1200000,
            'Audiomack': 2500000
        }
    },
    'Cassper Nyovest': {
        'project_name': 'Any Minute Now',
        'release_month': 'September',
        'streams': {
            'Spotify': 3000000,
            'SoundCloud': 500000,
            'Audiomack': 1500000
        }
    },
    # Add more artists here, consider the upcomers too...
}

# Function to print monthly release stats
def print_monthly_releases(data, month):
    print(f"Artists releasing projects in {month}:")
    for artist in data:
        if data[artist]['release_month'] == month:
            print(f"- {artist}: {data[artist]['project_name']}")

# Function to print streaming stats
def print_streaming_stats(data, artist_name):
    if artist_name in data:
        print(f"Streaming stats for {artist_name}:")
        for platform, streams in data[artist_name]['streams'].items():
            print(f"- {platform}: {streams} streams")
    else:
        print("Artist not found.")

# Example usage
print_monthly_releases(artist_data, 'August')
print_streaming_stats(artist_data, 'Nasty C')
# print_monthly_releases(artist_data, 'September')
# print_streaming_stats(artist_data, 'Cassper Nyovest')

print("Hello, GitHub!")