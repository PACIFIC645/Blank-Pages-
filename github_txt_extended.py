# github_txt_extended

class Artist:
    def __init__(self, name, project_name, release_month, streams):
        self.name = name
        self.project_name = project_name
        self.release_month = release_month
        self.streams = streams

    def print_streaming_stats(self):
        print(f"Streaming stats for {self.name}:")
        # Ensure all expected platforms are present in the streams dictionary
        expected_platforms = ['Spotify', 'SoundCloud', 'Audiomack']
        for platform in expected_platforms:
            streams = self.streams.get(platform)
            if streams is not None:
                print(f"- {platform}: {streams} streams")
            else:
                print(f"- {platform}: Data not available")

class ArtistManager:
    def __init__(self):
        self.artist_data = {}

    def add_new_artist_data(self, name, project_name, release_month, streams):
        if name in self.artist_data:
            print("Artist already exists. Consider updating the existing entry.")
            return False
        new_artist = Artist(name, project_name, release_month, streams)
        self.artist_data[name] = new_artist
        return True

    def print_monthly_releases(self, month):
        print(f"Artists releasing projects in {month}:")
        for artist in self.artist_data.values():
            if artist.release_month == month:
                print(f"- {artist.name}: {artist.project_name}")

    def print_streaming_stats_for_artist(self, artist_name):
        artist = self.artist_data.get(artist_name)
        if artist:
            artist.print_streaming_stats()
        else:
            print("Artist not found.")

# Demonstrate usage of the ArtistManager class
artist_manager = ArtistManager()
artist_manager.add_new_artist_data(
    'Nasty C', 'Zulu Man With Some Power', 'August', 
    {'Spotify': 5000000, 'SoundCloud': 1200000}
)
artist_manager.add_new_artist_data(
    'Cassper Nyovest', 'Any Minute Now', 'September', 
    {'Spotify': 3000000, 'Audiomack': 1500000}
)
artist_manager.print_monthly_releases('August')
artist_manager.print_streaming_stats_for_artist('Nasty C')


