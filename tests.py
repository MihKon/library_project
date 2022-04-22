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