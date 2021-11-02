import requests
import json

URL = 'http://localhost:5000/predict'
URL_JSON = 'http://localhost:5000/predictjson'

def test_empty_request():
    response = requests.get(URL)
    assert response.status_code == 500

def test_url_request():
    params = {'age' : 10, 'absences' : 5, 'health' : 1}
    response = requests.get(URL, params=params)
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'

def test_api_request():
    data = {'age' : 10, 'absences' : 5, 'health' : 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(URL_JSON, data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'