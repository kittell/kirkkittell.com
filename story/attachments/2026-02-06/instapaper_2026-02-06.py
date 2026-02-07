import json
from pathlib import Path
from requests_oauthlib import OAuth1Session

def load_keys():
    # Retrieve API keys from a separate location from code

    # Cross-platform home directory
    home = Path.home()

    # Shared subpath on both Mac and PC
    keyfile = home / 'OneDrive' / 'Programs' / 'instapaper' / 'instapaper_api_keys.json'

    with open(keyfile, 'r') as f:
        return json.load(f)

def get_oauth_token(keys):
    # Step 1: Get an OAuth access token via xAuth
    oauth = OAuth1Session(keys['consumer_id'], client_secret=keys['consumer_secret'])

    response = oauth.post(
        'https://www.instapaper.com/api/1/oauth/access_token',
        data={
            'x_auth_username': keys['username'],
            'x_auth_password': keys['password'],
            'x_auth_mode': 'client_auth',
        }
    )

    if response.status_code != 200:
        raise Exception('xAuth failed: ' + response.text)

    # Parse token + secret
    token_data = dict(item.split('=') for item in response.text.split('&'))

    print('Authenticated!')
    return token_data

def get_auth(api_keys, oauth_token):
    auth = OAuth1Session(
        api_keys['consumer_id'],
        client_secret=api_keys['consumer_secret'],
        resource_owner_key=oauth_token['oauth_token'],
        resource_owner_secret=oauth_token['oauth_token_secret']
    )
    return auth

def fetch_bookmarks(api_keys, oauth_token, limit, folder_id=None):
    auth = get_auth(api_keys, oauth_token)
    resp = auth.post(
        'https://www.instapaper.com/api/1/bookmarks/list',
        data={
            'folder_id': folder_id,
            'limit': limit
            }
    )

    resp_json = resp.json()
    bookmarks = []
    for item in resp_json:
        if item.get('type') == 'bookmark':
            bookmarks.append(item)

    return bookmarks

if __name__ == '__main__':
    api_keys = load_keys()
    oauth_token = get_oauth_token(api_keys)
    bookmarks = fetch_bookmarks(api_keys, oauth_token, limit=10, folder_id='archive')
    print(bookmarks)
    for b in bookmarks:
        print(f"{b['bookmark_id']}, {b['url']}, {b['title']}, {b['time']}")