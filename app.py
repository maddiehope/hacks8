# flask imports
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
import pandas as pd
from flask_cors import CORS
import sqlite3
import os

# CONFIGURING DATA
#------------------------------------------------------------------------------------------------------------------------------------
# dataframe imports
import pandas as pd
import numpy as np

# reading all sets into pandas DataFrames
arbys = pd.read_csv("datasets/arbys.csv")
bk = pd.read_csv("datasets/bk.csv")
bojangles = pd.read_csv("datasets/bojangles.csv")
canes = pd.read_csv("datasets/canes.csv")
cfa = pd.read_csv("datasets/cfa.csv")
deltaco = pd.read_csv("datasets/deltaco.csv")
dominos = pd.read_csv("datasets/dominos.csv")
fiveguys = pd.read_csv("datasets/fiveguys.csv")
kfc = pd.read_csv("datasets/kfc.csv")
littlecaesars = pd.read_csv("datasets/littlecaesars.csv")
mcdonalds = pd.read_csv("datasets/mcdonalds.csv")
papajohns = pd.read_csv("datasets/papajohns.csv")
pizzahut = pd.read_csv("datasets/pizzahut.csv")
popeyes = pd.read_csv("datasets/popeyes.csv")
sonic = pd.read_csv("datasets/sonic.csv")
steaknshake = pd.read_csv("datasets/steaknshake.csv")
tacobell = pd.read_csv("datasets/tacobell.csv")
wendys = pd.read_csv("datasets/wendys.csv")
zaxbys = pd.read_csv("datasets/zaxbys.csv")

# creating an iterable list of all the dataframes
chain_collection = [arbys, bk, bojangles, canes, cfa, deltaco, dominos, fiveguys, kfc, littlecaesars, mcdonalds, papajohns, pizzahut, popeyes, sonic, steaknshake,
                    tacobell, wendys, zaxbys ]


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