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


        # creating a list of all the food_select values 
        select_items = [food_select1, food_select2, food_select3, food_select4, food_select5]

        # removing the select items if they are "none"
        for i in range(4):
            if select_items[i] == None:
                del select_items[i]

        if chain_select != "chain_collection":
            selection = pricefinder.one_chain(chain_select, select_items)
            df = pd.DataFrame(selection) 

        elif chain_select == "chain_collection":
            selections = pricefinder.all_chain(select_items)
            df = pd.DataFrame(selections) 
            
        
        for i, items in enumerate(select_items):
            df[items + "(size)"] = df.apply(lambda x: str(x[i+1]) + " (" + str(x[4-i]) + ")" if x[i+1] and x[4-i] else '', axis=1)
            df = df.drop(columns = [items], axis = 1)
    
        df = df.drop(columns = ['Size', 'Type'], axis =1)
        df = df.fillna('')

        # replace all instances of nan (aesthetics)
        df = df.applymap(lambda x: x.replace('nan', 'none') if isinstance(x, str) else x)

        substring = 'none ('

        def remove_substring(x):
            if isinstance(x, str) and substring in x:
                return False
            return True

        df = df[df.applymap(remove_substring).all(axis=1)]

        df = df.set_index('chain')
        df = df.assign(**{df.columns[0]: df.pop(df.columns[0]).shift(-1)})


    # create error function in case user forgets to make any food selections
    except:
        return error()

    # once this process is done, the user is returned to the home page 
    return render_template("postdata.html",df=df,title="Prices")

# error function 
@app.route('/error', methods=['POST'])
def error():
    return render_template("error.html", title="Error")


#run statement 
app.run(debug=True, port=8080) 