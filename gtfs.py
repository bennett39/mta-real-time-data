from google.transit import gtfs_realtime_pb2
from dotenv import load_dotenv
import os
import requests


def get_feed(feed, url):
    response = requests.get(url, allow_redirects=True)
    feed.ParseFromString(response.content)
    with open('output.txt', mode='w') as f:
        for entity in feed.entity:
            if entity.HasField('trip_update'):
                f.write(str(entity.trip_update))

load_dotenv()
feed = gtfs_realtime_pb2.FeedMessage()
url = ('http://datamine.mta.info/mta_esi.php?key='
        + os.getenv("API_KEY")
        + '&feed_id=1')
get_feed(feed, url)
