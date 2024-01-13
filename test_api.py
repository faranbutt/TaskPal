from fastapi.testclient import TestClient
from main import app,server
import pytest
import asyncio
    
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

    # Stop the server
    await server.should_exit()
    
def test_get_todos():
    # Create a FastAPI test client
    client = TestClient(app)

    # Perform a GET request to the /todos endpoint
    response = client.get("/todos/")

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response contains the expected data
    expected_data = [
        {
            "description": "This is another dummy task description",
            "completed": False,
            "title": "Dummy Task 2",
            "id": 2,
            "priority": 2
        },
        {
            "description": "Please eat food by tomorrow",
            "completed": False,
            "title": "Food",
            "id": 4,
            "priority": 4
        }
    ]
    assert response.json() == expected_data