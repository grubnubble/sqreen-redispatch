from app import *

client = app.test_client()

def test_hello():
    response = client.get("/")
    assert response.status_code == 200

def test_notify():
	data = "here is some data"
	response = client.post("notify", data=data)
	assert response.status_code == 200
	assert response.data == data

def test_notify_fails_appropriately():
	response = client.post("notify")
	assert response.status_code == 400
