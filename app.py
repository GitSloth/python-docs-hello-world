from flask import Flask
from flask import request,jsonify,Response 

app = Flask(__name__)


@app.route("/")
def testing():
    return "test"

@app.route("/testrun",methods=['POST', 'GET'])
def progress():
    data = float(request.args.get('value'))
    if data > 20:
        flag = "true"
    else:
        flag = "false"
    return flag