from flask import Flask
from flask import request,Response 

app = Flask(__name__)


@app.route("/")
def testing():
    return "test"

