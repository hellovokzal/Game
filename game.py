from flask import Flask, request, jsonify
from requests import post, get

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo1():
    if request.method == 'POST':
        data = request.get_json()
        site = post("http://arch.ksys.ru/", data=data, timeout=15)
        return site.json()
    else:
        site = get("http://arch.ksys.ru/", timeout=15)
        return site.text()

@app.route("/<path:message>", methods=['GET', 'POST'])
def echo(message):
    if request.method == 'POST':
        data = request.get_json()
        site = post(f"http://arch.ksys.ru/{message}", data=data, timeout=15)
        return site.json()
    else:
        site = get(f"http://arch.ksys.ru/{message}", timeout=15)
        return site.text()

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

def error1(e):
	return """
 <!DOCTYPE html>
<html>
<head>
  <title>500 Error Loading</title>
</head>
<body>
  <h1>500 Error Loading</h1>
  <p>Ошибка загрузки!</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
