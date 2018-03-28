import os
import json
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app_info = {
    "logged": False,
    "username": "",
    "allusers": "",
    "register": "",         # ???
    "check_active": "",     # Pass class for check button
    "register_active": "",  # Pass class for register button
    "route": "",            # Which is the current page
    "game": False           # Is there a current game active True/False
}
current_game = []           # 
current_riddle = 0
all_riddles = []            # All riddles available for the game
riddle_counter = 0
attempt = 1                 # There are three attempts per riddle.
points = 10
gained_points = 0


# logged = False
# allusers = ""
# username = ""

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # global logged
    # global username
    # global allusers
    global app_info
    if request.method == 'POST':
        # logged = False
        # username = ""
        # allusers = ""
        app_info["logged"] = False
        app_info["username"] = ""
        app_info["allusers"] = ""
        app_info["game"] = False
        return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    # global logged
    # global username
    # global allusers
    global app_info
    try:
        if request.method == 'POST':
            # username = request.form['username']
            app_info["username"] = request.form['username']
            with open("data/users.txt", "r") as readusernames:
                # allusers = readusernames.read()
                app_info["allusers"] = readusernames.read()
            if 'register' in request.form:
                app_info["logged"] = False
                app_info["username"] = ""
                app_info["allusers"] = ""
                app_info["register"] = ""
                app_info["check_active"] = ""
                app_info["register_active"] = "btn-deactivated"
                app_info["route"] = "register"
                # return render_template("register.html", register="", check_active="", register_active="btn-deactivated", username="", allusers="", route="register")
                # return render_template("register.html", app_info=app_info)
                return redirect(url_for('register'))
                 
            elif 'login' in request.form:
                # if username == "":
                #     allusers = ""
                #     logged = False
                #     username = "Enter a username to log in"
                if app_info["username"] == "":
                    app_info["allusers"] = ""
                    app_info["logged"] = False
                    app_info["username"] = "Enter a username to log in"
                # elif username in allusers:
                #     username += " LOGGED IN"
                #     logged = True
                #     # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user")
                #     return redirect(url_for('user'))
                elif app_info["username"] in app_info["allusers"]:
                    # username += " LOGGED IN"
                    app_info["logged"] = True
                    # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user")
                    return redirect(url_for('user'))
                # else:
                #     username = "That username does not exist. Please register first."
                #     logged = False
                else:
                    app_info["username"] = "That username does not exist. Please register first."
                    app_info["logged"] = False
                    
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"
       
    # return render_template("index.html", username=username, allusers=allusers, logged=logged, route="index")
    app_info["route"] = "index"
    return render_template("index.html", app_info=app_info)
    
@app.route('/register', methods=['GET','POST'])
def register():
    # global logged
    # global username
    # global allusers
    global app_info
    if request.method == 'POST':
        app_info["username"] = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            app_info["allusers"] = readusernames.read()
        if 'check' in request.form:
            if app_info["username"] in app_info["allusers"]:
                app_info["register"] = ""
                app_info["register_active"] = "btn-deactivated"
                app_info["check_active"] = ""
                username_feedback = "username already exist try another one"
            else:
                app_info["register"] = "register"
                app_info["register_active"] = ""
                app_info["check_active"] = "btn-deactivated"
                username_feedback = "Username available. Please click the register button."
            # return render_template("register.html", register=register, register_active=register_active, check_active=check_active, username_feedback=username_feedback, username=username, route="register")
            return render_template("register.html",app_info=app_info, username_feedback=username_feedback)
            
        if 'register' in request.form:
            with open("data/users.txt", "a") as addusernames:
                addusernames.write(app_info["username"] + "\n")
                app_info["allusers"] += (app_info["username"])
                app_info["logged"] = True
            # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user")
            return redirect(url_for('user'))

    # return render_template("register.html", username=username, allusers="", username_feedback=" Enter a valid username.", route="register")
    app_info["register"] = "register"
    app_info["allusers"]=""
    username_feedback="Enter a valid username."
    # return render_template("register.html", allusers="", username_feedback=" Enter a valid username.", route="register")
    return render_template("register.html", app_info=app_info)

