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
        self.foods = [ 'nugget','finger', 'burger', 'chicken sandwich', 'fries', 'salads', 'pizza', 'tacos', 'burritos', 'nachos', 'breadsticks' ]
        self.drinks = [ 'drink', 'bottled water', 'lemonade', 'sweet tea' ]
        self.desserts = [ 'milkshakes', 'cookies']


    # __str__ function to return the collection of dataframes within the chain_collection
    def __str__(self):
        #return "The fast food chains included in this class are: " + str(self.chain_collection_list)
        return f"The fast food chains used in this class are: {', '.join(str(i) for i in self.chain_collection_list)}"

        

# FUNCTIONS TO CHOOSE DATA 
#------------------------------------------------------------------------------------------------------------------------------------
    
    # ONE CHAIN FUNCTION
    #--------------------------------------------------------------
        # function to return cheapest prices from only ONE chain
        # i.e. cheapest desired combination for CFA

    def one_chain(self, chain, options):

        # self is taken from our class (this contains all chain dataframes)
        # chain is a STRING of the specific fast-food chain the user selected to find the cheapest prices for 
        # options is a LIST of STRINGS containing all of the user's picks 
        
        # finding the index for the chain the user selected in the chain_collection

        one_option = pd.DataFrame({'Type': [], 'Food': [], 'Size': [], 'Price':[]}) # will help us combine all menu items for the options for EVERY chain

        for i, item in enumerate(self.chain_collection_list):
            if item == chain:
                index = i
                break

        
        # grabbing the dataframe for the chosen resturant
        df = self.chain_collection[index]

        # removing any 'meal' or 'combo' items (we are going to make own combos!)
        df = df[~df['Food'].str.contains('combo', case=False, na=False)]
        df = df[~df['Food'].str.contains('meal', case=False, na=False)]
        df = df[~df['Food'].str.contains('upsize', case=False, na=False)]
        df = df[~df['Food'].str.contains('limited', case=False, na=False)]
        df = df[~df['Type'].str.contains('combo', case=False, na=False)]
        df = df[~df['Type'].str.contains('limited', case=False, na=False)]

        o = {} # dictionary that helps us collect the menu items for the options 

    # finding all the desired food
        for j, item in enumerate(options): # loops once through each item in the 'options' list 
        # finding all the desired food

        # using a mask to filter through the dataframe to choose only what the user picked
                if df['Food'].str.contains(item, case=False, na=False).any() == True: # making sure that the chain has a menu item for the user's option

                    slice = df[df['Food'].str.contains(item, case=False, na=False)] # filtering out desired food type using a mask
        
                    min_index = slice['Price'].idxmin()
                    min_row = df.loc[min_index]
                    o.update({self.chain_collection_list[i]+str(j): min_row})  # adding all menu items the chain has for the desired food and adding that slice to the o dictionary 

            
        this_chain = pd.DataFrame(o)
        this_chain = this_chain.transpose()

        one_option = pd.concat((one_option,this_chain))
 
        one_option = one_option.to_records(index=False) # converting to numpy array so it becomes hashable 
        return one_option


    # ALL CHAIN FUNCTION
    #--------------------------------------------------------------

    def all_chain(self, options):
        all_options = pd.DataFrame({'Type': [], 'Food': [], 'Size': [], 'Price':[]}) # will help us combine all menu items for the options for EVERY chain


        for i,chain in enumerate(self.chain_collection): # loops once over every restaurant dataframe in the chain_collection list 

            df = chain
            #print(chain_collection_list[i])

            # removing any 'meal' or 'combo' items (we are going to make own combos!)
            df = df[~df['Food'].str.contains('combo', case=False, na=False)]
            df = df[~df['Food'].str.contains('meal', case=False, na=False)]
            df = df[~df['Food'].str.contains('upsize', case=False, na=False)]
            df = df[~df['Food'].str.contains('limited', case=False, na=False)]
            df = df[~df['Type'].str.contains('combo', case=False, na=False)]
            df = df[~df['Type'].str.contains('limited', case=False, na=False)]

    
            o = {} # dictionary that helps us collect the menu items for the options 

            # finding all the desired food
            for j, item in enumerate(options): # loops once through each item in the 'options' list 
                #print(j)

                # using a mask to filter through the dataframe to choose only what the user picked
                if df['Food'].str.contains(item, case=False, na=False).any() == True: # making sure that the chain has a menu item for the user's option

                    #print(item)

                    slice = df[df['Food'].str.contains(item, case=False, na=False)] # filtering out desired food type using a mask
        
                    min_index = slice['Price'].idxmin()
                    min_row = df.loc[min_index]
                    o.update({self.chain_collection_list[i]+str(j): min_row})  # adding all menu items the chain has for the desired food and adding that slice to the o dictionary 

                    #print(o)
           
                this_chain = pd.DataFrame(o)
                this_chain = this_chain.transpose()
                #print(this_chain)

            all_options = pd.concat((all_options,this_chain)) 
 
        for i, item in enumerate(options):
            all_options[item] = all_options[all_options['Food'].str.contains(item, case=False, na=False)]['Food']

        all_options.drop(columns=['Food'], inplace=True)

        for i, item in enumerate(options):  
            all_options.insert(i, item, all_options.pop(item))

        all_options = all_options.reset_index()
        all_options = all_options.rename({'index': 'chain'}, axis=1) # taking the chain names out of the index and making them a seperate column

        all_options["chain"] = all_options["chain"].str.slice(stop=-1)

        for i, items in enumerate(options):
            all_options[items + "(size)"] = all_options.apply(lambda x: str(x[i+1]) + " (" + str(x['Size']) + ")" if x[i+1] and x['Size'] else '', axis=1)
            all_options = all_options.drop(columns = [items], axis = 1)
    
        all_options = all_options.drop(columns = ['Size', 'Type'], axis =1)

        all_options = all_options.applymap(lambda x: x.replace('nan', 'none') if isinstance(x, str) else x)


        #### unsure
        substring = 'none ('

        all_options = all_options[~all_options.applymap(lambda x: isinstance(x, str) and substring in x).any(axis=1)]

        all_options = all_options.set_index('chain')
        all_options = all_options.assign(**{all_options.columns[0]: all_options.pop(all_options.columns[0]).shift(-1)})
        all_options = all_options.reset_index()
        all_options = all_options.rename({'chain': 'Chain'}, axis=1)

        df.sort_values(by='Price', ascending=True, inplace=True)

        df = df.dropna()
        #### 
        
        all_options = all_options.to_records(index=False) # converting to numpy array so it becomes hashable 

        return all_options




