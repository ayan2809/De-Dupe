#flask app
from flask import *
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mode')
def mode():
    return render_template('mode.html')

@app.route('/singleMode')
def singleMode():
    return render_template('singleMode.html')

@app.route('/multiMode')
def multiMode():
    return render_template('multiMode.html')

@app.route('/dataUpload')
def dataUpload():
    return render_template('dataUpload.html')


@app.route('/failure')
def failure():
    return render_template('failure.html')


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8081,
                        type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
