import spotipy
from secrets import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAccess:
    "Spotify API abstraction"

    def __init__(self, username, scope):
        self.name = username
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.redirect_uri = REDIRECT_URI
        self.scope = scope
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope=scope,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
            )
        )

    def top_songs(self, time_range, n=10):
        songs = self.spotify.current_user_top_tracks(
            limit=n,
            time_range=time_range,
        )

        print(f"\n\n\n              {n} top {time_range} songs for {self.name}")

        for i in range(n):
            try:
                print("\n")
                song = songs["items"][i - 1]
                print(
                    f"{i+ 1}:",
                    song["name"],
                    f"-- {round(song['duration_ms'] / 3600)} minutes listened",
                )
            except IndexError:
                print(f"Less than {n} topsongs; occured at number {i}")
                break

    def top_artists(self, time_range, n=10):
        artists = self.spotify.current_user_top_artists(
            limit=n,
            time_range=time_range,
        )

        print(f"\n\n\n              {n} top {time_range} artists for {self.name}")

        for i in range(n):
            try:
                print("\n")
                artist = artists["items"][i - 1]
                print(
                    f"{i + 1}:",
                    artist["name"],
                    f"-- Genre: {artist['genre']}",
                )
            except IndexError:
                print(f"Less than {n} topsongs; occured at number {i}")
                break
