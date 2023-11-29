from flask import Flask, request, jsonify
from requests import post, get

site = ""

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo1():
    global site
    if request.method == 'POST':
        data = request.get_json()
        site = post("https://letomer.ru/", data=data, timeout=15)
        return str(f"{site.json()}")
    else:
        site = get("https://letomer.ru/", timeout=15)
        return str(f"{site.text()}")

@app.route("/<path:message>", methods=['GET', 'POST'])
def echo(message):
    global site
    if request.method == 'POST':
        data = request.get_json()
        site = post(f"https://letomer.ru/{message}", data=data, timeout=15)
        return str(f"{site.json()}")
    else:
        site = get(f"https://letomer.ru/{message}", timeout=15)
        return site.text

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

@app.errorhandler(404)

def error1(e):
	return """
 <!DOCTYPE html>
<html>
<head>
  <title>Not Found</title>
</head>
<body>
  <h1>Not Found</h1>
  <p>Not Loading</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
