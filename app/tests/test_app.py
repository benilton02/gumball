

def test_select_400(client):
    id = 20000
    url = f"/{id}"
    
    response = client.get(url)
    result = response.status_code
    expected = 400
    
    assert expected == result

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
    