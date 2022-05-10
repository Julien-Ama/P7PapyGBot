# coding=utf-8
from app import WikiWrapper
import requests


def test_paris_wiki():
    latitude = "2.35183"
    longitude = "48.85658"
    mock_title = "Paris"
    mock_description = ("Paris (/pa.ʁi/) est la commune la plus peuplée " 
                       "et la capitale de la France.\nElle se situe au " 
                       "cœur d'un vaste bassin sédimentaire aux sols " 
                       "fertiles et au climat tempéré, le bassin parisien," 
                       " sur une boucle de la Seine, entre les confluents" 
                       " de celle-ci avec la Marne et l'Oise. Paris est" 
                       " également le chef-lieu de la région Île-de-France" 
                       " et le centre de la métropole du Grand Paris, " 
                       "créée en 2016.")
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

def test_marseille_wiki():
    latitude = "5.369952"
    longitude = "43.296174"
    mock_title = "Marseille"
    mock_description = ("Marseille est une commune du Sud-Est de la France, "
                        "chef-lieu du département des Bouches-du-Rhône et "
                        "préfecture de la région Provence-Alpes-Côte d'Azur."
                        "\nEn 2019, Marseille est la deuxième commune la "
                        "plus peuplée de France avec 870 731 habitants. Son "
                        "unité urbaine, qui s'étend au nord jusqu'à "
                        "Aix-en-Provence, est la troisième de France avec "
                        "1 614 501 habitants, derrière Paris et Lyon.")
    mock_url = "https://fr.wikipedia.org/wiki/Marseille"
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

def test_bsg_wiki():
    latitude = "2.697386"
    longitude = "48.843026"
    mock_title = "Bussy-Saint-Georges"
    mock_description = ("Bussy-Saint-Georges est une commune française "
                        "située dans le département de Seine-et-Marne en "
                        "région Île-de-France.\nAvec 26 597 habitants au "
                        "recensement de 2019, Bussy-Saint-Georges est la "
                        "commune la plus peuplée de la communauté "
                        "d'agglomération de Marne et Gondoire.\n\n\n== "
                        "Géographie ==\n\n\n=== Localisation ===\n\nÀ vol "
                        "d'oiseau, la commune est située à 25,9 km à l'est "
                        "de Paris, à 19,0 km à l'ouest de Meaux et à 7 km du "
                        "parc à thème Disneyland Paris.")
    mock_url = "https://fr.wikipedia.org/wiki/Bussy-Saint-Georges"
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

def test_with_mock_testing_err_status_code(monkeypatch,):

    class MockResponse:
        def __init__(self):
           self.status_code = 404

        def json(self):
            return {"error" : "bad request"}

    def mock_get_reponse(url, payload):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_reponse)

    latitude = "2.35183"
    longitude = "48.85658"
    myWikiWrapper = WikiWrapper(latitude, longitude)
    assert myWikiWrapper.content == None
