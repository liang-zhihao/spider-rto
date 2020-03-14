import requests

def get_safe_session():
    s = requests.session()
    s.keep_alive = False
    s.adapters.DEFAULT_RETRIES = 5
    return s
def get_headers():
    headers = {
        # 传入你的cookies
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
                      ,'Connection': 'close'
        }
    return headers