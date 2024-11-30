import pytest
import requests
import json

def test_l33():
    """Tests fetching data from the provided URL"""
    # Send a GET request to the URL
    url = "https://api.allorigins.win/raw?url=http://beans.itcarlow.ie/prices.html"

    # Send a GET request to the URL
    response = requests.get(url, headers = {'User-agent': 'pyZombis'})

    # Check for successful response (status code 200)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, 33 - 1/4/6/7/9 will fail"