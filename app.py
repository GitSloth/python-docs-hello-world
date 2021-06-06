from flask import Flask
from flask import request,Response 

app = Flask(__name__)


@app.route('/')
def testing():
    return 'test'

@app.route("/test",methods=['POST', 'GET'])
def progress():
    data = float(request.args.get('value'))
    if data => 20:
        return flag = 1
    else:
        return flag = 0