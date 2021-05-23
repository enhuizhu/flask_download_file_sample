from flask import Flask, render_template, send_from_directory
from .services.fileService import get_files_from_dir
import os
from pprint import pprint

app = Flask(__name__)

@app.route('/videos')
def index():
  videoPath = os.path.dirname(os.path.abspath(__file__)) + '/data'
  files = get_files_from_dir(videoPath)
  pprint(files)
  return render_template('index.html', test = "hello, the world", files = files)

@app.route('/videos/<path:path>')
def get_file(path):
  videoPath = os.path.dirname(os.path.abspath(__file__)) + '/data'
  return send_from_directory(videoPath, path,  as_attachment=True)
