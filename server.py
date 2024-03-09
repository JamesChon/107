from flask import Flask, request
import json

app = Flask(__name__) #__name__ < use name of the folder

@app.get("/")
def home():
    return "Hello from Flask!"

@app.get("/testing")
def test():
    return "hello from another page"

# create 2 more API (about and blog)

@app.get("/about")
def about():
    me = {"name": "Chon"}
    return json.dumps(me)

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2", "build": 123456}
    return json.dumps(version)

#this time we need to read and write in to the server
products = []
@app.get("/api/products")
def get_products():

    return json.dumps(products)

@app.post("/api/products")
def save_products():
    products = request.get_json()
    print (products)
    products.append(products)
    return json.dumps(products)


app.run(debug = True) # apply the changes on the code live

# test

#API / Endpoints
#transform JSON / convert JSON in an object again