# git_txt_extended

# Define the Artist class to represent individual artist data
class Artist:
    # Initialize an Artist object with name, project details, and streaming stats
    def __init__(self, name, project_name, release_month, streams):
        self.name = name  # Artist's name
        self.project_name = project_name  # Name of the artist's project or album
        self.release_month = release_month  # Month the project was released
        self.streams = streams  # Dictionary containing streaming platform data

    # Method to print the streaming statistics for the artist
    def print_streaming_stats(self):
        print(f"Streaming stats for {self.name}:")
        for platform, streams in self.streams.items():
            # Loop through each platform in the streams dictionary and print the number of streams
            print(f"- {platform}: {streams} streams")

# Define the ArtistManager class to manage a collection of Artist objects
class ArtistManager:
    # Initialize the ArtistManager with an empty dictionary to store artist data
    def __init__(self):
        self.artist_data = {}

    # Method to add new artist data to the artist_data dictionary
    def add_new_artist_data(self, name, project_name, release_month, streams):
        if name in self.artist_data:
            # Check if the artist already exists and return False if so
            print("Artist already exists. Consider updating the existing entry.")
            return False

        # If the artist doesn't exist, create a new Artist object and add it to the dictionary
        new_artist = Artist(name, project_name, release_month, streams)
        self.artist_data[name] = new_artist
        return True  # Return True to indicate the artist was successfully added

    # Method to print the releases for a specific month
    def print_monthly_releases(self, month):
        print(f"Artists releasing projects in {month}:")
        for artist in self.artist_data.values():
            # Iterate through the artists and print those releasing projects in the specified month
            if artist.release_month == month:
                print(f"- {artist.name}: {artist.project_name}")

    # Method to print streaming statistics for a specific artist
    def print_streaming_stats_for_artist(self, artist_name):
        if artist_name in self.artist_data:
            # If the artist exists, print their streaming stats
            self.artist_data[artist_name].print_streaming_stats()
        else:
            # If the artist doesn't exist, print an error message
            print("Artist not found.")

# Demonstrate usage of the ArtistManager class
artist_manager = ArtistManager()

# Add data for two artists
artist_manager.add_new_artist_data(
    'Nasty C', 'Zulu Man With Some Power', 'August', 
    {'Spotify': 5000000, 'SoundCloud': 1200000, 'Audiomack': 2500000}
)

artist_manager.add_new_artist_data(
    'Cassper Nyovest', 'Any Minute Now', 'September', 
    {'Spotify': 3000000, 'SoundCloud': 500000, 'Audiomack': 1500000}
)

# Print releases for August and streaming stats for Nasty C
artist_manager.print_monthly_releases('August')
artist_manager.print_streaming_stats_for_artist('Nasty C')


