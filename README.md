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
~~~~html

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
* * *
# To DO
I will need to add a game menu item that will appear only when a user is logged in and
only while a game is running. This should allow the user to navigate away from the
game and return to the game by using this menu item.