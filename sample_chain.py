#Step 1: Choose a song on Spotify
#Step 2: Search for this song on WhoSampled
#Step 3: Grab sample data: tracks that the song sampled and tracks that sample the song
#Step 4: Create a playlist in Spotify
#Step 5: Add the sample chain to the playlist in chrono order

#import spotipy
import os
#import json
#import requests
#from spotipy.oauth2 import SpotifyClientCredentials
#from spotipy import util
#from spotipy.util import prompt_for_user_token


class CreateSampleChainPlaylist:
    def __init__(self, song):
        self.song=song
        
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

    #Step 5: Add the sample chain to the playlist in chrono order   
    def get_spotify_uri(self, song_name, artist):
        pass

    def add_track_to_playlist(self):
        pass
