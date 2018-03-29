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
wrong_answers =[]           # This will hold wrong answers
answer = ""                 # Current answer of current riddle


def global_game_reset():
    global current_game
    global current_riddle
    global all_riddles
    global riddle_counter
    global attempt
    global points
    global gained_points
    global wrong_answers         # This will hold wrong answers
    global answer                 # Current answer of current riddle

    current_game = []
    current_riddle = 0
    all_riddles = []
    riddle_counter = 0
    attempt = 1
    points = 10
    gained_points = 0
    wrong_answers =[]           # This will hold wrong answers
    answer = ""                 # Current answer of current riddle
    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global app_info
    # global attempt
    # global points
    # global gained_points
    # global riddle_counter
    # global wrong_answers
    if request.method == 'POST':    #RESET
        app_info["logged"] = False
        app_info["username"] = ""
        app_info["allusers"] = ""
        app_info["game"] = False
        # attempt = 1
        # points = 10
        # gained_points = 0
        # riddle_counter = 0
        # wrong_answers =[] 
        global_game_reset()
        return redirect(url_for('index'))

@app.route('/', methods=['GET','POST'])
def index():
    global app_info
    global attempt      #Needed only for debugging
    try:
        if request.method == 'POST':
            app_info["username"] = request.form['username']
            with open("data/users.txt", "r") as readusernames:
                app_info["allusers"] = readusernames.read()
            if 'register' in request.form:
                app_info["logged"] = False
                app_info["username"] = ""
                app_info["allusers"] = ""
                app_info["register"] = ""
                app_info["check_active"] = ""
                app_info["register_active"] = "btn-deactivated"
                app_info["route"] = "register"
                return redirect(url_for('register'))
                 
            elif 'login' in request.form:
                if app_info["username"] == "":
                    app_info["allusers"] = ""
                    app_info["logged"] = False
                    app_info["username"] = "Enter a username to log in"
                elif app_info["username"] in app_info["allusers"]:
                    app_info["logged"] = True
                    return redirect(url_for('user'))
                else:
                    app_info["username"] = "That username does not exist. Please register first."
                    app_info["logged"] = False
                    
    except Exception as e:
        return "<h1> Error: " + str(e) + "</h1>"
       
    app_info["route"] = "index"
    return render_template("index.html", app_info=app_info, attempt=attempt)
    
@app.route('/register', methods=['GET','POST'])
def register():
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
            return render_template("register.html",app_info=app_info, username_feedback=username_feedback)
            
        if 'register' in request.form:
            with open("data/users.txt", "a") as addusernames:
                addusernames.write(app_info["username"] + "\n")
                app_info["allusers"] += (app_info["username"])
                app_info["logged"] = True
            return redirect(url_for('user'))

    app_info["register"] = "register"
    app_info["allusers"]=""
    username_feedback="Enter a valid username."
    return render_template("register.html", app_info=app_info)

@app.route('/user', methods=['GET', 'POST'])
def user():
    global app_info
    global current_game
    global current_riddle
    global all_riddles
    global riddle_counter
    global attempt      #Needed only for debugging
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
        
    app_info["route"] = "user"
    return render_template("user.html", app_info=app_info, user_data=user_data, attempt=attempt)

@app.route('/halloffame')
def halloffame():
    global app_info
    best_individual_games = [
            (1, "20/3/2018", "AB", 72),
            (2, "21/3/2018", "BC", 63),
            (3, "17/3/2018", "DE", 60),
            (4, "15/3/2018", "AB", 56),
            (5, "16/3/2018", "CD", 54),
            (6, "16/3/2018", "BC", 50),
            (7, "17/3/2018", "AB", 48),
            (8, "14/3/2018", "FDG", 34)] # This will be replaced by a text file or json
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
            (10, "AFFDG", 410)] # This will be replaced by a text file or json
    app_info["route"] = "halloffame"
    return render_template("halloffame.html", app_info=app_info, best_individual_games=best_individual_games, best_all_games=best_all_games)
    
@app.route('/about')
def about():
    global app_info
    app_info["route"] = "about"
    return render_template("about.html", app_info=app_info)
    
@app.route('/contact')
def contact():
    global app_info
    app_info["route"] = "contact"
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

# @app.route('/game1', methods=['GET', 'POST'])
# def game1():
#     global app_info
#     global all_riddles
#     global current_game
#     global current_riddle
#     global riddle_counter
#     global attempt
#     global points
#     global gained_points
    
#     if request.method == 'POST':

