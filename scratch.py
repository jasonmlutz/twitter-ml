import oauth2 as oauth
import json
from credentials import *

#def oauth_req(url, http_method="GET", post_body="", http_headers=None):
#    """ From https://developer.twitter.com/en/docs/basics/authentication/guides/single-user
#    """
#    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#    token = oauth2.Token(key=TOKEN_KEY, secret=TOKEN_SECRET)
#    client = oauth2.Client(consumer, token)
#    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
#    return content
#
#home_timeline = oauth_req("https://api.twitter.com/1.1/statuses/home_timeline.json")


consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

search_endpoint = "https://api.twitter.com/1.1/search/tweets.json"
timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"

custom_search = "nasa"

compiled_search_endpoint = search_endpoint+"?q="+custom_search+"&count=100&result_type=recent&lang=en"

#response, data = client.request(timeline_endpoint)
response, data = client.request(compiled_search_endpoint)

tweets = json.loads(data)

count=0
for status in tweets['statuses']:
    print("{}. {}\n".format(count, status['text']))
    count += 1
