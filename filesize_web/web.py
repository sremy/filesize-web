from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>Here, Simple file size API"


@app.route('/filesize')
def human_filesize_parameter():
    filesize = request.args.get('size', '')
    return str(filesize)


@app.route('/filesize/<int:filesize>')
def human_filesize(filesize):
    return str(filesize)

