# music/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .spotify_service import get_playlist_tracks, get_spotify_access_token

def index(request):
    return render(request, 'index.html')

def playlist(request):
    playlist_id = '7aYH3mMVYM0zZsgxpB3ifJ'  # Your playlist ID
    try:
        access_token = get_spotify_access_token()  # Ensure this function is defined in spotify_service.py
        if not access_token:
            return JsonResponse({'error': 'Failed to get access token'}, status=500)
        
        tracks = get_playlist_tracks(access_token, playlist_id)
        return JsonResponse({'songs': tracks})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
