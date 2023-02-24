import pytest
import requests
import json

url = "https://automationintesting.online/message/"

def test_message_api_creats_new_messages():
    response = requests.post(url, json={
        'description':'Hello, is there any discounts?',
        'email':'jane@email.com',
        'name':'Jane',
        'phone':'12345678900',
        'subject':'Any discounts?',
    })
    assert response.status_code == 201
    print(response.text)

def test_message_api_creats_new_messages():
    response = requests.post(url, json={
        'description':'Hello, is room 102 vacant?',
        'email':'smith@email.com',
        'name':'smith',
        'phone':'04506797000',
        'subject':'room 102 vacant?',
    })
    assert response.status_code == 201
    print(response.text)
