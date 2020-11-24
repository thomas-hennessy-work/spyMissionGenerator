from flask import flask
import requests
app = Flask(__name__)
api = 'http://localhost:5001'

@app.route('/')
def index():
    return("information")