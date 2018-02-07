# ps_json
Experimenting with json

# Use this code for extracting information from 2 json files
# These json files appear as a downloadable csv (https://github.com/pricesearcher-code-tests/python-software-developer/blob/master/products.csv.gz)
# And a json file located in a AWS S3 bucket (https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json)

# The code needs the csv file in the same folder it is run and named "products.csv"
# The code automatically links to the AWS S3 bucket link

# Run the code and when asked enter an ID and if it exists in either of the files a json file (output.json) will be created
# The created json file will contain id, name, brand, retailer, price, in_stock
