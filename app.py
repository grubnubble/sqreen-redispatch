from flask import Flask
import sqreen

sqreen.start()
app = Flask(__name__)

@app.route('/')
def hello():
	return 'hello, world!'