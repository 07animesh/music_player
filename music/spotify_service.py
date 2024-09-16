# music/spotify_service.py
import base64
import requests
from django.conf import settings

def get_spotify_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = {
        'Authorization': 'Basic ' + base64.b64encode(f"{settings.SPOTIFY_CLIENT_ID}:{settings.SPOTIFY_CLIENT_SECRET}".encode()).decode()
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    
    response = requests.post(auth_url, headers=auth_header, data=auth_data)
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get('access_token')
    else:
        raise Exception(f"Failed to get access token: {response.status_code} - {response.text}")

def get_playlist_tracks(access_token, playlist_id):
    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(playlist_url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        tracks = []
        for item in response_data['items']:
            track = item['track']
            tracks.append({
                'title': track['name'],
                'artist': ', '.join(artist['name'] for artist in track['artists']),
                'url': track['external_urls']['spotify'],
                'preview_url': track.get('preview_url')  # Optional preview URL
            })
        return tracks
    else:
        raise Exception(f"Failed to get playlist tracks: {response.status_code} - {response.text}")
