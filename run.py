import os
from flask import Flask, render_template, request

app = Flask(__name__)

# username_set = {'AB', 'BC', 'CD'}

@app.route('/', methods=['GET','POST'])
def index():
    allusers = ""
    username = ""
    if request.method == 'POST':
        if 'register' in request.form:
            with open("data/users.txt", "r") as readusernames:
                allusers = readusernames.read()
                username = request.form['username']
                if username in allusers:
                    return render_template("index.html", username="username already exist try another one")
                else:
                    with open("data/users.txt", "a") as addusernames:
                        addusernames.write(username + "\n")
                        allusers += (username)
                    # username_set.add(username)
                    return render_template("index.html", username=username, allusers=allusers)
                
        elif 'login' in request.form:
            with open("data/users.txt", "r") as readusernames:
                username = "Please register first"
                userlist = readusernames.read()
            return render_template("index.html", username=username, allusers= userlist)
        
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    # return render_template("index.html", username=username, allusers=username_set)
    return render_template("index.html", username=username, allusers="")
    
    
@app.route('/halloffame')
def halloffame():
    # return "<h1>Riddle-Me-This Application</h1><h2>Hall of Fame</h2>"
    return render_template("halloffame.html")
    
@app.route('/about')
def about():
    # return "<h1>Riddle-Me-This Application</h1><h2>About</h2>"
    return render_template("about.html")
    
@app.route('/contact')
def contact():
    # return "<h1>Riddle-Me-This Application</h1><h2>Contact</h2>"
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