@app.route('/user', methods=['GET', 'POST'])
def user():
    # global logged
    # global username
    # global allusers
    global app_info
    global current_game
    global current_riddle
    global all_riddles
    global riddle_counter
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
    
    if app_info["game"] == False:  # RESET
        current_game = []
        current_riddle = 0
        all_riddles = []
        riddle_counter = 0
        
    # return render_template("user.html", username=username, allusers=allusers, logged=logged, route="user", user_data=user_data)
    app_info["route"] = "user"
    return render_template("user.html", app_info=app_info, user_data=user_data)

@app.route('/halloffame')
def halloffame():
    # global logged
    # global username
    # global allusers
    global app_info
    best_individual_games = [
            (1, "20/3/2018", "AB", 72),
            (2, "21/3/2018", "BC", 63),
            (3, "17/3/2018", "DE", 60),
            (4, "15/3/2018", "AB", 56),
            (5, "16/3/2018", "CD", 54),
            (6, "16/3/2018", "BC", 50),
            (7, "17/3/2018", "AB", 48),
            (8, "14/3/2018", "FDG", 34)]
    best_all_games = [
            (1, "AB", 890),
            (2, "BC", 825),
            (3, "DE", 710),
            (4, "CD", 700),
            (5, "CDDF", 540),
            (6, "BCOE", 500),
            (7, "ABDF", 480),
            (8, "FDG", 450),
            (9, "OFDG", 420),
            (10, "AFFDG", 410)]
    app_info["route"] = "halloffame"
    # return render_template("halloffame.html", username=username, allusers=allusers, logged=logged, route="halloffame", best_individual_games=best_individual_games, best_all_games=best_all_games)
    return render_template("halloffame.html", app_info=app_info, best_individual_games=best_individual_games, best_all_games=best_all_games)
    
@app.route('/about')
def about():
    # global logged
    # global username
    # global allusers
    global app_info
    app_info["route"] = "about"
    # return render_template("about.html", username=username, allusers=allusers, logged=logged, route="about")
    return render_template("about.html", app_info=app_info)
    
@app.route('/contact')
def contact():
    # global logged
    # global username
    # global allusers
    global app_info
    app_info["route"] = "contact"
    # return render_template("contact.html", username=username, allusers=allusers, logged=logged, route="contact")
    return render_template("contact.html", app_info=app_info)

def set_current_riddle(data):
    ordered_data = [0,0,0]
    for cr in data:
        if cr[0] == "id":
            ordered_data[0] = cr[1]
        elif cr[0] == "source":
            ordered_data[1] = cr[1]
        elif cr[0] == "answer":
            ordered_data[2] = ''.join(list(cr[1]))
    return ordered_data