#         if 'answer_btn' in request.form:
#             # Check Answer
#             if attempt == 1:
#                 answer = request.form['answer_text']
#                 if answer == current_riddle[2]: # answer correct
#                     gained_points += 10
#                     attemp = 1                  # First attempt of
#                     riddle_counter += 1         # Next Riddle
#                     if riddle_counter > len(current_game)-1:    # If that was last riddle then
#                         return redirect(url_for('game_over'))   # GAME OVER
#                     # Trigger next riddle
#                     current_riddle = set_current_riddle(current_game[riddle_counter]) 
#                     # return render_template("game_1.html", app_info=app_info, all_riddles=all_riddles, current_game=current_game, current_riddle=current_riddle, riddle_counter=riddle_counter+1, attempt=attempt, points=points, gained_points=gained_points)

            
#                 # Otherwise answer is wrong
#                 else:
#                     attempt = 2                 # This is your next attempt
#                     points = 6                  # Set correct number of points
#                     # elif attempt == 3:
#                     #     points = 2
#                     # return render_template("game_2.html", app_info=app_info, all_riddles=all_riddles, current_game=current_game, current_riddle=current_riddle, riddle_counter=riddle_counter+1, attempt=attempt, points=points, gained_points=gained_points)
#         return redirect(url_for('game'))
        
# @app.route('/game2', methods=['GET', 'POST'])
# def game2():
    
    
#     global app_info
#     global all_riddles
#     global current_game
#     global current_riddle
#     global riddle_counter
#     global attempt
#     global points
#     global gained_points
    
#     if request.method == 'POST':
        
        
    

#         if 'answer_btn' in request.form:
#             # return "<h1>Now this is Attempt 2 POST ACCEPTED - FORM WORKS</h1>"
            
#         # return "<h1>Now this is Attempt 2 POST ACCEPTED</h1>"
#             # Check Answer
#             if attempt == 2:
#                 # Get all words and concatenate them
#                 answer = ""
#                 for ndx, each_word in enumerate(current_riddle[2]):
#                     index = 'answer_text' + str(ndx)
#                     answer += (request.form['index'] + " ")
                    
#                 if answer == current_riddle[2]: # Answer correct
#                     gained_points += 6          # Gain points
#                     attemp = 1                  # Reset attempt
    
#                     riddle_counter += 1
#                     if riddle_counter > len(current_game)-1:
#                         return redirect(url_for('game_over'))
    
#                     current_riddle = set_current_riddle(current_game[riddle_counter])
                
