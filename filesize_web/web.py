from flask import Flask
from flask import request
from archivesize.filesize import human_size

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>Here, Simple file size API"


@app.route('/filesize')
def human_filesize_parameter():
    filesize = int(request.args.get('size', '0'))
    return str(human_size(filesize))


@app.route('/filesize/<int:filesize>')
def human_filesize(filesize):
    return str(human_size(filesize))

