from fastapi.testclient import TestClient
from main import app, ConversationManager

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert ConversationManager._is_initialized == False
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_convert_query():
    query_request = {"user_query": "Give me sum of all benefits in year 2013"}
    response = client.post("/convert-query", json=query_request)
    assert ConversationManager._is_initialized == True
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert "sql_query" in response.json()
    assert 'SELECT SUM(Benefits) FROM Salaries WHERE Year = 2013' in response.json()['sql_query']

def test_execute_query():
    sql_query = {"sql_query": "SELECT SUM(Benefits) FROM Salaries WHERE Year = 2013"}
    response = client.post("/execute-query", json=sql_query)
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert len(response.json()) > 0
    assert "896116253.5699887" == str(response.json()['query_result'][0]['SUM(Benefits)'])

def test_memory():
    query_request = {"user_query": "Give me sum of all benefits in year 2013"}
    query_request_2 = {"user_query": "Now for base pay"}
    client.post("/convert-query", json=query_request)
    response = client.post("/convert-query", json=query_request_2)
    assert 'SELECT SUM(BasePay) FROM Salaries WHERE Year = 2013' in response.json()['sql_query']