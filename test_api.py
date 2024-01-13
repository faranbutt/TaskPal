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

    yield  test_get_todos()
    yield test_create_todos()

    # Stop the server
    await server.should_exit()
    
def test_get_todos():
    # Create a FastAPI test client
    

    # Perform a GET request to the /todos endpoint
    response = client.get("/todos/")

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response contains the expected data
    expected_data = [
        {
            "completed": 'false',
            "title": "Dummy Task 2",
            "description": "This is another dummy task description",
            "id": 2,
            "priority": 2
            },
    ]
    assert  response.json() == expected_data    
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