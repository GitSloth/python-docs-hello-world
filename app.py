from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def testing():
    return 'test'

@app.route('/datatrans', methods = ['POST', 'GET'])
def dattransfer():
    data = float(requests.args.get('value'))
    if data > 10:
        return '1'
    else:
        return '0'