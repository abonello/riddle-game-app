import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
logged = False
allusers = ""
username = ""

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global logged
    global username
    global allusers
    if request.method == 'POST':
        logged = False
        username = ""
        allusers = ""
        return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    global logged
    global username
    global allusers
    try:
        if request.method == 'POST':
            username = request.form['username']
            with open("data/users.txt", "r") as readusernames:
                allusers = readusernames.read()
            if 'register' in request.form:
                return render_template("register.html", register="", check_active="", register_active="btn-deactivated", username="", allusers="", route="register")
                    
            elif 'login' in request.form:
                if username == "":
                    allusers = ""
                    logged = False
                    username = "Enter a username to log in"
                elif username in allusers:
                    username += " LOGGED IN"
                    logged = True
                    # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user")
                    redirect(url_for('user'))
                else:
                    username = "That username does not exist. Please register first."
                    logged = False
                    
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"
        
    return render_template("index.html", username=username, allusers=allusers, logged=logged, route="index")
    
@app.route('/register', methods=['GET','POST'])
def register():
    global logged
    global username
    global allusers
    if request.method == 'POST':
        username = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            allusers = readusernames.read()
        if 'check' in request.form:
            if username in allusers:
                register=""
                register_active="btn-deactivated"
                check_active=""
                username_feedback="username already exist try another one"
            else:
                register="register"
                register_active=""
                check_active="btn-deactivated"
                username_feedback="Username available. Please click the register button."
            return render_template("register.html", register=register, register_active=register_active, check_active=check_active, username_feedback=username_feedback, username=username, route="register")
            
        if 'register' in request.form:
            with open("data/users.txt", "a") as addusernames:
                addusernames.write(username + "\n")
                allusers += (username)
                logged = True
            # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user")
            redirect(url_for('user'))

    return render_template("register.html", username=username, allusers="", username_feedback=" Enter a valid username.", route="register")

@app.route('/user')
def user():
    global logged
    global username
    global allusers
    user_data = {
        "number_of_games" : 5,
        "date_best_game" : "15/3/2018",
        "points_best_game" : 56,
        "total_user_points" : 340,
        "games_played": [
            ("17/3/2018", 48),
            ("16/3/2018", 50),
            ("16/3/2018", 54),
            ("15/3/2018", 56),
            ("14/3/2018", 34)]
    }
    return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user", user_data=user_data)

@app.route('/halloffame')
def halloffame():
    global logged
    global username
    global allusers
    return render_template("halloffame.html", username=username, allusers=allusers, logged=logged, route="halloffame")
    
@app.route('/about')
def about():
    global logged
    global username
    global allusers
    return render_template("about.html", username=username, allusers=allusers, logged=logged, route="about")
    
@app.route('/contact')
def contact():
    global logged
    global username
    global allusers
    return render_template("contact.html", username=username, allusers=allusers, logged=logged, route="contact")
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
