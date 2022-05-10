from app import GeoWrapper
import requests

def test_paris_geo():
    input = "paris"
    mock_latitude = 2.35183
    mock_longitude = 48.85658

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude

def test_marseille_geo():
    input = "marseille"
    mock_latitude = 5.369952
    mock_longitude = 43.296174

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude

def test_bsg_geo():
    input = "Bussy-Saint-Georges"
    mock_latitude = 2.697386
    mock_longitude = 48.843026

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude

def test_wrong():
    input = ""
    mock_latitude = None
    mock_longitude = None

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude

def test_barcelone_geo():
    input = "Barcelone"
    mock_latitude = 2.177432
    mock_longitude = 41.382894

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude

def test_get_location_coordinates_success(monkeypatch, ):  # monkeypatch fixture to replace
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {
                "type": "FeatureCollection",
                "query": ["barcelone"],
                "features": [
                    {
                        "geometry": {
                            "type": "Point",
                            "coordinates": [1.11111111, 1.11111111],
                        },
                    }
                ],
            }

    def mock_get_reponse(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_reponse)
    request = GeoWrapper("toto")
    assert request.longitude == 1.11111111
    assert request.latitude == 1.11111111


def test_with_mock_testing_err_status_code(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 404

        def json(self):
            return {"error": "bad request"}

    def mock_get_reponse(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_reponse)

    input = "paris"
    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == None
    assert myGeoWrapper.longitude == None
