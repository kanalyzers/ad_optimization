# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import os
#from gevent.pywsgi import WSGIServer

from flask import Flask, request
from google.cloud import storage
import logging
from flask import render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)


MODEL_BUCKET = 'kanalyzers.appspot.com'
MODEL_FILENAME = 'tf_model.h5'
MODEL = None

# upload folder
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.before_first_request
def _load_model():
    #global MODEL
    client = storage.Client()
    bucket = client.get_bucket(MODEL_BUCKET)
    blob = bucket.get_blob(MODEL_FILENAME)
    s = blob.download_as_string()

    s


@app.route('/index.html')
def index():
    message = "Click"
    return render_template('index.html', message=message)


@app.route('/form.html')
def form():
    return render_template('form.html')


@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')


@app.route('/tables.html')
def tables():
    return render_template('tables.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))


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
    app.run(host='127.0.0.1', port=8080, debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    # [END gae_flex_quickstart]
