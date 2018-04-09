# Riddle-Me-This
## A Flask milestone project for Practical Python
### Part of the Fullstack Web Developer Course - Code Institute

This project is deployed at [riddle-guessing-game](http://riddle-guessing-game.herokuapp.com/).  
Github Repository is at [riddle-game-app](https://github.com/abonello/riddle-game-app).

#### Install Flask
~~~~
sudo pip3 install flask
~~~~

#### Prepare requirements file
This will be needed for the Heroku deployment.
~~~~
sudo pip3 freeze --local > requirements.txt
~~~~
**requirements.txt** file will allow anybody else who is cloning this 
repository to install all requirements.  
Note that while install Flask, it will install its own requirements as well.

#### Prepare the Procfile
This will be needed for the Heroku deployment.
~~~~
echo web: python run.py > Procfile
~~~~

#### Create the run.py
This is the application file.
~~~~
touch run.py
~~~~

#### Wireframe
I am using Pencil for wireframing this app.  
I uploaded the files as at 15/03/18 14:44  
These files were pulled to Cloud9.

#### Adding file place holders
I added:  
* users.txt in /data  
* styles.css in /static/css  
* index.html in /templates  

#### Fundamental imports in run.py
~~~~python
import os
from flask import Flask
~~~~

#### create flask application
~~~~python
app = Flask(__name__)
~~~~

#### create first route for ROOT:
~~~~python
@app.route('/')
def index():
    return "<h1>Hello World</h1>"
~~~~

#### Prepare the app to run
~~~~python
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
~~~~
It will get the IP address and the PORT. It also sets debug to True which is 
very handy when developing an app as the server will be restarted automatically
after saving a file.

#### Manual Testing
Run run.py to check that setup and flask are OK.  
Everything working.

#### Added more routes -- About, Contact, Hall-of-Fame
All manually tested and working.

#### Added simple templates for About, Contact, Hall-of-Fame
All manually tested and working.

#### Current routing
~~~~python
@app.route('/')
def index():
    # return "<h1>Hello World -- This is Riddle-Me-This Application</h1><h2>It is a guessing game.</h2>"
    return render_template("index.html")
    
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
~~~~

Note to self: Will be cleaning code later.

* * *
#### Catch up note

18/3/18


Over the past few days I experimented with various html and css code to find
how I am going to lay things down while keeping to the wireframe I prepared.
I explored how the menu will respond to different screen sizes. I want the menu
to be a button at the top for mobiles. It becomes a menu across the top for 
tablets and then a menu below the main title for larger screens.

I managed to achieve this.

I also explored various colors and visual details such as borders. Now I think 
that I am in a position to start laying down the foundation for the index page.
I will start by writing the whole html and css code which I will later refactor
in a way as to use a base template which will be extended in the other templates.

* * *
#### Draft Index.html Template

I finished the responsive draft for the **index.html** template together with 
the accompanying styles.css  
NB:
1. The current colour scheme is only tentative at this stage.
2. The logo image is a place holder. It might be changed later on.

I used Chrome extensively to develope the CSS using the automatic features that
this browser offers to display changes in real time. I also found it handy when
setting colors.

I will think about what fonts to use before proceeding to the next step.

Next I will draft **about.html**, **contact.html** and **halloffame.html** based on the 
same code.

#### Manual testing of draft for index.html
The draft up to this point was manually tested to make sure that the layout
is fully responsive. I used Chrome for this.

#### Selecting Google Fonts

##### Main Title:  short list
|||
|--|--|
|**Gloria Hallelujah**|Schoolbell|
|Courgette|Kalam|
|Merienda|

##### Sub Titles:
Bubblegum Sans

##### Text: short list
|||
|-|-|
|***Forum***|Comfortaa|
|***Kelly Slab***|**Averia Serif Libre**|

##### Selected fonts

Main Title : Gloria Hallelujah  
Sub Titles : Bubblegum Sans  
Other Text : Averia Serif Libre

Changed h2 in main section to h3. Better semantics.


##### Apply draft code to other pages

Now I have index.html, about.html, halloffame.html and contact.html base on the
same layout and responsive design.

What I need to add is the menu for the registration and login at the top of the 
page.

I also need to try and test the deployment on heroku.

##### Bug
I noticed a bug when I tries to load the page on my mobile. There is some 
horizontal scroll of the whole page and I cannot understand what is causing it.
Also the Menu button is partly out of sight.

I rethought the layout for mobile design. I saw that the logo image was taking
too much space so I decided to remove this for mobiles and tablets. It will 
appear only in the desktop layout. Also the form for registering / login has
been moved. It will appear at the top for mobiles and tablets. Note that the 
placement is slightly different due to the Menu button for mobiles. And, it will
appear above the menu (below the titles) for the desktop layout. I think this 
gives a better user experience. I am still finding that there is some horizontal 
scrolling when testing in Chrome emulating mobiles.

Fixed: missprint in .logo margin. Was set to -50px. Now chagned to 0px.

#### Heroku Deployment
Logged in to heroku. (Need email and password) I then listed the apps I already
have. Following this I created an app with the title "riddle-guessing-game". All
this was done in the command line.
~~~~
heroku login
heroku apps
heroku apps:create riddle-guessing-game
~~~~
Once I list the heroku apps again, the new app is in the list.
Logging into heroku and creating an app will also add a git remote. This can be 
viewed by listing the git remotes.
~~~~
git remote -v
~~~~

The result of the last command is:
~~~~
    heroku  https://git.heroku.com/riddle-guessing-game.git (fetch)
    heroku  https://git.heroku.com/riddle-guessing-game.git (push)
    origin  https://github.com/abonello/riddle-game-app.git (fetch)
    origin  https://github.com/abonello/riddle-game-app.git (push)
~~~~

Next I will push the project to heroku.
~~~~
git push -u heroku master
~~~~

Successfully installed Flask-0.12.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24
https://riddle-guessing-game.herokuapp.com/ deployed to Heroku
remote: Verifying deploy... done.
To [Riddle-Guessing-Game](https://git.heroku.com/riddle-guessing-game.git)

Create a watcher in heroku.
~~~~
heroku ps:scale web=1
~~~~

Next we need to go to the Heroku site. Select the app. From settings, click on 
*Reveal Config Vars*. Here you need to create some configuration variables.
Set the following key : value pairs
IP 0.0.0.0
PORT 5000

These will be the IP and PORT used in the following line of code in run.py
~~~~python
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
~~~~

Restart all Dynos:  
Go to More in Heroku and restart all dynos.

I am getting the following error:  
at=error code=H14 desc="No web processes running" method=GET path="/favicon.ico" host=riddle-guessing-game.herokuapp.com request_id=86105bba-9b47-44f2-a211-f83b2cc3a3fa fwd="92.21.201.110" dyno= connect= service= status=503 bytes= protocol=https

I tracked this down to the following:  
When I run
~~~~
heroku ps:scale web=1
~~~~
I get the following:
*       Scaling dynos... !  
         ▸    Couldn't find that process type.  
 

I changed this code in run.py
~~~~python
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
~~~~

Then I pushed again to heroku. run the scaling and restarted the dynos.  
No errors and the app is successfully deployed.
~~~~
git push -u heroku master
heroku ps:scale web=1
~~~~

#### Passing a variable to index.html
~~~~html
<h2>{{ username }}</h2>
~~~~
and run.py, the @app.route('/')
~~~~python
username = "AB"
return render_template("index.html", username=username)
~~~~

This displays the hardcoded text. Now I want to capture a text written as 
username and posted using the login button.

Get two buttons to function from the same form.  

Changes to code:  
run.py  
import request is added  
modify the routing for / 
Currently I have a default username but this will be changed. It will be a list
of usernames stored in a text file. The file will be read in a set to which new
usernames can be added to make sure they are unique.
~~~~python
from flask import Flask, render_template, request

@app.route('/', methods=['GET','POST'])
def index():
    username = "AB"
    if request.method == 'POST':
        if 'register' in request.form:
            username = request.form['username']
        elif 'login' in request.form:
            username = "Please register first"
        
    return render_template("index.html", username=username)
~~~~

index.html  
POST method was added to the form and an action. names were added to each form 
part.  
~~~~html
<form class="align-right" method="POST" action="/">
    <div class="form-group">
        <input type="text" class="form-control form-username form-align" name="username" id="username" placeholder="username">
        <button type="submit" class="btn btn-default form-align" name="login" type="submit" value="login">Login</button>
        <button type="submit" class="btn btn-default form-align" name="register" type="submit" value="register">Register</button>
    </div>
</form>
~~~~

* * *
Next I need to check if a username already exist when someone tries to register.  

~~~~python
@app.route('/', methods=['GET','POST'])
def index():
    username_set = {'AB', 'BC', 'CD'}
    username = ""
    if request.method == 'POST':
        if 'register' in request.form:
            username = request.form['username']
            if username in username_set:
                username = ""
                return render_template("index.html", username="username already exist try another one")
            else:
                username_set.add(username)
                
        elif 'login' in request.form:
            username = "Please register first"
        
    return render_template("index.html", username=username, allusers=username_set)
~~~~

For now a username_set holds all the users. When someone new tries to register
the username is checked to see if it already exist in which case a text appears,
currently an h2 below the subtitle asking the user to select another name. If 
the username does not exist it is added to the set.  
I am currently displaying the contents of the set in the main section for testing 
purposes. This will be removed.

The set is reinitialised everytime the / route is selected so I cannot add two users.
Moving
~~~~python
username_set = {'AB', 'BC', 'CD'}
~~~~
outside of def index() solved this temporary problem. Now the set will hold any
added users for as long as I do not restart the server.

Login and Registration sorted.

~~~~python
@app.route('/', methods=['GET','POST'])
def index():
    allusers = ""
    username = ""
    if request.method == 'POST':
        username = request.form['username']
        with open("data/users.txt", "r") as readusernames:
            allusers = readusernames.read()
        if 'register' in request.form:
                if username in allusers:
                    return render_template("index.html", username="username already exist try another one")
                else:
                    with open("data/users.txt", "a") as addusernames:
                        addusernames.write(username + "\n")
                        allusers += (username)
                    return render_template("index.html", username=username, allusers=allusers)
                
        elif 'login' in request.form:
            if username == "":
                return render_template("index.html", username="Enter a username to log in", allusers=allusers)
            elif username in allusers:
                username += " LOGGED IN"
                return render_template("index.html", username=username, allusers=allusers)
            else:
                username = "That username does not exist."
            return render_template("index.html", username=username, allusers=allusers)
        
    return render_template("index.html", username=username, allusers="")
~~~~

I will now need to make the registration button redirect to another page and 
move the relevant code there.

I changed the register code in route for index.html to load the register.html  
In here I will have another form which will do the checking of a username to 
see if it already exist and the actual registration of a new username.

Completed code for register page.  
Checking if username already exist.  
Then register and for now redirect to index.html. Later this will take the user
to the user page in logged in status.

#### There is a bug.

When I check if a username is available, if it is available it is immediately 
showing in the header. This should only appear after the user finishes the
registration process. (or if the user logs in using the login button).

Fix:  
At first I tried to remove the username=username from the return, but this means
that I cannot keep the username displayed in the text box. I wanted to keep this
then I decided to remove the variable displaying the username in the header in
the register page as I do not intend to use this anyway.

Alternatively I could have given a different variable name for the text box but
then I would add another variable to an already long list that I have to pass.


~~~~html
<form class="align-right" method="POST" action="/">
    <div class="form-group">
        {%if logged == "True" %}
            <button type="submit" class="btn btn-default form-align" name="logout" type="submit" value="logout">Logout</button>
        {% else %}
            <input type="text" class="form-control form-username form-align" name="username" id="username" placeholder="username">
            <button type="submit" class="btn btn-default form-align" name="login" type="submit" value="login">Login</button>
            <button type="submit" class="btn btn-default form-align" name="register" type="submit" value="register">Register</button>
        {% endif %}
    </div>
</form>
~~~~
The above code those not work as I cannot make it call the same route from the logout as for the login or register buttons.
The following code allows me to have different action for logout and works well.
~~~~html
{%if logged %}
    <form class="align-right" method="POST" action="/logout">
        <div class="form-group">
            <button type="submit" class="btn btn-default form-align" name="logout" type="submit" value="logout">Logout</button>
        </div>
    </form>
{% elif not logged %}
    <form class="align-right" method="POST" action="/">
        <div class="form-group">
            <input type="text" class="form-control form-username form-align" name="username" id="username" placeholder="username">
            <button type="submit" class="btn btn-default form-align" name="login" type="submit" value="login" alt="login">Login</button>
            <button type="submit" class="btn btn-default form-align" name="register" type="submit" value="register">Register</button>
        </div>
    </form>
{% endif %}
~~~~

I also applied a try except code that will display the exception raised.
Small thing to fix. After logging out I was ending up in a url ending .../logout

I fixed this by redirecting to the url of index  
I also made sure that the logged variable holds the value False
~~~~python
logged = False
return redirect(url_for('index'))
~~~~

I need to make logged status and current username persistent between pages.  
Done using global variables.

I am loosing logged status. Need to pass it around.

I created three global variable:
1. username
2. allusers
3. logged

and I am passing these to all pages. At the moment I am displaying them on all
pages just to make sure that the values are correct. Later these will be removed 
from the pages.
~~~~html
<p>User: {{ username }}</p>
<p>All users: {{ allusers }}</p>
<p>Logged: {{ logged }}</p>
~~~~

I need to clean the code, removing any commented out code. I will keep a copy 
of the code as it is now and store it in a folder called old. The reason for 
this is so that I can quickly refer to it and study it. This will be beyond what
I can do with the git versioning.

Cleaned code run.py

* * *
### User page

Now I need to create a User page. The menu for the user page should only appear
in all other pages if the user is logged in.

The code for the link in the menu is:
~~~~html
{% if logged %}
    <li class="nav-item"><a class="nav-link scroll" href="/user" id="userNav">USER</a></li>
{% endif %}
~~~~

The code for the route is:
~~~~python
@app.route('/user')
def user():
    global logged
    global username
    global allusers
    return render_template("user.html", username=username, allusers=allusers, logged=logged)
~~~~

I created a temporary user.html  
Now I need to make the register form in register.html and the login in other pages 
to redirect to the logged in user page.
Note: I am aware that the code related to login / register / logout is only on
the index.html. I intend to do a base.html page which will make this code available
for all pages.

I added jinja templating code to automatically hide the current page's menu.
In this way I have a code which is ready to be used in a base.html page.

I want to prepare the layout of the user.html page.
I created this set of data (hardcoded for now)
~~~~python
user_data = {
    "number_of_games" : 5,
    "date_best_game" : "15/3/2018",
    "points_best_game" : 56,
    "total_user_points" : 340
}
~~~~
Later on this data will be stored in a text file in json format. This makes passing
a lot of variables to an html page easier. The same system will replace the other
current varaibles controlling user login.
Now I want to add a list of games played. The data to be stored are date and points gained.
Order by date -- most recent first.

~~~~python
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
~~~~

I modified other routes which call the user route to use 
~~~~python
redirect(url_for('user'))
~~~~
instead of
~~~~python
return render_template( . . . )
~~~~

In user.html
I created a bootstrap styled table within a div that will display the data 
for the games played by the logged in user.

#### Shadow around divs which contain tables of data
Given that this is a game I feel I have more artistic freedom to explore ways 
to display tables than I would have if this project was a corporate website or
the like. For this reason I am applying multiple shadows in order to get a mix of 
colours around the divs that contain tables of data. The colors chosen are on the 
red and yellow scales to keep close to the colours which are dominant in the 
images I will be using in the riddles. The exact color choice is quite subjective.

I will be using identical shadows in other pages to unify the style of the application.

Now I need to uncomment the second div within the main section. Here I will have
the button which the user will use to start the game.



# Bug
The login and register redirection is not working.  
This fixes the problem:  
~~~~python
return redirect(url_for('user'))
~~~~

In main section of user.html I moved the main class from the column divs to the 
row div. This will give a unified background for both sides of the page with equal
height if the two sides have different amount of content.

Added a simple button that will POST to a new page called game.html



## Hall of fame
Updated code of halloffame.html to display two tables, one for Individual Games 
and the other for All Games Played.

There is also an instruction for a guest user to login / register. This will be 
hidden once a user logs in and will be replaced with the username.

For now the data is hard coded in a list. This will be replaced and stored in a 
text file so that it can be retained from session to another.


## Refactoring data structure for app information
I am going to change the various global variables to a dictionary. In this way 
I will only have to pass one item to a web page.
Done.



### Images
I processed 10 images and uploaded them for testing algorithms related to the game.
I created a json file with related information "riddle.json".

I need to import json in run.py


Random selection of riddles  
import random

Now I have code that can randomly select 5 riddles out of a test group of 10.
I noticed that sometimes the function selects less than 5 riddles. I do not know
what is causing this but I will look into it later.
It happens if an item is selected more than once. I will use a while loop.
I can extract the name of the file and show the correct image for the riddle.
Once all the riddles in the game have been used, the game will be over and 
app_info["game"] will be set to False.

Fixed a bug that resulted in a smaller selection of riddles due to the random
process selecting an item multiple times.

#### buggy code
~~~~python
for x in range(0, 5):
    # Randomly select 5 riddles
    choose_game = random.choice(all_riddles)
    print choose_game.items()
    if choose_game.items() not in current_game:
        current_game.append(choose_game.items())

current_riddle = current_game[riddle_counter]
~~~~

#### Fixed code
~~~~python
for x in range(0, 5):
    # Randomly select 5 riddles
    repeat = True
    while repeat:
        choose_game=random.choice(all_riddles)
        print choose_game.items()
        if choose_game.items() in current_game:
            pass
        else:
            repeat = False
        
    current_game.append(choose_game.items())
    
current_riddle = current_game[riddle_counter]
~~~~


### Create Game over route
Clears values of variables and redirect to user page. The points for the last game
will eventually be listed as the first row of the list of games played.


I need a variable to track the Attempt of a particular riddle and change what is 
shown on the game page.

First and Second attempt working. Display only. Will deal with checking the 
answer later.  
I will add the code for the third attempt.  
Finished code for third attempt layout including showing number of letters per 
word.   


Now I need to capture the input from the user and check the answer. Then decide 
if it is correct or wrong. If it is correct assign the points and move to the next 
riddle or end game if it is the last riddle. If it is wrong, move to the next 
attempt or move to next riddle if it is the last attempt or end game if it is the 
last attempt of the last riddle.

## HEROKU bug: Problem with Heroku
It is not finding the image files

~~~~
<img class="img-responsive" src="static/img/{{ current_riddle[1][1] }}" alt="riddle image"></img>
File "/app/.heroku/python/lib/python3.6/site-packages/jinja2/environment.py", line 411, in getitem
~~~~
I suspect that this will not be the only line of code that will have to be changed.  

I suspect that the items in current_riddle appear in heroku appear in a different 
order than locally so instead of finding the image name the code is returning 
something else.  
current_riddle is a list
This is filled from current_game which is another list.  
In turn this contains dictionaries from the json which will be unordered.  
I need to use a different way to call for that data that I need.


I refactored the code related to creating the list of the current riddle. I changed 
the tuple holding the answer into a string. I also have a fixed order to the data.
I will try to deply to heroku and see if it works.

Had to comment out some debugging code and after committing and pushing again to 
heroku it is working well. Now I commented out all the debuging code that was 
at the bottom of the page.

* * *
### Show riddle number
Added this code

I added code to start checking answers  

I need to clean run.py and game.html. I will be deleating all commented out code 
that is not going to be used.



## 400 Bad Request error in game.html
The routing and action for the form did not change however when I try to POST an 
answer during attempt=2 I m getting this error. Attempt = 1 works well.
This error was not there before.

I found that enumeration starts counting from 0 and loop.index starts from 1
Therefore when I tried to get information from the table the reference was wrong
The bad request related to getting information from the page not the page posting 
to the server.

There was also a problem with enumeration which was counting all letters rather 
than words.

Now it is fixed. Codes as:  
~~~~python
elif attempt == 2:
    # Get all words and concatenate them
    answer = ""
    index = ""
    local_answer = current_riddle[2].split()
    # for ndx, each_word in enumerate(current_riddle[2]):
    for ndx, each_word in enumerate(local_answer):
        index = 'answer_text' + str(ndx+1)
        answer += (request.form[index] + " ")

    answer = answer[0:-1]           # Strip last space
    
    if answer == current_riddle[2]: # Answer correct
        gained_points += 6          # Gain points
        attempt = 1                 # Reset attempt

        riddle_counter += 1
        if riddle_counter > len(current_game)-1:
            return redirect(url_for('game_over'))

        current_riddle = set_current_riddle(current_game[riddle_counter])
    
    # Otherwise answer is wrong
    else:
        attempt = 3                 # This is your next attempt
        points = 2                  # Set correct number of points
~~~~

Now code for Attempt 1 and Attempt 2 of the game is done.



Finished code for attempt 3.
* * *

Added stripping of white spaces  

#### Clean input for attempt 1:  
Removed multiple space or a new line between words that the user might type  
before the answer is checked.
~~~~python
# Clean the answer
# If there are multiple spaces or other white characters in between the words
temp =[]
temp = answer.split()
answer=""
for item in temp:
    answer += item + " "

answer = answer.strip()     # Strip trailing spaces
~~~~

#### Make it case insensitive:  
I turn both answer and stored value to lower case before comparing
~~~~python
if answer.lower() == current_riddle[2].lower():
~~~~


Changed place holders in text fields to indicate the number of the word within
the answer.


Done  
Store and display wrong answers during attempt 2 and attempt 3.

#### Correcting a bug in displaying answers.
If I am on the second or more riddles of a game, there is some information that 
is already stored in the wrong_answers list. This needs to be cleared before
starting subsequent riddles otherwise it will appear erroneously if one passes.



#### Looking for Bugs
I am going through the logic and running the game through different possibilities.
I am finding a number of errors mostly related to not reseting variables. I have 
neglected the branch of the game which deals with Pass. variables like answer need to 
be global so that they can reach here too.
Since I have to reset all variables at least in two places, when a game is over 
and when a person logs out I will create a function for this.


Changed the code to make it more robust. It can now accept the all the input for 
attempts 2 and 3 even if typed all in one text field EVEN IF they contain 
multiple spaces in between or a new line. [NB. Not escaped characters - I will 
treat this as spelling mistakes and will be marked as incorrect.]

NB: Attempt 2 and 3 can accept the answer all typed in one of the text fields.
(Text fields act just as a visual clue) This is not undesirable. It can make typing
easier and if a user chooses to do this the answer will be accepted.

All manual checks of the logic done up to this stage.


#### Bug in game.html
I noticed that all three attempts where saying First attempt. This has been fixed.
~~~~html
<div class="col col-md-10 col-md-offset-1">
    <p class="game_text">Points: {{ gained_points }}</p>
    <p class="game_text
    {% if attempt > 1 %}red 
    {% endif %}">
    {% if attempt == 1 %}First 
    {% elif attempt == 2 %}Second 
    {% elif attempt == 3 %}Third 
    {% endif %}attempt: {{ points }} points</p>
</div>
~~~~

Added a game menu item that will appear only when a user is logged in and
only while a game is running. This should allow the user to navigate away from the
game and return to the game by using this menu item.


### Prepare unittest
The aim is to clean the run.py - Refactor using functions and unit test the 
functions that need them.
I have already manually tested the draft code up to now but adding unit tests
will make the process easier and avoids human error. Since this is my first 
large project that I am building on my own from scratch I took a more organic
improvisatory approach to arrive at this point. I chose this approach because as
a composer and sound designer I am familiar and confident with it and have 
transferrable skills that I can use.  
I now want to make the rest of the development more systematic.

unittest module is in standard library -- no need to install anything  
Create a test_run.py file. This will hold the test code.

Import unittest module and the module we will be testing, ie run.py
~~~~python
import unittest
import run
~~~~

#### Create Test Cases
Create a test class that inherits from unittest.TestCase. This inheritance will
give us access to a lot of testing capabilities. 

|Method	| Checks that | New in |
|-------|-------------|--------|
|assertEqual(a, b) | a == b |  |
|assertNotEqual(a, b) | a != b |  |
|assertTrue(x) | bool(x) is True |  |
|assertFalse(x) | bool(x) is False |  |
|assertIs(a, b) | a is b | 2.7 |
|assertIsNot(a, b) | a is not b | 2.7 |
|assertIsNone(x) | x is None | 2.7 |
|assertIsNotNone(x) | x is not None | 2.7 |
|assertIn(a, b) | a in b | 2.7 |
|assertNotIn(a, b) | a not in b | 2.7 |
|assertIsInstance(a, b) | isinstance(a, b) | 2.7 |
|assertNotIsInstance(a, b) | not isinstance(a, b) | 2.7 |

assertRaises(exc, fun, *args, **kwds)	fun(*args, **kwds) raises exc	 
assertRaisesRegexp(exc, r, fun, *args, **kwds)	fun(*args, **kwds) raises exc and the message matches regex r	2.7

assertAlmostEqual(a, b)	round(a-b, 7) == 0	 
assertNotAlmostEqual(a, b)	round(a-b, 7) != 0	 
assertGreater(a, b)	a > b	2.7
assertGreaterEqual(a, b)	a >= b	2.7
assertLess(a, b)	a < b	2.7
assertLessEqual(a, b)	a <= b	2.7
assertRegexpMatches(s, r)	r.search(s)	2.7
assertNotRegexpMatches(s, r)	not r.search(s)	2.7
assertItemsEqual(a, b)	sorted(a) == sorted(b) and works with unhashable objs	2.7
assertDictContainsSubset(a, b)	all the key/value pairs in a exist in b	2.7



Each test will be in its own method. The naming convention for these methods is 
to start with **test_** which is required. Any test method whose name does not 
start in this way will not run. These test_methods will take **self** as a 
first argument.

I am going to create a simple add function in a temp_run.py and create a test 
for it to check that everything is set up properly. 
Using the usual Fail Change Pass

~~~~python
# Method to test in temp_run.py
def add(x,y):
    """Add Function"""
    return 0
~~~~

~~~~python
# Testing code in test_run.py
import unittest
import temp_run         # The code that we are testing

class TestRun(unittest.TestCase):
    '''
    Test suite for run.py
    '''
    def test_add(self):
        '''
        test a testing add method to check that set up is ok
        '''
        answer = run.add(10, 3)
        self.assertEqual(answer, 13, "Failed")
~~~~

To run from command line:
~~~~
python -m unittest test_run.py
~~~~
This method of running unittest is not working in cloud9

I added 
~~~~python
if __name__ == "__main__":
    unittest.main()
~~~~
and now I can call the test by using the run button.

Function to test:
~~~~python
def add(x,y):
    """Add Function"""
    return x + y
~~~~

Test: test_run.py
~~~~python
import unittest
import run              # The code that we are testing

class TestRun(unittest.TestCase):
    '''
    Test suite for run.py
    '''
    def test_add(self):
        '''
        test a testing add method to check that set up is ok
        '''
        answer = run.add(10, 3)
        self.assertEqual(answer, 13, "Failed")
        self.assertEqual(run.add(10, 3), 13, "Failed: add positive to positive")
        self.assertEqual(run.add(0, 3), 3, "Failed: add 0 to positive")
        self.assertEqual(run.add(0, -5), -5, "Failed: add 0 to negative")
        self.assertEqual(run.add(-7, -5), -12, "Failed: add negative to negative")
        self.assertEqual(run.add(7, -5), 2, "Failed: add positive to negative, positive answer")
        self.assertEqual(run.add(7, -9), -2, "Failed: add positive to negative, negative answer")
        self.assertEqual(run.add(0, 0), 0, "Failed: add 0 to 0")

if __name__ == "__main__":
    unittest.main()
~~~~

Now that I know that unittest is working properly I will delete both the add method
and its test.


I will start by testing each route that I have.


Created a /login route. Remove the related code from / route

Added Sessions. Now tests for routes which require login are not working well.  
**I Need to discuss this with Nishant**

I created a new class in the test suite. This will be used to test functions
that need to read or append data to files. Two @classmethod are used, one will 
create test files at the beginning  and the other will remove the test files at 
the end of all the tests in this class.

The test_user.txt contains  
    test_user1  
    test_user2  
    test_user3  
    
The function I am testing is the following:
~~~~python
def read_from_file(file_name):
    store=""
    file = "data/" + file_name
    with open(file, "r") as readusernames:
        store = readusernames.read()
    return store
~~~~

The test is  
~~~~python
def test_read_from_file(self):
    """ Read from a text file """
    data = run.read_from_file("test_users.txt")
    print(data)
    self.assertIn("test_user1", data)
    self.assertIn("test_user2", data)
    self.assertIn("test_user3", data)
    self.assertNotIn("test_user4", data)
~~~~
It passes. Now I will apply the function whenever I need to read a file. I 
need to read the users.txt for registration and login.

Later I need to add other txt or json files to hold list of games for a user and 
hall of fame.

I will use the same read function to read json files. There is an important change
that needs to be done to the **json.load** method. This expects an object that has
a **.read** attribute. My function turns the data into a string so I will use 
**json.loads** instead. The **s** at the end means that it expects a string.

#### Games Played by User
At the moment it is a simple dictionary. I want to store it into a text file. 
Later I want to turn it into a json file so that I can store the data for different 
users.
~~~~python
user_data = ast.literal_eval(read_from_file("user_game_data.txt"))
~~~~
Now I added a user name to the data. I had a bit of a problem with the tuples 
but I found a way of hiding these within a dictionary. A sort of encoding and 
decoding. There might be more elegant ways of doing this but it works.

Now I can read data about the games played by a user from a json file and display 
them in the user's page. If a player has not played any games yet an empty set 
of data is returned and the display adapts accordingly.

Tidied the test_run.py

Now I need to add any games played by a user. I will need to know the date, 
build the set of data including best points and corresponding date and total
points  

Build test for sort_current_riddle  -- I did this function to make sure that 
the order of the data is always the same. This was giving an error when I 
deployed on heroku.

Created unittest for json_tuple_helper_function - this is useful for useing 
tuples in json files

Created test for find_loggedin_user  -- this is the function which will look up 
for stored games to display for a particular user.

I worked on a function that will update the data for a particular user; number 
of games played, date of best game, points for best game, total points gained, and 
a list of games played.  
Now I need to write this back to the json file, but I want it to amend the data
in the file if a record for the user already exist, otherwise I want it to
add a new record if it is a new user.

I was thinking of using this function in the game over function but it was breaking 
the unittest for that routing. Probably because the routing will be doing 
some processing instead of redirecting immediately. Now I placed it at exit 
points of the game function before it redirects to the game_over function.
I really do not understand why this is happening because I do call the 
global_game_reset() function and the test works fine.



To Check: Do I need to change the structure of my json to give an identifier for 
each record?

#### Simplify Json structure
I can simplify the jason structure to be able to locate a user's record by using 
the username as a key for the related data. I already have code to check that 
usernames are unique which will be useful for this data format. Ex:  
~~~~
{'one': {
    'col1': 'data1', 
    'col2': ['a', 'b', 78], 
    'col3': ('d1', 'd2', 56)}, 
 'two': {
    'col1': 'data2', 
    'col2': ['c', 'd', 53], 
    'col3': ('e1', 'e2', 25)}
}
~~~~
This means that I need to revisit **find_loggedin_user**. The unittests for this 
function assume a different format of data so they will need to be reworked too.

I saved the current file with a different name "user_game_data_json3.json" and 
duplicated the function with a name of find_loggedin_user_OLD. I prefer this 
way of working as I can cross reference without having to undo or rely 
on versioning (Although versioning is still being used).

I made the changes in the json file and as expected the unittest failed. I am 
going to prepare a unittest for the new format which should fail at first and 
then work on the function.

Finished refactoring find_loggedin_user to work with new data. **NB:** the output 
of the function did not change so there should be no effect on any calls to this
function. All tests pass.

The user page is not updating the data displayed at the end of a game
I found the error in:
~~~~python
info = {}
    info["item"] = ["1/4/2018",  gained_points]
    info["istuple"] = True
~~~~
which results in 
~~~~
[{'item': ['1/4/2018', 10], 'istuple': True}, ('17/3/2018', 48), 
~~~~
I need the first group of data to be like the second. -- DONE.  

Now I need to save it to json.

#### bug with unittest test_game_over

It is rendering the user template correctly but the unittest is receiving a 
500 error instead of status_code 200.
 I cannot find the error it is tied to the occasional error in store_game_info:  
 about indeces and strings for line of code  
 TypeError: string indices must be integers
 ~~~~python
 user_data["number_of_games"] += 1
 ~~~~
That value is stored as int. I am trying the following to see if I can eliminate it:  
~~~~python
user_data["number_of_games"] = int(user_data["number_of_games"]) + 1
~~~~
This did not solve the problem. user_data is a dictionary. The keys should be strings.




#### Now I need to update the json file
At the end of a game, the json file need to be updated.

This is working.

I noticed a bug: When a new user registers, the user is not taken to the user page.
Trying to force the userpage will keep redirecting to the home page. I need to 
set the session
~~~~
session['logged_in'] = True
~~~~


# Problem
## If two users log in from two different machines they will interfere with each other's game. It looks like the latest person to log in takes over.

#### Template Inheritance
Turned each html into an extension for a base.html file. This has reduced 
drastically the amount of code in the html files.


#### Flash Points Just Gained in latest game

Flashing the points gained at the end of a game. This will be displayed when
the user is returned to the user's page at the end of a game.

#### Starting planning files needed for recording Hall of Fame (HOF)

#### Using datetime to store today's date in records of games and HOF
~~~~python
import datetime

# in store_game_info()
today = datetime.datetime.now().strftime("%d/%m/%Y")
~~~~
For now this will be used to store the information about last played game and 
date_best_game played (if it applies) in user_game_data_json.json.

Later it may be needed for HOF too if data need to be updated.

I need to update the unittest for test_store_game_info since at the moment it is 
using a hardcoded date.  --- DONE

#### Contact form
Drafted. Does it need to be working for this project?

#### Hall of fame
Now reading from file
Turned best_individual_games into a global variable so that I can access it from
other functions, specifically the store_game_info().

Individual Hall of Fame is working well. It displays data from a json file and it 
will update and save the data to the same file after a game is played if the 
points make it to the hall of fame.

Added code for total points HOF.

#### HOF all games add # of games played
Added code in halloffame.html for the table to hold and display the data.  
Adjusted template of hof_all_games.json  
Code for all games to read and write json

#### changed Contact form

#### Cleaned run.py and rearranged order of functions.

#### Fixed Register button which was registering empty users
I also added a class to hide the register button when a user first reaches this 
page. Thus the user has to press the "Check Username Available" button. If the 
username is available, the "Check Username Available" button is hidden and the 
"Register" button is displayed.  
If for any reason the user deletes the username which will still be displayed 
in the text field, then tries to register, the user will be redirected back 
to the "Check username Available" button and the message "Please type in a 
username and check its availability." will be displayed. 
PART of DEFENSIVE CODING.

* * *
* * *
## TO DO -- ESSENTIAL

_~~Strip any trailing spaces at the end to an input string~~_

_~~For attempt 1 make sure there is only one space between words.~~_

_~~Make it case insensitive~~_

_~~Store and display wrong answers during attempt 2 and attempt 3.~~_

_~~I will need to add a game menu item that will appear only when a user is logged in and
only while a game is running. This should allow the user to navigate away from the
game and return to the game by using this menu item.~~_

_Clean the run.py - Refactor using functions and unit tests for the functions._  
Some has been done. More to go -- ONGOING

_~~Store Points, **Games Played by User**and Hall of Fame in a permanent way.
Text or JSON?~~_ 

_~~Template Inheritance -- Clean the templates using base.html  
This will extend the base code. EX:~~_
~~~~html
{% extends 'base.html' %}
{% block content %}
<h2>{{ page_title }}</h2><!-- Home Page -->
{% endblock %}
~~~~

_~~Add code for today's date~~_

_~~Build contact form~~_

Better text for **About** including rules for game, input types expected. Case insensitive,
No extra characters expected, numbers as text.  

_~~Attempt 2 and 3 can accept the answer all typed in one of the text fields.
(Just a visual clue)~~_

Put more images and increase the game to 10 riddles.

```diff
- How can I prevent certain routes from being accessed directly. 
- I want them to be accessible only through the menus AND 
- when the user is logged in.
```

```diff
- Check that the game can be accessed independently by more 
- than one user at the same time.  NOT WORKING
```

```diff
- At the end of each riddle I need some form of feedback 
- about outcome and number of points gained. 
- Similarly at end of game need to display the amount of 
- points earned for the whole game before moving on to 
- the user page.  

- I was thinking some form of modal before progressing 
- to the next riddle or the user page if it is the end 
- of the game.
```
***Perhaps a breakdown of points and answers, but this can be placed in EXTRAS.***

_~~Register button is logging in a user with an empty name. Button should be
inactive if no username is typed.~~_





## TO DO -- EXTRA
<span style="color:blue">`If a user is added to the HOF all games, I need to check if he already is on the
list. If yes, his entry will be updated, ie older entry removed. Need to check 
that this does not end with less than the current of entries. ie do not drop 
entries before checking and updating.`</span>

Timed game

Sounds





## Applying colors to markdown text and bullets

- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`
- ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) `#c5f015`
- ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `#1589F0`


```diff
+ this will be highlighted in green
- this will be highlighted in red
```