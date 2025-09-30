import pytest
import requests

base_url = "https://ru.yougile.com"
project_id = None


@pytest.fixture(scope="session")
def get_token():
    my_headers = {'Content-Type': 'application/json'}
    info = {
        "login": "vicktoriyavakhing@gmail.com",
        "password": "U8dYNe~Pq<[o7Ya",
        "companyId": "2f08f167-2c32-458c-9579-f250677ea270"
    }

    resp = requests.post(base_url + '/api-v2/auth/keys', headers=my_headers, json=info)
    data = resp.json()
    print(data)
    return data["key"]


@pytest.fixture
def auth_headers(get_token):
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_token}'
    }


def test_create_project_positive(auth_headers):
    global project_id
    project_data = {
        "title": "Python",
        "users": {"a40b4f42-acd5-4afc-b5c7-6b82311fa008": "admin"}
    }
    resp = requests.post(base_url + '/api-v2/projects', headers=auth_headers, json=project_data)
    project_id = resp.json()["id"]
    assert resp.status_code == 201
    assert project_data["title"] == "Python"


def test_create_project_negative(auth_headers): 
    # невалидные вводные данные, нет User
    project_data = {
        "title": "Nice",
        "users": {"a40b4f42-acd5-4afc-b5c7-6b82311fa008": "--"} 
    }

    resp = requests.post(base_url + '/api-v2/projects', headers=auth_headers, json=project_data)

    assert project_data["title"] == "Nice"
    with pytest.raises(AssertionError):
        assert resp.status_code == 201


def test_get_project_with_id_positive(auth_headers):
    global project_id
    assert project_id is not None

    resp = requests.get(f"{base_url}/api-v2/projects/{project_id}", headers=auth_headers)

    assert resp.status_code == 200
    data = resp.json()["id"]
    assert project_id == data


def test_get_project_with_id_negative(auth_headers):
    # невалидный id
    fake_id = str(123)

    resp = requests.get(f"{base_url}/api-v2/projects/{fake_id}", headers=auth_headers)

    assert resp.status_code in (400, 404)


def test_change_project_positive(auth_headers):
    global project_id
    assert project_id is not None
    payload = {"title": "Updated Python Project"}   

    resp = requests.put(f'{base_url}/api-v2/projects/{project_id}', headers=auth_headers, json=payload)

    assert resp.status_code == 200
    assert payload["title"] == 'Updated Python Project'


def test_change_project_negative(auth_headers):
    # невалидный id
    fake_id = str(123)
    payload = {"title": "Updated Python Project"}   

    resp = requests.put(f'{base_url}/api-v2/projects/{fake_id}', headers=auth_headers, json=payload)

    assert payload["title"] == 'Updated Python Project'
    assert resp.status_code in (400, 404)


def test_delete_token(get_token):
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_token}'
    }
    resp = requests.delete(f"{base_url}/api-v2/auth/keys/{get_token}", headers=my_headers)
    assert resp.status_code == 200
