from flask import Flask
import os

app = Flask(__name__)

@app.route("/hello")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route("/sys")
def get_sys():
	
	hostname = os.environ['NAME']
	return f"<p>{hostname}</p>"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=8080)

