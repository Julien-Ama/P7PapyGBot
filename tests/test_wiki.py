# coding=utf-8
from app import WikiWrapper

def test_1():
    latitude = "2.35183"
    longitude = "48.85658"
    mock_title = "Paris"
    mock_description = "Paris (/pa.ʁi/) est la commune la plus peuplée et la capitale de la France.\nElle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la Marne et l'Oise. Paris est également le chef-lieu de la région Île-de-France et le centre de la métropole du Grand Paris, créée en 2016."
    mock_url = "https://fr.wikipedia.org/wiki/Paris"
    myWikiWrapper = WikiWrapper(latitude, longitude)
    print(myWikiWrapper.content)
    assert myWikiWrapper.content["title"] == mock_title
    assert myWikiWrapper.content["description"] == mock_description
    assert myWikiWrapper.content["url"] == mock_url
    assert myWikiWrapper.content == {
        "title": mock_title,
        "description": mock_description,
        "url": mock_url
    }

