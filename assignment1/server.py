from flask import Flask, request, Response, url_for
import rocksdb
import uuid
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = '/usr/src/myapp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/scripts", methods=['POST'])
def script_uploader():
	db = rocksdb.DB("lab1.db", rocksdb.Options(create_if_missing=True))

	if request.method == 'POST':
    	# check if the post request has the file part
		if 'data' not in request.files:
			return "No File data"
		else:
			key = uuid.uuid4().hex
			file = request.files['data']
			filename = file.filename
			file_path = UPLOAD_FOLDER+'/'+key
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], key))
			# You should use os.path.join here too.
			#with open(UPLOAD_FOLDER+'/'+filename) as f:
			#	file_content = f.read()
			#	print(file_content)
			#print(url_for('uploaded_file',filename=filename))
			db.put(key.encode(), file_path.encode())
			return Response("{'script-id': %s}" % key, status=201, mimetype='application/json')
	return "V1/script"

@app.route("/api/v1/scripts/test")
def test():
	#os.system('python %s' % (UPLOAD_FOLDER+'/'+'foo.py'))
	result = subprocess.run(['python3', UPLOAD_FOLDER+'/'+'foo.py'], stdout=subprocess.PIPE)
	print(result.stdout)
	return Response(result.stdout, status=200)

@app.route('/api/v1/scripts/<script_id>')
def script_invoker(script_id):
	result = subprocess.run(['python3', UPLOAD_FOLDER+'/'+'foo.py'], stdout=subprocess.PIPE)
	return Response(result.stdout, status=200)

	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)