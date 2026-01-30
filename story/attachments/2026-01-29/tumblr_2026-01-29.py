import requests
import json
import html
from pathlib import Path
from bs4 import BeautifulSoup

API_KEY = "YOUR_API_KEY"  # register at https://www.tumblr.com/oauth/apps
BLOG_IDENTIFIER = "kittell.tumblr.com"
LIMIT = 10

def load_tumblr_keys():
    # Cross‑platform home directory
    home = Path.home()

    # Shared subpath on both Mac and PC
    keyfile = home / "OneDrive" / "Programs" / "tumblr" / "tumblr_api_keys.json"

    with open(keyfile, "r") as f:
        return json.load(f)

def get_posts(keys):
    url = f"https://api.tumblr.com/v2/blog/{BLOG_IDENTIFIER}/posts/link"
    params = {
        "api_key": keys['consumer_key'],
        "limit": LIMIT
    }

    response = requests.get(url, params=params)
    data = response.json()

    posts = data["response"]["posts"]

    return posts

def get_npfdata_from_body(body):
    soup = BeautifulSoup(body, 'html.parser')

    # Step 1: extract the attribute
    raw = soup.p["data-npf"]

    # Step 2: unescape HTML entities (&quot; → ")
    unescaped = html.unescape(raw)

    # Step 3: parse JSON
    npf_data = json.loads(unescaped)

    return npf_data

if __name__ == "__main__":
    keys = load_tumblr_keys()
    posts = get_posts(keys)
    for post in posts:
        npf_data = get_npfdata_from_body(post['body'])
        print(npf_data['url'])
