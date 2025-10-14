# app.py
import uvicorn
from fastapi import FastAPI, Request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
REDIRECT_URI = "https://spotify.homeclean.site/callback"  # nhớ đăng ký trong Spotify Dashboard
SCOPE = "user-read-email user-library-read user-read-playback-state user-modify-playback-state"

app = FastAPI()

auth_manager = SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache-fastapi"   # để lưu token, refresh cho lần sau
)

@app.get("/")
def index():
    # bước 1: redirect user đến trang login Spotify
    auth_url = auth_manager.get_authorize_url()
    return {"login_url": auth_url}

@app.get("/callback")
def callback(request: Request):
    # bước 2: hứng code từ Spotify redirect về
    code = request.query_params.get("code")
    if not code:
        return {"error": "No code provided"}
    
    # bước 3: đổi code sang access token
    token_info = auth_manager.get_access_token(code, as_dict=True)
    return {"token_info": token_info}

@app.get("/me")
def get_profile():
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp.current_user()
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
