# Riddle-Me-This
## A Flask milestone project for Practical Python
### Part of the Fullstack Web Developer Course - Code Institute

This project is deployed at []().  
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
echo web:python run.py > Procfile
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

I will think about what fonts to use before proceeding to the next step.

Next I will draft **about.html**, **contact.html** and **halloffame.html** based on the 
same code.