import pandas as pd
import numpy as np

class PriceFinder:

    __all__= ["one_chain","all_chains", "__init__","__str__"]

# CONFIGURING DATA
#------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):

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
        self.chain_collection = [arbys, bk, bojangles, canes, cfa, deltaco, dominos, fiveguys, kfc, littlecaesars, mcdonalds, papajohns, pizzahut, popeyes, sonic, steaknshake, tacobell, wendys, zaxbys ]

        self.chain_collection_list= ["arbys", "bk", "bojangles", "canes", "cfa", "deltaco", "dominos", "fiveguys", "kfc", "littlecaesars", "mcdonalds", "papajohns", "pizzahut", "popeyes", "sonic", "steaknshake", "tacobell", "wendys", "zaxbys"]

        # creating list of options the user will be able to choose from
        self.foods = [ 'nugget','finger', 'burger', 'chicken sandwhich', 'chicken sandwich', 'fries', 'salads', 'pizza', 'tacos', 'tacos', 'burritos', 'nachos', 'breadsticks' ]
        self.beverages = [ 'soft drink', 'bottled water', 'lemonade', 'sweet tea' ]
        self.desserts = [ 'milkshakes', 'cookies']


    # __str__ function to return the collection of dataframes within the chain_collection
    def __str__(self):
        return "The fast-food chains included in this class: " + self.chain_collection_list

# FUNCTIONS TO CHOOSE DATA 
#------------------------------------------------------------------------------------------------------------------------------------
    
    # function to return cheapest prices from only ONE chain
    # i.e. cheapest desired combination for CFA
    def one_chain(self, chain, options):

        # self is taken from our class (this contains all chain dataframes)
        # chain is a STRING of the specific fast-food chain the user selected to find the cheapest prices for 
        # options is a LIST of STRINGS containing all of the user's picks 
        
        # finding the index for the chain the user selected in the chain_collection
        for i, item in enumerate(self.chain_collection_list):
            if item == chain:
                index = i
                break
        
        # grabbing the dataframe for the chosen resturant
        df = self.chain_collection[index]

        # removing any 'meal' or 'combo' items (we are going to make own combos!)
        df = df[~df['Food'].str.contains('combo', case=False, na=False)]
        df = df[~df['Food'].str.contains('meal', case=False, na=False)]
        df = df[~df['Type'].str.contains('combo', case=False, na=False)]
        df = df[~df['Type'].str.contains('meal', case=False, na=False)]

        # finding all the desired food
        for i, item in enumerate(options):
            # using a mask to filter through the dataframe to choose only what the user picked
            mask = df['Food'].str.contains(item, case=False, na=False) # filtering out desired food type using a mask
            options[i] = df[mask] # replacing item name in the list with the filtered df

        # this will return a list with all availabe menu items matching each option submitted 
        # Each index is a dataframe slice that corresponds with the index of the submitted option list  
        return options 




