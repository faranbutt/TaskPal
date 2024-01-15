from fastapi.testclient import TestClient
client = TestClient(app)


response = client.get('/todos/')
print(response)