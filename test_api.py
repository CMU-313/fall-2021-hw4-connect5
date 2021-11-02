import requests
import json
import pytest
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

URL = 'http://localhost:5000/predict'
URL_JSON = 'http://localhost:5000/predictjson'


@pytest.fixture
def http():
    http = requests.Session()
    retries = Retry(total=10, backoff_factor=0.1)
    http.mount('http://', HTTPAdapter(max_retries=retries))
    return http


def test_empty_request(http):
    response = http.get(URL)
    assert response.status_code == 400


def test_url_request(http):
    params = {'age': 10, 'absences': 5, 'health': 1, 'G2': 15}
    response = http.get(URL, params=params)
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'


def test_api_request(http):
    data = {'age': 10, 'absences': 5, 'health': 1, 'G2': 15}
    headers = {'Content-Type': 'application/json'}
    response = http.post(URL_JSON, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'


def test_invalid_url_request(http):
    params = {'age': 10, 'absences': 5, 'health': 1}
    response = http.get(URL, params=params)
    assert response.status_code == 400


def test_invalid_api_request(http):
    data = {'age': 10, 'absences': 5}
    headers = {'Content-Type': 'application/json'}
    response = http.post(URL_JSON, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
