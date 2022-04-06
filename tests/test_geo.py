from app import GeoWrapper

def test_2():
    input = "paris"
    mock_latitude = 2.35183
    mock_longitude = 48.85658

    myGeoWrapper = GeoWrapper(input)
    assert myGeoWrapper.latitude == mock_latitude
    assert myGeoWrapper.longitude == mock_longitude
