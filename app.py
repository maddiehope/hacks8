# flask imports
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import requests
import pandas as pd
from flask_cors import CORS
import sqlite3
import os

# importing PriceFinder class
from pricefinder import *
pricefinder = PriceFinder()

# CREATING FLASK APP
#------------------------------------------------------------------------------------------------------------------------------------
app = Flask(__name__, template_folder='templates')
CORS(app)

# creating the "Home" page for route "/"
@app.route('/', methods=['GET'])
def selection():
    return render_template("home.html",title="Home") # will return the "home.html" template, i.e. the selection menu

# takes the data from user selection and passes it into the PriceFinder() functions
@app.route('/price', methods=['POST'])
def price():

    # tries to proceed how intended
    try: 
        # grabbing the variables from the form
        chain_select = request.form.get("chain-select")
        food_select1 = request.form.get("food-select1")
        food_select2 = request.form.get("food-select2")
        food_select3 = request.form.get("food-select3")
        food_select4 = request.form.get("food-select4")
        food_select5 = request.form.get("food-select5")

        #testing #took out required
        print(chain_select)
        print(food_select1)

        # creating a list of all the food_select values 
        select_items = [food_select1, food_select2, food_select3, food_select4, food_select5]

        if chain_select != "chain_collection":
            selection = pricefinder.one_chain(chain_select, select_items)
            df = pd.DataFrame(selection) 

        elif chain_select == "chain_collection":
            selections = pricefinder.all_chain(select_items)
            df = pd.DataFrame(selections) 

    # create error function in case user forgets to make any food selections
    except:
        return error()

    # once this process is done, the user is returned to the home page 
    return render_template("postdata.html",title="Prices")

# error function 
@app.route('/error', methods=['POST'])
def error():
    return render_template("error.html", title="Error")


#run statement 
app.run(debug=True, port=8080) 