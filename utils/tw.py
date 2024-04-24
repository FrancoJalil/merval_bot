import os
from dotenv import load_dotenv
load_dotenv()
import tweepy

API_KEY = os.environ.get("API_KEY")
API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
BEARER = os.environ.get("BEARER")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

def post_tweet(content):
    print(content)
    print("*"*20)
    try:
        api = tweepy.Client(BEARER, API_KEY, API_KEY_SECRET,
                            ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        
        
        api.create_tweet(text=content)

        
    except:
        print("Error")

