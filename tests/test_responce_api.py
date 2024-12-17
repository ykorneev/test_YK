import pytest
import requests


def test_get():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_dict = response.json()
    assert response.status_code == 200
    assert 'massage' in response.text

def test_json():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    response_json = response.json()

    assert response.status_code == 200, f"status code should be 200, but get {response.status_code}"
    assert 'message' in response_json.keys(), "key 'message' not in body"
    assert 'status' in response_json.keys(), "key 'status' not in body"
    assert 'code' not in response_json.keys(), "key 'code' in body"

    assert response_json['status'] == 'success'
    assert 'images.dog.ceo/breeds' in response_json['message']

@pytest.mark.parametrize("code, result", [(200, True), (300, True), (400, False), (500, False)])
def test_raise_for_status(code, result):
    url = f'https://httpbin.org/status/{code}'

    response = requests.get(url)

    try:
        response.raise_for_status()
        assert result == True
    except requests.HTTPError as err:
        print(err)
        assert result


