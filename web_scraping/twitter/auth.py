import os
import secret.auth_token as at

bearer_token = os.environ.get('BEARER_TOKEN')

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {at.AUTH_TOKEN}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r