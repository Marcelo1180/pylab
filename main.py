import json
from flask import Flask, Response, jsonify, request, abort
import webbrowser

app = Flask(__name__)
@app.route('/')
def home():
    # return jsonify({'status': 'El servicio se encuentra disponible'}), 200
    print (request)
    return '<h1>oh</h1> haasfasdfd fasdffasdfadfi'

if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    app.run(host='localhost', port=5000, debug=True)
