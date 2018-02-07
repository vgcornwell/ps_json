import requests       # Import requests for downloading products.json
import re             # Import re for removing unwanted punctuation from csv
import pandas         # Import pandas for extracting columns from csv
import json           # Import json to create json files

df = pandas.read_csv('products.csv')        # Read products.csv
Id = df['Id']                               # Extract Id column
Na = df[' Name']                            # Extract Name column
Br = df[' Brand']                           # Extract Brand column
Re = df[' Retailer']                        # Extract Retailer column
Pr = df[' Price']                           # Extract Price column
In = df[' InStock']                         # Extract In Stock column

T = raw_input('Enter ID: ')                 # Allow user to input ID

i = 0

while i < len(Id):
    if T == str(Id[i]):                                 # See if T matches ID row i
        ID = Id[i]                                      # Set ID to mathced ID                
        if Na[i] == ' ""':                              # If name is empty, set NA to None (in Python) = null (in json)
            NA = None
        else:
            NA = (re.sub(r'[ \"]','',Na[i]))            # If name isn't empty, reomve unwanted punctuation
        if Br[i] == ' ""':
            BR = None
        else:
            BR = (re.sub(r'[ \"]','',Br[i]))           
        if Re[i] == ' ""':
            RE = None
        else:
            RE = (re.sub(r'[ \"]','',Re[i]))
        if Pr[i] == ' ""':
            PR = None
        else:
            PR = float(re.sub(r'[ \"]','',Pr[i]))       # If price isn't empty, remove unwanted punctuation and set as float
        if In[i] == ' ""':
            IN = None
        else:       
            IN = "y" in In[i]                           # If in stock isn't empty, booliean for "y" (which will appear in "y" or "yes")
        
        j = i
        break                                           # Break so we don't iterate any further (because we have assumed all IDs are unique)
    else:
        i = i + 1                                       # If ID =/= id[i] increase counter and repeat

# Set the product.json second as it is more time consuming

if i == len(Id):
    r = requests.get('https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json')

    dat = r.json()

    k = 0

    while k < len(dat):
        if T == dat[k]["id"]:                   # Note: this is same as above loop
            ID = dat[k]["id"]
            
            if dat[k]["name"] == "":
                NA = None
            else:
                NA = dat[k]["name"]
            if dat[k]["brand"] == "":
                NA = None
            else:
                BR = dat[k]["brand"]
            if dat[k]["retailer"] == "":
                NA = None
            else:
                RE = dat[k]["retailer"]
            if dat[k]["price"] == "":
                PR = None
            elif dat[k]["price"] == None:
                PR = None
            else:
                PR = float(dat[k]["price"])
                
            if dat[k]["in_stock"] == "":
                IN = None
            elif dat[k]["in_stock"] == False:               # Added True and False as products.json keeps this information unlike products.csv
                IN = False
            elif dat[k]["in_stock"] == True:
                IN = True
            else:
                IN = "y" in dat[k]["in_stock"]

            l = k
            break
        else:
            k = k + 1

data = {
        'id' : str(ID),             # Set ID in json
        'name' : NA,                # Set Name in json
        'brand' : BR,               # Set Brand in json
        'retailer' : RE,            # Set Retailer in json
        'price' : PR,               # Set Price in json
        'in_stock' : IN             # Set In Stock in json
        }

json_str = json.dumps(data, sort_keys=True)     # Dump the json data

with open('output.json', 'w') as outfile:                       # Create output.json
    json.dump(data, outfile, sort_keys = True, indent = 4)      # Dump in desired format

