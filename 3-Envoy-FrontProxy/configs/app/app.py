import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/e1")
def hello():
    return "Coming from 1st endpoint!"


@app.route("/e2")
def hello2():
    return "Coming from 2nd endpoint!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9090)
