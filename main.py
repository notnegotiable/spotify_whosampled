#Step 1: Choose a song on Spotify
#Step 2: Search for this song on WhoSampled
#Step 3: Grab sample data: tracks that the song sampled and tracks that sample the song
#Step 4: Create a playlist in Spotify
#Step 5: Add the sample chain to the playlist in chrono order

import spotipy
import json
import requests
from secrets import spotify_user_id

class CreateSampleChainPlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    #Step 1: Choose a song on Spotify
    def get_track(self):
        pass

    #Step 2: Search for this song on WhoSampled
    def search_whosampled(self):
        pass

    #Step 3: Grab sample data: tracks that the song sampled and tracks that sample the song
    def grab_sample_data(self):
        pass

    #Step 4: Create a playlist in Spotify
    def create_playlist(self):
        pass
        )

    #Step 5: Add the sample chain to the playlist in chrono order   
    def get_spotify_uri(self, song_name, artist):
        pass

    def add_track_to_playlist(self):
        pass


