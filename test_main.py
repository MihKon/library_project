import json
from urllib import response

import requests
from fastapi.testclient import TestClient

from sql_app.main import app

client = TestClient(app)


def test_get_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_book_by_id():
    response = client.get("/api/v1/books/1/")
    assert response.status_code == 200


def test_get_shelves():
    response = client.get("/api/v1/shelves/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_shelf_by_id():
    response = client.get("/api/v1/shelves/1/")
    assert response.status_code == 200

    
def test_get_users():
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_user_by_id():
    response = client.get("/api/v1/users/1/")
    assert response.status_code == 200

        
def test_get_authors():
    response = client.get("/api/v1/authors/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_author_by_id():
    response = client.get("/api/v1/authors/1/")
    assert response.status_code == 200

        
def test_get_transactions():
    response = client.get("/api/v1/transactions/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_transaction_by_id():
    response = client.get("/api/v1/transactions/1/")
    assert response.status_code == 200