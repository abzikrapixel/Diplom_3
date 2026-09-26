import requests
from helpers.data import NAME, PASSWORD, generate_email
from helpers.urls import API_REGISTER, API_USER

def register_user():
    email = generate_email()
    payload = {"email": email, "password": PASSWORD, "name": NAME}
    response = requests.post(API_REGISTER, json=payload, timeout=20)
    token = response.json().get("accessToken")
    return email, token

def delete_user(token):
    return requests.delete(API_USER, headers={"Authorization": token}, timeout=20)