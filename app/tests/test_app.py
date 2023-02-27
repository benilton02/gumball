import os

def test_create_author_and_book(client):
    url = "/"
    
    payload = {
        'author': {
            'id': 7,
            'name': "Machado de Assis",
        },
        'book': { 
            'id': 5,
            'name':'Dom Casmurro'
        }
    }
    
    response = client.post(url, json=payload)
    result = response.status_code   
    expected = 201
    expected_keys = ['book', 'author', 'author_book']
    for key in expected_keys:
        assert key in response.json.keys()    
    assert result == expected
    

def test_get_all_authors(client):
    url = '/authors'
    expected = 200
    total_expected = 1
    
    response = client.get(url)
    result = response.status_code
    total_author = len(response.json)

    assert isinstance(response.json, list)
    assert total_expected == total_author
    assert result == expected


def test_get_all_books(client):
    url = '/books'
    expected = 200
    total_expected = 1
    
    response = client.get(url)
    result = response.status_code
    total_books = len(response.json)

    assert isinstance(response.json, list)
    assert total_expected == total_books
    assert result == expected


def test_get_author_by_id(client):
    author_id = 7
    endpoint = f'/authors/{author_id}'
    expected = 200
    
    response = client.get(endpoint)
    result = response.status_code

    assert author_id == response.json['id']
    assert result == expected
    
    
def test_get_book_by_id(client):
    book_id = 5
    endpoint = f'/books/{book_id}'
    expected = 200
    
    response = client.get(endpoint)
    result = response.status_code

    assert book_id == response.json['id']
    assert result == expected


def test_get_one_author_by_name(client):
    name = 'Machado de Assis'
    url = f"/authors/one?name={name}"
    
    response = client.get(url)
    result = response.status_code
    expected = 200

    assert result == expected
    assert isinstance(response.json, list)
    assert response.json[0]['name'] == name


def test_get_one_book_by_name(client):
    name = 'Dom Casmurro'
    url = f"/books/one?name={name}"
    
    response = client.get(url)
    result = response.status_code
    expected = 200

    assert result == expected
    assert isinstance(response.json, list)
    assert response.json[0]['name'] == name


file_path = "instance/test.db"
if os.path.exists(file_path):
    os.remove(file_path)