#                 # Otherwise answer is wrong
#                 else:
#                     attempt == 3                # This is your next attempt
#                     points = 2                  # Set correct number of points
#         return redirect(url_for('game'))
#     return "<h1>Now this is Attempt 2 POST NOT ACCEPTED - FORM PROBLEM</h1>"


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
    global wrong_answers
    global answer
    
    app_info["route"] = "game"  # I will need this to control the menu
    
    #this_riddle = current_game  # What is this for?????????????????????????????? Comment out to see if it is used
    
    if app_info["game"] == False:
        app_info["game"] = True  # Game On
        with open("data/riddles.json", "r") as all_riddles_json:
            all_riddles = json.load(all_riddles_json)
        
        for x in range(0, 5):
            
            repeat = True
            while repeat:
                choose_game=random.choice(all_riddles)
                if choose_game.items() not in current_game:
                    repeat = False
                
            current_game.append(choose_game.items())
        
        current_riddle = set_current_riddle(current_game[riddle_counter])
            
    if request.method == 'POST':
        if 'play' in request.form:
            points = 10
            attempt = 1

        elif 'answer_btn' in request.form:
            # Check Answer
            
            if attempt == 1:
                answer = request.form['answer_text']
                
                # Clean the answer
                # If there are multiple spaces or other white characters in between the words
                temp =[]                    # Clean answer
                temp = answer.split()
                answer=""
                for item in temp:
                    answer += item + " "
                    
                    
                answer = answer.strip()         # Strip trailing spaces
                
                
                if answer.lower() == current_riddle[2].lower(): # answer correct
                    gained_points += 10
                    wrong_answers = []
                    attemp = 1                  # First attempt of
                    riddle_counter += 1         # Next Riddle
                    if riddle_counter > len(current_game)-1:    # If that was last riddle then
                        return redirect(url_for('game_over'))   # GAME OVER
                    # Trigger next riddle
                    current_riddle = set_current_riddle(current_game[riddle_counter]) 
            
                # Otherwise answer is wrong
                else:
                    # wrong_answers = [answer]
                    if len(answer) == 0:                #if no answer is given
                        wrong_answers.append("-")
                    else:
                        wrong_answers.append(answer)
                    attempt = 2                 # This is your next attempt
                    points = 6                  # Set correct number of points

            elif attempt == 2:
                
                # Get all words and concatenate them
                answer = ""
                index = ""
                local_answer = current_riddle[2].split()
                # for ndx, each_word in enumerate(current_riddle[2]):
                for ndx, each_word in enumerate(local_answer):
                    index = 'answer_text' + str(ndx+1)
                    # print index
                    # answer += each_word + "-"
                    # answer += (request.form['index'] + " ")
                    # print request.form['answer_text1']
                    # print request.form[index]
                    answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    
                    
                # print "answer is: " + answer
                # return "<h1>Reached attempt 2 built answer " + index + "</h1>"
                # return index+answer
                # print len(answer)
                # answer = answer[0:-1]      # Strip final space
                temp =[]                    # Clean answer
                temp = answer.split()
                answer=""
                for item in temp:
                    answer += item + " "
                answer = answer.strip()         # Strip trailing spaces
                # print len(answer)
                
                if answer.lower() == current_riddle[2].lower(): # Answer correct
                    gained_points += 6          # Gain points
                    attempt = 1                  # Reset attempt
                    points = 10
                    wrong_answers = []

                    riddle_counter += 1
                    if riddle_counter > len(current_game)-1:
                        return redirect(url_for('game_over'))

                    current_riddle = set_current_riddle(current_game[riddle_counter])
                
                # Otherwise answer is wrong
                else:
                    # wrong_answers.append(answer)
                    if len(answer) == 0:                #if no answer is given
                        wrong_answers.append("-")
                    else:
                        wrong_answers.append(answer)
                    attempt = 3                 # This is your next attempt
                    points = 2                  # Set correct number of points
                    
                
            elif attempt == 3:
                answer = ""
                index = ""
                local_answer = current_riddle[2].split()
                
                for ndx, each_word in enumerate(local_answer):
                    index = 'answer_text' + str(ndx+1)
                    answer += (request.form[index].strip() + " ") #Strip any typed white spaces
                    
                # answer = answer[0:-1]      # Strip final space
                temp =[]                    # Clean answer
                temp = answer.split()
                answer=""
                for item in temp:
                    answer += item + " "
                answer = answer.strip()         # Strip trailing spaces
                
                if answer.lower() == current_riddle[2].lower():  # Answer correct
                    gained_points += 2           # Gain points
                    attempt = 1                  # Reset attempt
                    points = 10
                    wrong_answers = []           # Reset wrong answers

                    riddle_counter += 1
                    if riddle_counter > len(current_game)-1:
                        return redirect(url_for('game_over'))

                    current_riddle = set_current_riddle(current_game[riddle_counter])
                
                # Otherwise answer is wrong
                else:
                    attempt = 1                 # This is your next attempt
                    points = 10                 # Set correct number of points
                    wrong_answers = []           # Reset wrong answers
                    riddle_counter += 1
                    if riddle_counter > len(current_game)-1:
                        return redirect(url_for('game_over'))
                    current_riddle = set_current_riddle(current_game[riddle_counter])

        #This will happen if pass
        # increase attempt
        elif 'pass_btn' in request.form:
            if attempt == 1:
                # wrong_answers.append("-")
                wrong_answers = []
                wrong_answers = ["-"]
                attempt = 2
                points = 6
            # else:
                # attempt += 1
            elif attempt == 2:
                points = 2
                wrong_answers.append("-")
                # wrong_answers[1] = "-"
                attempt = 3
            elif attempt == 3:
                # points = 2
                if riddle_counter > len(current_game)-1:
                    return redirect(url_for('game_over'))
                current_riddle = set_current_riddle(current_game[riddle_counter])
                points = 10
                attempt = 1
                riddle_counter += 1
                wrong_answers = []
            # elif attempt == 4:
            #     points = 10
            #     attempt = 1
            #     riddle_counter += 1
                
                if riddle_counter > len(current_game)-1:     # Call next riddle
                    # Store the gained_points
                    
                    
                    gained_points = 0                         # Reset gained_points
                    return redirect(url_for('game_over'))
                current_riddle = set_current_riddle(current_game[riddle_counter])
                
                
    return render_template("game.html", app_info=app_info, all_riddles=all_riddles, current_game=current_game, current_riddle=current_riddle, riddle_counter=riddle_counter+1, attempt=attempt, points=points, gained_points=gained_points, wrong_answers=wrong_answers)

@app.route('/game_over')
def game_over():
    global app_info
    app_info["route"] = "game"
    app_info["game"] = False
    
    # global current_game
    # global current_riddle
    # global all_riddles
    # global riddle_counter
    # global gained_points
    # global points
    # global wrong_answers         # This will hold wrong answers
    # global answer                 # Current answer of current riddle

    # current_game = []
    # current_riddle = 0
    # all_riddles = []
    # riddle_counter = 0
    # gained_points = 0
    # points = 10
    # wrong_answers =[]           # This will hold wrong answers
    # answer = ""                 # Current answer of current riddle
    
    global_game_reset()
    return redirect(url_for('user'))
    
    
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
