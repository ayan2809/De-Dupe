#flask app
from flask import *
from flask_cors import CORS
import requests
import urllib.request
import json
import requests
import random
import string


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8081,
                        type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
