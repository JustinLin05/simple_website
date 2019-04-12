from flask import Flask, jsonify, render_template, request
from werkzeug import secure_filename
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def hello_flask():
	return 'hello flask'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route('/api/hello-world', methods=['GET'])
def say_hello():
	resObj = {
		'content': 'Hello, flask-react'
	}
	return jsonify(resObj)

app.run(host='0.0.0.0', port=80)
