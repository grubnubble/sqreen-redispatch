from flask import Flask, request
import sqreen

sqreen.start()
app = Flask(__name__)



@app.route('/')
def hello():
	return 'hello, world!'

@app.route('/notify', methods=["POST"])
def notify():
	if request.data:
		# simple check to keep in mind that we 
		# 	need to validate the request in some way
		print request.data
		return request.data
	else:
		return 'bad request!', 400