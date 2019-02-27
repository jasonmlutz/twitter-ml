import oauth2 as oauth
import json
from credentials import *

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
