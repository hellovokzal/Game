from flask import Flask, request, jsonify
from requests import post, get

app = Flask(__name__)

@app.route("/<path:message>", methods=['GET', 'POST'])
def echo1():
    if request.method == 'POST':
        data = request.get_json()
        site = post("{message}", data=data, timeout=15)
        return site.text()
    else:
        site = get("{message}", timeout=15)
        return site.text()

@app.route("/<path:message>", methods=['GET', 'POST'])
def echo(message):
    if request.method == 'POST':
        data = request.get_json()
        site = post(f"{message}", data=data, timeout=15)
        return site.text()
    else:
        site = get(f"{message}", timeout=15)
        return site.text()

@app.route("/favicon.ico")

@app.errorhandler(500)

def error(e):
	return """
 <!DOCTYPE html>
<html>
<head>
  <title>500 Internal Server Error</title>
</head>
<body>
  <h1>500 Internal Server Error</h1>
  <p>Не удалось загрузить сайт!</p>
</body>
</html>
"""

@app.errorhandler(500)

def error(e):
	return """
 <!DOCTYPE html>
<html>
<head>
  <title>404 Not Found</title>
</head>
<body>
  <h1>404 Not Found</h1>
  <p>Ссылка пустая!</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
