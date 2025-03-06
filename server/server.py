from flask import Flask
import json

app = Flask(__name__)

# This is an endpoint 
@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/about")
def about():
    return "Hello from the about page"

@app.get("/info")
def info():
    name = {"name":"Adrian RA"}
    return json.dumps(name)


app.run(debug=True)#This pass the changes to the server when we save