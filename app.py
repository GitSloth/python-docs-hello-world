from flask import Flask
from flask import request,Response 

app = Flask(__name__)


@app.route('/')
def testing():
    return 'test'

@myapp.route("/test",methods=['POST', 'GET'])
def progress():
    data = float(request.args.get('value'))
    if data => 20:
        flag = 1
    else:
        flag = 0
    return flag