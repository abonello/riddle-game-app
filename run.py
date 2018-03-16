import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    
@app.route('/halloffame')
def halloffame():
    return "<h1>Riddle-Me-This Application</h1><h2>Hall of Fame</h2>"
    
@app.route('/about')
def about():
    return "<h1>Riddle-Me-This Application</h1><h2>About</h2>"
    
@app.route('/contact')
def contact():
    return "<h1>Riddle-Me-This Application</h1><h2>Contact</h2>"
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
