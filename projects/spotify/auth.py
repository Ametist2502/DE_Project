import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def auth_with_credentials(client_id: str, client_secret: str) -> spotipy.Spotify:
    try:
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp
    except Exception as e:
        logging.error(f"Error: {e}")

def auth_with_code_flow(scope: str):
    try:
        auth_manager = SpotifyOAuth(scope=scope)
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return sp   # ✅ phải return object Spotify, không return auth_manager
    except Exception as e:
        logging.error(f"Error: {e}")