import json
from urllib import response

import requests
from fastapi.testclient import TestClient

from sql_app.main import app

client = TestClient(app)


def get_access_token():
    r = requests.post("http://127.0.0.1:8000/token", data={
        'grant_type': 'password',
        'username': 'ilyamarvin',
        'password': 'qwerty123456'})

    return r.json()['access_token']

token = get_access_token()

auth_headers = {'Authorization': f'Bearer {token}'}


# Тест на просмотр всех книг
def test_get_books():
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert type(response.json()) is list


# Тест на поиск книги    
def test_get_book_by_id():
    response = client.get("/api/v1/books/1/")
    assert response.status_code == 200


# Тест на просмотр всех полок
def test_get_shelves():
    response = client.get("/api/v1/shelves/", headers=auth_headers)
    assert response.status_code == 200
    assert type(response.json()) is list

    
# Тест на поиск полки
def test_get_shelf_by_id():
    response = client.get("/api/v1/shelves/12/", headers=auth_headers)
    assert response.status_code == 200

    
# Тест на просмотр всех пользователей
def test_get_users():
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert type(response.json()) is list

    
# Тест на поиск пользователя
def test_get_user_by_id():
    response = client.get("/api/v1/users/1/")
    assert response.status_code == 200

        
# Тест на просмотр всех авторов
def test_get_authors():
    response = client.get("/api/v1/authors/")
    assert response.status_code == 200
    assert type(response.json()) is list


# Тест на поиск автора
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


def test_search_author():
    response = client.get("/api/v1/authors/?q=Пушкин")
    assert response.status_code == 200
    assert type(response.json()) is list
    assert all(element["surname"] != "Пушкин" for element in response.json()) == False


def test_search_book():
    response = client.get("/api/v1/books/?q=Герой&нашего&времени")
    assert response.status_code == 200
    assert type(response.json()) is list
    assert all(element["title"] != "Герой нашего времени" for element in response.json()) == False


def test_get_review_by_id():
    response = client.get("/api/v1/reviews/1")
    assert response.status_code == 200


def test_add_review():
    global review_id
    response = client.post("/api/v1/reviews?user_id=2&book_id=1", json={"id": 0, "text": "Хорошая книга!", "score": 5})
    assert response.status_code == 200
    review_id = response.json()["id"]


def test_delete_review():
    response = client.delete(f"/api/v1/reviews/{review_id}")
    assert response.status_code == 200


def test_add_shelf():
    global shelf_id
    response = client.post(
        "/api/v1/shelves", 
        headers=auth_headers, 
        json={
            "id": 0, 
            "title": "Новая полка", 
            "description": "Моя новая полка", 
            "type_of_shelf": True
        }
    )
    assert response.status_code == 200
    shelf_id = response.json()["id"]


def test_delete_shelf():
    response = client.delete(f"/api/v1/shelves/{shelf_id}", headers=auth_headers)
    assert response.status_code == 200
