from configuration.config import GEO_API_URL, GEO_TOKEN


import requests


class GeoWrapper:

    def __init__(self, input):
        self.input = input
        self.latitude = None
        self.longitude = None
        self.get_coordinates()

    def get_coordinates(self):
        result = requests.get(f"{GEO_API_URL}{self.input}"
                              f".json?access_token={GEO_TOKEN}&language=fr")
        if result.status_code == 200 and self.input != "":
            json_result = result.json()  # conversion Json
            if len(json_result['features']) > 0:
                self.latitude =\
                    json_result['features'][0]['geometry']['coordinates'][0]
                self.longitude =\
                    json_result['features'][0]['geometry']['coordinates'][1]
        else:
            print("Il y a un souci dans la requête")
