import geocoder
import socket
from yelpapi import YelpAPI

api_key = "0PlhQ1heSAsyVXWgveoroa0CBfJIjQSmYpz2H6TYIF6TYkXgrX-nrWLPYkOlXSobjb1X37QUehHVBLMUEw3HsaK4J90j-Y-jFRA-bj5xbbpAtoZqA17-5IK-UJx-XHYx"
yelp_api = YelpAPI(api_key)
# search_results = yelp_api.search_query(args)

# argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. '
#                                                 'Visit https://www.yelp.com/developers/v3/manage_app to get the '
#                                                 'necessary API keys.')
# argparser.add_argument('api_key', type=str, help= "yelpAPIkey")
# # args = argparser.parse_args()
# argparser.parse_args(['api_key','0PlhQ1heSAsyVXWgveoroa0CBfJIjQSmYpz2H6TYIF6TYkXgrX-nrWLPYkOlXSobjb1X37QUehHVBLMUEw3HsaK4J90j-Y-jFRA-bj5xbbpAtoZqA17-5IK-UJx-XHYx'])
# yelp_api = YelpAPI(args.api_key)

# ipMe = socket.gethostbyname(socket.gethostname())#should return user's ip address?
# g = geocoder.ip(str(ipMe))
# currentLat = g.latlng
# print(currentLat)
results = yelp_api.search_query(term="Boba tea", location="Englewood")

print(results)
startingLocation = input("What is your starting address?")
endingLocation = input("What is your end address?")

Gmaps = googlemaps.Client(key='AIzaSyAYgVkq5nEN8zigOctrNfzpDrNjiKq9CWg', client_id=None, client_secret=None, timeout=None, connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, queries_per_second=50, channel=None, retry_over_query_limit=True)

#look into cgi module for form methods like field storage
