# flask imports
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
import pandas as pd
from flask_cors import CORS
import sqlite3
import os

# CREATING FLASK APP
#------------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__, template_folder='templates')
CORS(app)

# creating the "Home" page for route "/"
@app.route('/', methods=['GET'])
def selection():
    return render_template("home.html",title="Home") # will return the "home.html" template, i.e. the selection menu


#run statement 
app.run(debug=True, port=8080) 