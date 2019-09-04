from app import *

client = app.test_client()

def test_hello():
    response = client.get("/")
    assert response.status_code == 200

def test_notify():
	data = "here is some data"
	hasher = hmac.new(SECRET, data, hashlib.sha256)
	good_token = hasher.hexdigest()
	response = client.post("notify", data=data, headers={'X-Sqreen-Integrity': good_token})
	
	assert response.status_code == 200
	assert response.data == data

def test_notify_fails_with_bad_signature():
	bad_token = 'xxxxx'
	response = client.post("notify", headers={'X-Sqreen-Integrity': bad_token})
	assert response.status_code == 400
