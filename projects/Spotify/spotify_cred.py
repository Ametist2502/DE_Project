"""
Yêu cầu cài đặt thư viện:
pip install flask requests
"""

import os
import base64
import random
import string
import urllib.parse
import requests
from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

# --- CẤU HÌNH CỦA BẠN ---
CLIENT_ID = 'project_Build_ETL'
CLIENT_SECRET = 'project_Build_ETL'
REDIRECT_URI = 'https://spotify.homeclean.site/callback'

# Hàm tạo chuỗi ngẫu nhiên cho state
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# --- 1. Endpoint Login ---
@app.route('/login')
def login():
    state = generate_random_string(16)
    scope = 'ugc-image-upload user-read-email user-read-private'
    
    # Tạo URL authorization
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': state
    }
    
    auth_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(params)
    
    # Nếu chạy headless hoàn toàn, bạn có thể muốn in URL ra console để copy
    print(f"\n--- COPY LINK NÀY VÀO TRÌNH DUYỆT ĐỂ LOGIN ---\n{auth_url}\n")
    
    return redirect(auth_url)

# --- 2. Endpoint Callback ---
@app.route('/callback')
def callback():
    # Lấy code và state từ query parameters
    code = request.args.get('code')
    state = request.args.get('state')
    error = request.args.get('error')

    if error:
        return jsonify({'error': error}), 400

    if state is None:
        return jsonify({'error': 'state_mismatch'}), 400
        
    # Chuẩn bị request đổi code lấy token
    token_url = 'https://accounts.spotify.com/api/token'
    
    # Tạo header Authorization Basic base64(client_id:client_secret)
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    # Body của request
    data = {
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    
    try:
        # Gửi POST request đến Spotify
        response = requests.post(token_url, data=data, headers=headers)
        response_data = response.json()
        
        if response.status_code == 200:
            # Trả về kết quả dưới dạng JSON
            return jsonify({
                'message': 'Đăng nhập thành công!',
                'access_token': response_data.get('access_token'),
                'refresh_token': response_data.get('refresh_token'),
                'expires_in': response_data.get('expires_in')
            })
        else:
            return jsonify({'error': 'invalid_token', 'details': response_data}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- 3. Endpoint Refresh Token ---
@app.route('/refresh_token')
def refresh_token():
    refresh_token_val = request.args.get('refresh_token')
    
    token_url = 'https://accounts.spotify.com/api/token'
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token_val
    }
    
    try:
        response = requests.post(token_url, data=data, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Listening on port 8888...")
    # debug=True giúp server tự reload khi sửa code, hữu ích khi dev
    app.run(port=8888, debug=True)