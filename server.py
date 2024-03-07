from flask import Flask

app = Flask(__name__) #__name__ < use name of the folder

@app.get("/")
def home():
    return "Hello from Flask!"


app.run(debug = True) # apply the changes on the code live

# test