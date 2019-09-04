from flask import Flask, request
import hmac
import hashlib
import sqreen

sqreen.start()
app = Flask(__name__)
SECRET = '59e1b59394ca7450f3d4ae0db3fb4083'

def check_signature(secret_key, request_signature, request_body):
	"""Helper function from Sqreen docs"""

	hasher = hmac.new(secret_key, request_body, hashlib.sha256)
	dig = hasher.hexdigest()

	return hmac.compare_digest(dig, request_signature)

@app.route('/')
def hello():
	return 'hello, world!'

@app.route('/notify', methods=["POST"])
def notify():
	request_signature = str(request.headers.get('X-Sqreen-Integrity'))
	if check_signature(SECRET, request_signature, request.get_data()):
		app.logger.info("Notification from Sqreen: %s", request.data)
		print(request.data)
		return request.data
	else:
		return 'bad request!', 400




if __name__ == '__main__':
	app.run(debug=True)