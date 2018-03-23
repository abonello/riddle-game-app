import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# username_set = {'AB', 'BC', 'CD'}
logged = False
allusers = ""
username = ""

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global logged
    global username
    global allusers
    if request.method == 'POST':
        # return "<h1>Logout</h1>"
        # return render_template("index.html", username="", allusers="", logged=False)
        logged = False
        username = ""
        allusers = ""
        return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    # allusers = ""
    # username = ""
    global logged
    global username
    global allusers
    # console.log(request.from[])
    try:
        if request.method == 'POST':
            username = request.form['username']
            with open("data/users.txt", "r") as readusernames:
                allusers = readusernames.read()
            if 'register' in request.form:
                return render_template("register.html", register="",check_active="", register_active="btn-deactivated", username="", allusers="")
                    
            elif 'login' in request.form:
                if username == "":
                    allusers = ""
                    logged = False
                    username = "Enter a username to log in"
                    # return render_template("index.html", username="Enter a username to log in", allusers=allusers, logged=False)
                elif username in allusers:
                    username += " LOGGED IN"
                    logged = True
                    # return render_template("index.html", username=username, allusers=allusers, logged=logged)
                else:
                    username = "That username does not exist. Please register first."
                    logged = False
                # return render_template("index.html", username=username, allusers=allusers, logged=logged)
                
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"
        
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    # return render_template("index.html", username=username, allusers=username_set)
    # return render_template("index.html", username=username, allusers=allusers, logged=False)
    return render_template("index.html", username=username, allusers=allusers, logged=logged)
    
@app.route('/register', methods=['GET','POST'])
def register():
    # allusers = ""
    # username = ""
    global logged
    global username
    global allusers
    if request.method == 'POST':
        username = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            allusers = readusernames.read()
        if 'check' in request.form:
            if username in allusers:
                return render_template("register.html", register="", register_active="btn-deactivated", check_active="", username_feedback="username already exist try another one", username=username)
            else:
                return render_template("register.html", register="register", register_active="", check_active="btn-deactivated", username_feedback="Username available. Please click the register button.", username=username)
                # return render_template("register.html", register="register", register_active="", check_active="btn-deactivated", username_feedback="Username available. Please click the register button.", username="")
  
        if 'register' in request.form:
            with open("data/users.txt", "a") as addusernames:
                addusernames.write(username + "\n")
                allusers += (username)
                logged = True
            # username_set.add(username)
            # return render_template("register.html", register="register", username_feedback="Username added. You can now log in.", allusers=allusers)
            # return render_template("register.html", register="register", username_feedback="Username added. You can now log in.",username=username, allusers=allusers)
            # Go back to index as registered for now. Later I will redirect to user page.
            # return render_template("index.html", register="register", username_feedback="Username added. You can now log in.",username=username, allusers=allusers, logged="True")
            return render_template("index.html", register="register", username_feedback="Username added. You can now log in.",username=username, allusers=allusers, logged=logged)

        # elif 'login' in request.form:
        #     if username == "":
        #         return render_template("index.html", username="Enter a username to log in", allusers=allusers)
        #     elif username in allusers:
        #         username += " LOGGED IN"
        #         return render_template("index.html", username=username, allusers=allusers)
        #     else:
        #         username = "That username does not exist."
        #     return render_template("index.html", username=username, allusers=allusers)
        
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    # return render_template("index.html", username=username, allusers=username_set)
    return render_template("register.html", username=username, allusers="", username_feedback=" Enter a valid username.")

@app.route('/halloffame')
def halloffame():
    global logged
    global username
    global allusers
    # return "<h1>Riddle-Me-This Application</h1><h2>Hall of Fame</h2>"
    return render_template("halloffame.html", username=username, allusers=allusers, logged=logged)
    
@app.route('/about')
def about():
    global logged
    global username
    global allusers
    # return "<h1>Riddle-Me-This Application</h1><h2>About</h2>"
    return render_template("about.html", username=username, allusers=allusers, logged=logged)
    
@app.route('/contact')
def contact():
    global logged
    global username
    global allusers
    # return "<h1>Riddle-Me-This Application</h1><h2>Contact</h2>"
    return render_template("contact.html", username=username, allusers=allusers, logged=logged)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
