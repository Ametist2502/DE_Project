from auth import auth_with_credentials
from dotenv import load_dotenv
import os

load_dotenv()
SPOTIFY_ID=os.getenv('SPOTIFY_ID')
SPOTIFY_SECRET=os.getenv('SPOTIFY_SECRET')

sp = auth_with_credentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(f"{i + 1 + playlists['offset']:4d} {playlist['uri']} {playlist['name']}")
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None