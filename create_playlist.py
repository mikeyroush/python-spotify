# log into Youtube
# find liked videos
# scan videos for songs
# create a spotify playlist
# search for the found songs
# add songs to playlist

import json, requests
from Secrets import spotify_id, spotify_secret

class CreatePlaylist:
	
	def __init__(self):
		self.user_id = spotify_id
		self.token = spotify_secret
		
	def get_youtube_login(self):
		pass
		
	def get_liked_videos(self):
		pass
		
	def scan_videos(self):
		pass
		
	def create_playlist(self):
		request_body = {
			"name": "Liked YouTube Videos",
			"description": "All songs from my liked YouTube videos",
			"public": True
		}
		
		endpoint = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'
		response = requests.post(
			endpoint,
			data=request_body,
			headers={
				"Content-Type":"application/json",
				f'Authorization":"Bearer {self.token}'
			}
		)
		response_json = response.json()
		
		#save playlist id
		return response_json["id"]
		
	def find_song(self, track, artist):
		endpoint = f'https://api.spotify.com/v1/search?q={track}%20{artist}&type=track&market=US&limit=20'
		response = requests.get(
			endpoint,
			headers={
				"Content-Type":"application/json",
				f'Authorization":"Bearer {self.token}'
			}
		)
		response_json = response.json()
		song = response_json["tracks"]["items"][0]["uri"]
		
		#return the first song
		return song
		
	def add_song(self):
		pass
