import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()

TOKEN = os.getenv("ENSEMBLE_TOKEN") or os.environ.get("ENSEMBLE_TOKEN")
POSTS_URL = os.getenv("ENSEMBLE_POSTS_URL") or os.environ.get("ENSEMBLE_POSTS_URL")

def get_test_data():
    with open("/home/kamol/projects/cofilmai-challenge/hashtags.json") as f:
        return json.load(f)

def get_tranding_posts(hashtag, params):
    trending_posts = []

    headers = {
        'accept': 'application/json',
    }

    response = requests.get(POSTS_URL, params=params, headers=headers)

    # data = response.json() if response.status_code == 200 else []

    data = get_test_data()["data"]
    if not data:
        return None
    
    # next_cursor = data.get("nextCursor") NOTE: Use recursion if all data should be extracted.
    response_data = data.get("data")

    if not response_data:
        return None
    
    for datum in response_data:
        print(datum)
        # NOTE: Data cleaning should be added.
        trending_posts.append(
            {
                "hashtag": hashtag,
                "postAuthorNickname": datum["author"].get("nickname"),
                "music_author": datum["added_sound_music_info"].get("author"),
                "description": datum.get("desc")
            }
        )

    return trending_posts


def get_trending_data(hashtag): 
    """
    hashtag: Keyword to filter posts by their hashtag
    # NOTE: Add batch_size for amount of posts get scrapped.
    # batch_size: Amount of posts to pull. 
        # Options:
        #     1: 20
        #     2: 40
        #     ...
        #     n: n*20
    """
    trending_posts = []
    params = {
        'name': hashtag,
        'cursor': "0",
        'token': TOKEN,
    }

    data = get_tranding_posts(hashtag, params)

    if data:
        trending_posts += data

    return trending_posts


