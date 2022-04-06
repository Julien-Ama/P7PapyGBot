# coding=utf-8
import requests

from configuration.config import WIKI_API_URL
from pprint import pprint

class WikiWrapper:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.content = None
        self.get_info_from_long_lat()

    def get_info_from_long_lat(self):

        payload = {
            "action": "query",
            "format": "json",
            "ggscoord": f"{self.longitude}|{self.latitude}",
            "generator": "geosearch",
            "prop": "extracts|info",
            "explaintext": True,  # convert HTML to plain text
            "exsentences": 3,  # how many sentences to return
            "inprop": "url",  # get url (added info to prop for this)
        }
        result = requests.get(WIKI_API_URL, payload)

        if result.status_code == 200:
            json_result = result.json()
            print("wiki")
            pprint(json_result)

            if 'query' in json_result:
                pages = json_result['query']['pages']
                pages = (list(pages.values()))

                title = pages[0]['title']
                description = pages[0]['extract']
                url = pages[0]["fullurl"]

                print(title)
                print(description)
                print(url)

                self.content = {
                    "title" : title,
                    "description" : description,
                    "url" : url
                }