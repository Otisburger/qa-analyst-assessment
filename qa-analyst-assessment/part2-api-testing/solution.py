import pytest
import requests

# sends a get request and asserts that the response received contains an id, name, email, and a status code of 200 
def test_fetch_user_successfully():
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(url + '/users/1')
    responseDict = response.json()
    assert ("id" in responseDict) == True
    assert ("name" in responseDict) == True
    assert ("email" in responseDict) == True
    assert response.status_code == 200

# sends a post request containing json data and asserts that the response received has a status code between 200 and 299
def test_create_new_post():
    url = "https://jsonplaceholder.typicode.com"
    response = requests.post(url + '/posts', {"data": "data"})
    assert 200 <= response.status_code <= 299

# sends a get request and asserts that the response received has a status code of 404
def test_handle_nonexistent_user():
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(url + '/users/999')
    assert response.status_code == 404