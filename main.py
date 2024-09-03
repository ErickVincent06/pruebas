import spotipy
from spotipy.oauth2 import SpotifyAuthBase
import os

CLIENT_ID = os.environ.get('SP_ID_APP')
CLIENT_SECRET = os.environ.get('SP_PSW')
REDIRECT_URI = 'http://localhost:8000/callback'
