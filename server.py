from flask import Flask, request, abort

app = Flask(__name__,static_url_path='')#change the directory of static files

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return app.send_static_file('index.html')#"index.html" under the folder "static"

@app.errorhandler(404)
def page_not_found(error):
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)#open "http://localhost:5000" to see the index page
	# app.run(debug=True)