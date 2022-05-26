from distutils.log import debug
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        json_ = request.get_json()
        return jsonify({'POSTED: ': json_}), 201
    else:
        return jsonify({'about': "Hello world"})


@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply(num):
    return jsonify({'result': num*num})


app.run(debug=True)
