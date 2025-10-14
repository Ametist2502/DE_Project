from auth import auth_with_credentials, auth_with_code_flow
from dotenv import load_dotenv
import os

# load_dotenv()
# SPOTIFY_ID=os.getenv('SPOTIFY_ID')
# SPOTIFY_SECRET=os.getenv('SPOTIFY_SECRET')
# redirect_uri = 'https://spotify.homeclean.site/callback'
# scope="user-library-read"
# sp = auth_with_credentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET)


# sp = auth_with_code_flow(scope=scope)# Lấy thông tin user đang login
# me = sp.current_user()
# print(me)

# # Lấy danh sách playlist của user
# playlists = sp.current_user_playlists(limit=10)
# for playlist in playlists['items']:
#     print(playlist['name'], playlist['id'])

# # Lấy top tracks của user
# top_tracks = sp.current_user_top_tracks(limit=5, time_range="short_term")
# for idx, track in enumerate(top_tracks['items']):
#     print(f"{idx+1}. {track['name']} - {track['artists'][0]['name']}")

# Lấy danh sách bài hát trong playlist
print(sp.audio_analysis(track_id='5J90ah0ppUSev1uahqQiN6'))