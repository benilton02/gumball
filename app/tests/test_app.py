from app.models import Character, db


def test_save_200(client):
    url = "/"
    payload = {
        "name": "flask"
    }
    
    response = client.post(url, json=payload)
    result = response.status_code   
    expected = 201
        
    assert result == expected
    ...
    

def test_select_200(client):
    url = '/'
    expected = 200
    
    response = client.get(url)
    result = response.status_code

    assert result == expected


def test_select_202(client):
    queryset = Character.query.all()
       
    for query in queryset:
        db.session.delete(query)
        db.session.commit()

    url = '/'
    expected = 202
    
    response = client.get(url)
    result = response.status_code

    assert result == expected


def test_select_one_400(client):
    id = 20000
    url = f"/{id}"
    
    response = client.get(url)
    result = response.status_code
    expected = 400
    
    assert result == expected
    

def test_select_one_200(client):
    id = 20000
    url = f"/{id}"
    expected = 200
    
    character_test = Character(id=id, name='anais')
    db.session.add(character_test)
    db.session.commit()
    
    response = client.get(url)
    result = response.status_code
    
    assert result == expected
    ...
    

    