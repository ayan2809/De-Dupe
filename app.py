#flask app
from flask import *
from flask_cors import CORS
from dedupe import *
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage



app = Flask(__name__)
CORS(app)
app.secret_key = 'sessionNameEZPZ'
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

@app.route('/singleUserResult')
def singleUserResult():
    return render_template('singleUserResult.html', data=session['temp_dict'])

@app.route('/failure')
def failure():
    return render_template('failure.html')


@app.route('/check_duplication', methods=['POST'])
def check_duplication():
    # Fetching the data from the form
    MRN=request.form['MRN']
    firstName=request.form['firstName']
    lastName=request.form['lastName']
    DOB=request.form['DOB']
    State= request.form['State']
    Pincode=request.form['Pincode']
    Phone = request.form['Phone']
    YOE=request.form['YOE']
    Specialization= request.form['Specialization']
    Education = request.form['Education']
    # Fetching the scale values
    MRNscale = request.form['MRNscale']
    fNamescale = request.form['fNamescale']
    lNamescale = request.form['lNamescale']
    DOBscale = request.form['DOBscale']
    Statescale = request.form['Statescale']
    Pincodescale = request.form['Pincodescale']
    Phonescale = request.form['Phonescale']
    YOEscale = request.form['YOEscale']
    Specializationscale = request.form['Specializationscale']
    Educationscale = request.form['Educationscale']

    response=checkDuplicates(MRN,firstName,lastName,DOB,State,Pincode,Phone,YOE,Specialization,
                    Education,MRNscale,fNamescale,lNamescale,DOBscale,Statescale,
                    Pincodescale,Phonescale,YOEscale,Specializationscale,Educationscale)
    # response = {'fName': firstName, 'lName': lastName, 'YOE': YOE}
    # print(response['check'])
    # if response['check']==1:
    #     return redirect(url_for('singleUserResult'))
    #     # return render_template('singleUserResult.html')
    # else:

    session['temp_dict'] = response['data']
    return jsonify(response), 200


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      session['filename'] = f.filename
      return session['filename']


@app.route('/check_bulk_duplication', methods=['POST'])
def check_bulk_duplication():
    return 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
