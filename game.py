from flask import Flask, request, jsonify
from requests import post, get

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def echo1():
    if request.method == 'POST':
        data = request.get_json()
        site = post("https://acb.basketballrandom.net/demo", json=data)
        return site.json()
    else:
        site = get("https://acb.basketballrandom.net/demo")
        return site.text

@app.route("/<path:message>", methods=['GET', 'POST'])
def echo(message):
    if request.method == 'POST':
        data = request.get_json()
        site = post(f"https://acb.basketballrandom.net/{message}", json=data)
        return site.json()
    else:
        site = get(f"https://acb.basketballrandom.net/{message}")
        return site.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
