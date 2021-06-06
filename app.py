from flask import Flask
from flask import request

app = Flask(__name__)


ledFlag = 0 

#unused POST method
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    print(content)
    return 'JSON posted'
    
#testrun  
@app.route('/testrun')
def testrunner():
    return 'please receive this'


@app.rout('/ledflag')
def giveLEDFlag():
    return ledFlag

