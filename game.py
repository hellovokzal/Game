from flask import Flask

num = 0

app = Flask(__name__)

@app.route("/")

def echo():
	global num
	num = num + 1
	return str(num)
	
@app.route("/<path:message>")

def echo1(message):
	global num
	num = num + 1
	return f"""<title>{message}</title>
<h1>{num}</h1>
"""

@app.errorhandler(500)

def echo2(e):
	return "Error load!"
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
