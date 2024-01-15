from fastapi.testclient import TestClient
from main import app,server
import pytest
import asyncio

client = TestClient(app)

 
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module", autouse=True)
async def server():
    # Start the server
    await server.run()

    # Provide the server some time to start up
    await asyncio.sleep(1)
    yield server()
    # Stop the server
    await server.should_exit()
 

      
    
def test_create_todos():
    # Define the request payload
    todo_data = {
        "title": "Test Todo",
        "description": "This is a test todo",
        "priority": 3,
        "completed": False
    }

    # Perform a POST request to the /create_todo endpoint
    response = client.post("/todos/create_todo", json=todo_data)
  
    # Check that the response status code is 201 (Created)
    assert response.status_code == 200
    expected_data = {
        "status": 201,
        "transaction": "Successfull"
    }
    assert response.json() == expected_data

def test_get_todos():
    # Create a FastAPI test client
    
    # Perform a GET request to the /todos endpoint
    response = client.get("/todos/")
    assert response.status_code == 200
    last_id = Last_Todo()
    expected_data = todo_data = {
        "title": "Test Todo",
        "description": "This is a test todo",
        "priority": 3,
        "completed": False,
        'id': last_id
    }
    assert expected_data in response.json()

def test_update_todos():
    last_id = Last_Todo()
    response = client.patch(f'/todos/{last_id}?completed={True}')
    response.status_code==200
    expected_data = {
        "status": 200,
        "transaction": "Successfull"
    }
    assert response.json() == expected_data

def test_updated_status_of_todo():
    last_id = Last_Todo()
    last_todo_status = Last_Todo_Status()
    assert True == last_todo_status


def test_delete_todos():
    last_id = Last_Todo()
    response = client.delete(f"todos/delete_todo/{last_id}")
    expected_data = {
        "status": 201,
        "transaction": "Successfull"
    }
    assert response.json() == expected_data
    
def test_delete_todo_not_found():
    response = client.delete('todos/delete_todo/999999')
    assert response.status_code == 404
    expected_response = {'detail': 'todo not found'}
    assert response.json() == expected_response   
    
    
def Last_Todo():
    response_for_last_id = client.get('/todos/')
    todos = response_for_last_id.json()
    last_todo_id = todos[-1]['id']
    return last_todo_id

def Last_Todo_Status():
    response_for_last_id = client.get('/todos/')
    todos = response_for_last_id.json()
    last_todo_status = todos[-1]['completed']
    return last_todo_status