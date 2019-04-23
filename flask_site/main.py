from flask import send_from_directory
import os
#from gevent.pywsgi import WSGIServer

from flask import Flask, request, redirect, url_for, flash
from google.cloud import storage
import logging
from flask import render_template
from werkzeug.utils import secure_filename
try:
    from io import StringIO # Python 3	    from io import StringIO # Python 3
except:
    from StringIO import StringIO	    
    from io import BytesIO as StringIO

from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from googleapiclient import errors
from io import StringIO
import csv
import json
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = Flask(__name__)

# build a service obj
ml = discovery.build('ml', 'v1')
service = build('ml', 'v1')

# Instantiates a client
client = storage.Client()
# creates bucket
bucket = client.get_bucket('kanalyzers.appspot.com')
# verify bucket
#print('Bucket {} created.'.format(bucket.name))

# blob actions
#blob = bucket.blob('saved_model.pb')
#blob.upload_from_string('this is test content!')

# bucket name vars for something sam was doing
PROJECT_NAME = 'kanalyzers'
MODEL_BUCKET = 'kanalyzers.appspot.com'
MODEL_FILENAME = 'tf_model.h5'
MODEL = None


# upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'csv', 'xml'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

output_stream= StringIO()

def csvtojson(filename):
    csvfile = open(UPLOAD_FOLDER+'/'+filename, 'r')
    reader = csv.reader(csvfile)
    next(reader)
    ret = []
    for row in reader:
        cur = []
        for col in row:
            cur.append(int(col))
        ret.append(cur)

    return ret


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Sending uploaded CSV to our Cloud ML model
    service = discovery.build('ml', 'v1')

    name = 'projects/{}/models/{}'.format('kanalyzers', 'juliakeras')
    instances = csvtojson(filename)

    response = service.projects().predict(
        name=name,
        body={"instances": instances }
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    #response['predictions'][0]['dense_2'][0] accesses the returned click probabilities

    #looping through returned predictions to get all probilities returned by model
    ret = []
    for p in response['predictions']:
        if p['dense_2'][0] > 0.5:
            p = 1
        else:
            p = 0
        ret.append(p)

    df = pd.read_csv(UPLOAD_FOLDER+'/'+filename)
    df.insert(0, "clicks", ret )
    df.to_csv(UPLOAD_FOLDER+"/clickpredictions.csv", index=False)


    # values = ', '.join(str(v) for v in ret)
    #
    # return values

    return render_template('index.html')


with open("main.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')


# load model
@app.before_first_request
# def _load_model():
#     #global MODEL
#     client = storage.Client()
#     bucket = client.get_bucket(MODEL_BUCKET)
#     blob = bucket.get_blob(MODEL_FILENAME)
#     s = blob.download_as_string()
#
#     s

#  routes
@app.route('/uploads')
def uploads():
    pass


@app.route('/index.html')
def hello():
    message = "Click"
    return render_template('index.html', message=message)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form.html')
def form():
    return render_template('form.html')


@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')


@app.route('/tables.html')
def tables():
    return render_template('tables.html')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    #app.run(host='127.0.0.1', port=8080, debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    # [END gae_flex_quickstart]
