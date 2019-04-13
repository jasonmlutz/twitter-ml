import oauth2 as oauth
import json
from credentials import *

def oauth_twitter_search(query, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, lang="en", result_type="recent", count=100):
    """ Search Twitter ...
    looks like Tweets with "truncated": true could pose a problem
    """
    search_endpoint = "https://api.twitter.com/1.1/search/tweets.json"
    compiled_search_endpoint = "{}?q={}&count={}&result_type={}&lang={}".format(search_endpoint, query, count, result_type, lang)
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    client = oauth.Client(consumer)
    response, data = client.request(compiled_search_endpoint)
    tweets = json.loads(data)
    return tweets

nasa_tweets = oauth_twitter_search("@nasa")
control_tweets = oauth_twitter_search("the")
