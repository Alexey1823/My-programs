from flask import Flask
from os import environ


app=Flask(__name__)


@app.route("/")
def index():
    return"<p>Hello Synergy!</p>"


port = environ.get("PORT", 5000)
host = environ.get("HOST", "0.0.0.0")
app.run(host, port)
