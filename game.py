from flask import Flask

num = 0

text1 = ""

app = Flask(__name__)

@app.route("/")

def echo():
	global num
	global text1
	num = num + 0.5
	text1 = f"{num}"
	return f"""<title>Requests</title>
<h1>{text1[0:len(text1) - 2]}</h1>
"""
	
@app.route("/<path:message>")

def echo1(message):
	global num
	global text1
	num = num + 0.5
	text1 = f"{num}"
	return f"""<title>Custom: {message}</title>
<h1>{text1[0:len(text1) - 2]}</h1>
"""

@app.errorhandler(500)

def echo2(e):
	return "Error load!"
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
