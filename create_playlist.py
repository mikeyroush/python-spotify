# log into Youtube
# find liked videos
# scan videos for songs
# create a spotify playlist
# search for the found songs
# add songs to playlist

# important links:
# https://developers.google.com/explorer-help/guides/code_samples#authorization-and-authentication-errors
# https://developers.google.com/youtube/v3/docs
# https://spotipy.readthedocs.io/en/2.12.0/

import json
import requests
import os
import sys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl
import spotipy
import spotipy.util as util

from Secrets import spotify_username, spotify_id, spotify_secret, redirect_uri, youtube_api_key


class CreatePlaylist:
    def __init__(self):
        self.spotify_username = spotify_username
        self.spotify_id = spotify_id
        self.redirect_uri = redirect_uri
        self.spotify_secret = spotify_secret
        self.token = self.get_spotify_token()
        self.credentials = self.get_youtube_credentials()
        self.song_uris = [] 

    def get_youtube_credentials(self):
        # Get credentials and create an API client
        client_secrets_file = "client_secret.json"
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        return(credentials)

    def get_songs(self):
        # build youtube object
        api_service_name = "youtube"
        api_version = "v3"
        youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=self.credentials)

        # build request
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like")
        # send request
        response = request.execute()

	# parse through list
        print("Found videos:")
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = f'https://www.youtube.com/watch?v={item["id"]}'
            #print(f'{video_title}: {youtube_url}')

	    # use youtube_dl to extract info from video
            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url, download=False)
            song_name = video["track"]
            artist = video["artist"]
            #print(f'{song_name}: {artist}')

	    # save all important info if it exists
            try:
                print(self.get_song_id(song_name,artist))
                self.song_uris.append(self.get_song_id(song_name, artist))
            except:
                print("no song data")
        print("analyzed all songs")
        print(self.song_uris)

    def get_spotify_token(self):
        scope = 'playlist-modify-public'
        token = util.prompt_for_user_token(self.spotify_username, 
                scope,
                client_id=self.spotify_id,
                client_secret=self.spotify_secret,
                redirect_uri=self.redirect_uri)
        return token

    def create_playlist(self):
        self.get_songs()
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.user_playlists(self.spotify_username, limit=50, offset=0) 
            for item in results["items"]:
                #print(f'{item["name"]}: {item["id"]}')
                if item["name"] == "Youtube Liked Videos":
                    playlist = item["id"]
                    sp.user_playlist_unfollow(spotify_username, playlist)
                    break
            playlist = sp.user_playlist_create(self.spotify_username,"Youtube Liked Videos",public=True,description="All of songs from my liked YouTube videos")
            print("created playlist")
            sp.trace = False
            try:
                results = sp.user_playlist_add_tracks(self.spotify_username, playlist, self.song_uris)
                print(results)
            except:
                print("error: couldn't add songs")
        else:
            print("Can't get token for", self.spotify_username)

    def get_song_id(self, track, artist):
        results = ""
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            query = f'{track} {artist}'
            results = sp.track(q = query,
                    limit = 10,
                    offset = 0,
                    type = "track",
                    market = "US")
        print("results: " + results["tracks"]["items"][0]["id"])
        return results["tracks"]["items"][0]["id"]

playlist = CreatePlaylist()
playlist.create_playlist()
#playlist.get_songs()
