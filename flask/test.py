from flask import Flask,request,jsonify
from flask_cors import CORS
app = Flask(__name__, static_folder='.', static_url_path='')
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/test')
def index():
    return app.send_static_file('index.html')

@app.route('/postTest', methods=['POST'])
def postTest():
    json=request.get_json()
    #to=json['to']
    app.logger.debug(json)
    return "aaa"
print("aaa")

app.run(port=12345, debug=True)