@app.route('/game', methods=['GET', 'POST'])
def game():
    global app_info
    global all_riddles
    global current_game
    global current_riddle
    global riddle_counter
    global attempt
    global points
    global gained_points
    
    app_info["route"] = "game"  # I will need this to control the menu
    
    # current_riddle += 1
    this_riddle = current_game  # What is this for??????????????????????????????
    
    if app_info["game"] == False:
        app_info["game"] = True  # Game On
        # Read data from json and store them locally
        with open("data/riddles.json", "r") as all_riddles_json:
            all_riddles = json.load(all_riddles_json)
        
        for x in range(0, 5):
            # Randomly select 5 riddles - Later this will be 10 from a larger pool.
            
            repeat = True
            while repeat:
                choose_game=random.choice(all_riddles)
                # print choose_game.items()
                if choose_game.items() not in current_game:
                    repeat = False
                
            current_game.append(choose_game.items())
            # choose_game = random.choice(all_riddles)
            # print choose_game.items()
            # if choose_game.items() not in current_game:
            #     current_game.append(choose_game.items())
        
        # current_riddle = current_game[riddle_counter]
        current_riddle = set_current_riddle(current_game[riddle_counter])
            
    if request.method == 'POST':
        if 'play' in request.form:
            points = 10
            attempt = 1
            
            
            
            
            
        elif 'answer_btn' in request.form:
            # Check Answer
            
            if attempt == 1:
                answer = request.form['answer_text']
                if answer == current_riddle[2]:
                    gained_points += 10
                    attemp = 1

                    riddle_counter += 1
                    if riddle_counter > len(current_game)-1:
                        # app_info["game"] = False
                        # return "<h1>Gama OVER</h1>"
                        return redirect(url_for('game_over'))
                    # current_riddle = current_game[riddle_counter]
                    # ordered_data = [0,0,0]
                    # for cr in current_riddle:
                    #     if cr[0] == "id":
                    #         ordered_data[0] = cr[1]
                    #     elif cr[0] == "source":
                    #         ordered_data[1] = cr[1]
                    #     elif cr[0] == "answer":
                    #         ordered_data[2] = ''.join(list(cr[1]))
                    #         # Need to unpack the tuple with the answer into a list.
                            
                    # current_riddle = ordered_data
                    current_riddle = set_current_riddle(current_game[riddle_counter])
            
            
                #If I guess the answer set points to 10
                #I still need to add code to check the answer
            # if True:
            #     points = 10
            #     attempt = 1
            # elif False:
            #     attempt += 1
            #     if attempt == 2:
            #         points = 6
            #     elif attempt == 3:
            #         points = 2
            elif attempt == 2:
                # Get all words and concatenate them
                answer = ""
                for ndx, each_word in current_riddle[2]:
                    index = 'answer_text' + ndx
                    answer += (request.form['index'] + " ")
                    
                    if answer == current_riddle[2]:
                        gained_points += 6
                        attemp = 1
    
                        riddle_counter += 1
                        if riddle_counter > len(current_game)-1:
                            return redirect(url_for('game_over'))

                        current_riddle = set_current_riddle(current_game[riddle_counter])
                    
                    else:
                
                
                
                CONTINUE FROM HERE
                _________________________________________
                
                
                
                
                
                
                
                
                attempt += 1
                if attempt == 2:
                    points = 6
                elif attempt == 3:
                    points = 2
                
        
        #This will happen if the answer is wrong Or pass
        # increase attempt
        elif 'pass_btn' in request.form:
            attempt += 1
            if attempt == 2:
                points = 6
            elif attempt == 3:
                points = 2
                if riddle_counter > len(current_game)-1:
                    return redirect(url_for('game_over'))
                # current_riddle = current_game[riddle_counter] #This code is changing
                current_riddle = set_current_riddle(current_game[riddle_counter])
            elif attempt == 4:
                points = 10
                attempt = 1
                riddle_counter += 1
                # Call next riddle
                if riddle_counter > len(current_game)-1:
                    # Store the gained_points
                    
                    # Reset gained_points
                    gained_points = 0
                    return redirect(url_for('game_over'))
                #current_riddle = current_game[riddle_counter] #This code is changing
                current_riddle = set_current_riddle(current_game[riddle_counter])
                
                
                

    
    
    # return "<h2>Here " + username + " will play the game.</h2>"
    # return render_template("game.html", username=username, allusers=allusers, logged=logged, route="game") #, user_data=user_data)
    return render_template("game.html", app_info=app_info, all_riddles=all_riddles, current_game=current_game, current_riddle=current_riddle, riddle_counter=riddle_counter+1, attempt=attempt, points=points, gained_points=gained_points)

@app.route('/game_over')
def game_over():
    global app_info
    global all_riddles
    global current_game
    global current_riddle
    global riddle_counter
    app_info["route"] = "game"
    app_info["game"] = False
    current_game = []
    current_riddle = 0
    all_riddles = []
    riddle_counter = 0
    # return "<h1>Gama OVER</h1>"
    return redirect(url_for('user'))
    
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
