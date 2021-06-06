from flask import Flask
from flask import request

app = Flask(__name__)


ledFlag = 0 

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    print(content)
    return 'JSON posted'
    
    
@app.route('/testrun')
def testrunner():
    return 'please receive this'


@app.rout('/ledFlag')
def giveLEDFlag():
    return ledFlag
