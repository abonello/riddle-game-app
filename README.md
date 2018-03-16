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

#### Added more routes -- About Contact Hall-of-Fame
All manually tested and working.