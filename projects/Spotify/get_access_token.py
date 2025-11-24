import requests
import base64
import time
import os
from dotenv import load_dotenv

load_dotenv()

# --- CẤU HÌNH ---
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Lấy token này TỪ LẦN ĐĂNG NHẬP THỦ CÔNG ĐẦU TIÊN (Lưu cứng vào đây hoặc biến môi trường)
# Token này KHÔNG BAO GIỜ HẾT HẠN trừ khi người dùng revoke access app
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

def get_access_token_headless():
    """
    Hàm này lấy Access Token mới mà KHÔNG cần mở trình duyệt/UI.
    Nó hoạt động hoàn toàn ở background (headless).
    """
    url = "https://accounts.spotify.com/api/token"
    
    # Mã hóa Authorization Header
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            json_resp = response.json()
            access_token = json_resp['access_token']
            expires_in = json_resp['expires_in'] # Thường là 3600 giây (1 giờ)
            
            print(f"[SUCCESS] Đã lấy được Access Token mới (headless)!")
            print(f"Hết hạn sau: {expires_in} giây")
            
            # Cập nhật Refresh token nếu Spotify trả về cái mới (đôi khi nó đổi)
            if 'refresh_token' in json_resp:
                print("[INFO] Spotify đã cấp Refresh Token mới, hãy cập nhật lại DB/File của bạn.")
                new_refresh_token = json_resp['refresh_token']
                # TODO: Lưu new_refresh_token vào database/file tại đây
            
            return access_token
        else:
            print(f"[ERROR] Không thể lấy token: {response.text}")
            return None
            
    except Exception as e:
        print(f"[EXCEPTION] Lỗi kết nối: {e}")
        return None

# --- VÍ DỤ SỬ DỤNG ---
if __name__ == "__main__":
    # Giả lập một task chạy ngầm
    print("Bắt đầu tác vụ headless...")
    
    token = get_access_token_headless()
    
    if token:
        # Dùng token để gọi API
        api_url = "https://api.spotify.com/v1/me"
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(api_url, headers=headers)
        
        if resp.status_code == 200:
            user_data = resp.json()
            print(f"Đang chạy dưới danh nghĩa user: {user_data.get('display_name')}")
            print(f"Email: {user_data.get('email')}")
        else:
            print("Token không hoạt động.")