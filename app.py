from flask import Flask
from flask import request,Response 

app = Flask(__name__)


@app.route("/")
def testing():
    return "test"

route("/test",methods=['POST', 'GET'])
def progress():
    data = float(request.args.get('value'))
    if data => 20:
        return "1"
    else:
        return "0"