import requests

URL = 'http://localhost:5000/predict'

def test_empty_request():
    response = requests.get(URL)
    assert response.status_code == 500

def test_url_request():
    response = requests.get(URL+'?age=10&absences=5&health=1')
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'

def test_api_request():
    params = {'age' : 10, 'absences' : 5, 'health' : 1}
    response = requests.get(URL, params=params)
    assert response.status_code == 200
    text = response.text.strip()
    assert text == '0' or text == '1'