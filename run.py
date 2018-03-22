import os
from flask import Flask, render_template, request

app = Flask(__name__)

# username_set = {'AB', 'BC', 'CD'}

@app.route('/', methods=['GET','POST'])
def index():
    allusers = ""
    username = ""
    if request.method == 'POST':
        username = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            allusers = readusernames.read()
        if 'register' in request.form:
            return render_template("register.html",register="",check_active="", register_active="btn-deactivated", username="", allusers="")
                
        elif 'login' in request.form:
            if username == "":
                return render_template("index.html", username="Enter a username to log in", allusers=allusers)
            elif username in allusers:
                username += " LOGGED IN"
                return render_template("index.html", username=username, allusers=allusers)
            else:
                username = "That username does not exist. Please register first."
            return render_template("index.html", username=username, allusers=allusers)
        
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    # return render_template("index.html", username=username, allusers=username_set)
    return render_template("index.html", username=username, allusers="")
    
@app.route('/register', methods=['GET','POST'])
def register():
    allusers = ""
    username = ""
    if request.method == 'POST':
        username = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            allusers = readusernames.read()
        if 'check' in request.form:
            if username in allusers:
                return render_template("register.html", register="", register_active="btn-deactivated", check_active="", username_feedback="username already exist try another one")
            else:
                return render_template("register.html", register="register", register_active="", check_active="btn-deactivated", username_feedback="Username available. Please click the register button.", username=username)
                    
        if 'register' in request.form:
            with open("data/users.txt", "a") as addusernames:
                addusernames.write(username + "\n")
                allusers += (username)
            # username_set.add(username)
            # return render_template("register.html", register="register", username_feedback="Username added. You can now log in.", allusers=allusers)
            # return render_template("register.html", register="register", username_feedback="Username added. You can now log in.",username=username, allusers=allusers)
            # Go back to index as registered for now. Later I will redirect to user page.
            return render_template("index.html", register="register", username_feedback="Username added. You can now log in.",username=username, allusers=allusers)

        elif 'login' in request.form:
            if username == "":
                return render_template("index.html", username="Enter a username to log in", allusers=allusers)
            elif username in allusers:
                username += " LOGGED IN"
                return render_template("index.html", username=username, allusers=allusers)
            else:
                username = "That username does not exist."
            return render_template("index.html", username=username, allusers=allusers)
        
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    # return render_template("index.html", username=username, allusers=username_set)
    return render_template("register.html", username=username, allusers="", username_feedback=" Enter a username")
    
    
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
