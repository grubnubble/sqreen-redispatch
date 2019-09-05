from flask import Flask, request
import hashlib
import hmac
import re
import sqreen
from twilio.rest import Client

sqreen.start()
app = Flask(__name__)
SECRET = '59e1b59394ca7450f3d4ae0db3fb4083'
TWILIO_PHONE = '+18574454093' # NOT a real, working Twilio phone
PHONE = '+10005552222' # example only

def check_signature(secret_key, request_signature, request_body):
	"""Helper function from Sqreen docs"""

	hasher = hmac.new(secret_key, request_body, hashlib.sha256)
	dig = hasher.hexdigest()

	return hmac.compare_digest(dig, request_signature)

def send_sms(phone, notification):
	"""Helper function to send sms to a given phone number"""
	# not secure - these can be found at twilio.com/console
	account_sid = 'XXXX'
	auth_token = 'XXXX'

	client = Client(account_sid, auth_token)

	message = client.messages.create(body=notification,
										to=PHONE,
										from_=TWILIO_PHONE)
	return message.sid

@app.route('/')
def hello():
	return 'hello, world!'

@app.route('/notify', methods=["POST"])
def notify():
	request_signature = str(request.headers.get('X-Sqreen-Integrity'))
	if check_signature(SECRET, request_signature, request.get_data()):
		# This message will log to the flask app when it is in debug mode
		app.logger.info("Notification from Sqreen: %s", request.data)
		# Send the request data to a phone number
		send_sms(PHONE, request.data)
		print(request.data)
		return request.data
	else:
		return 'bad request!', 400

if __name__ == '__main__':
	app.run(debug=True)