import requests


def test_get():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_dict = response.json()
    assert response.status_code == 200
    assert response_dict.get("massage")
    assert response_dict.get("status")


def test_get_404():
    response = requests.get('https://dog.ceo/api/breeds/image/random1') # не существующая урла 
    response_dict = response.json()
    assert response.status_code == 404
    assert response_dict.get("massage") is None
    assert response_dict.get("status") == "error"
    assert response_dict.get("code") == 404