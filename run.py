import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
