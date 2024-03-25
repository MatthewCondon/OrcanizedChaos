## The below code was developed to create the Orcanized Chaos Web Application via Flask.
## To run it, simply execute "python3 app.py" in the terminal
## For more information on how this file was created/designed, reference instructions.txt in the Github Repository

## Import Tools Used Throughout App
# General Tools
from flask import *
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt # Will be used for password encryption/decryption
# MySQL Tools
import mysql.connector
import re, hashlib


## Setting up the Flask App
# Instantiate Flask Object and DB Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mightyMinionsOrcanizedChaos'


## Database Configurations
# Add Database Info
mydb = mysql.connector.connect(host='localhost', user='orcaAdmin', password='mightyMinions2024@', database='orca_users') # Will be hidden later...

# Database Models created in terminal
## Extra Configurations
bcrypt = Bcrypt(app) # Used for Password Hashing later...


## Pages Work
## Routes that for corresponding pages
# Load automatically when site opens
@app.route('/')
def start():
    return render_template('home.html')


# Home Page
@app.route('/home')
def home():
    return render_template('home.html')


# Used for logging into account
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If user posts a form, take username and password
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Check account existence on MySQL DB
        mysqlcursor = mydb.cursor()
        mysqlcursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        # Return result
        currentAccount = mysqlcursor.fetchone()

        # Determine account validity
        if currentAccount:
            # Create session data
            session['id'] = currentAccount[0]

            # Send user to profile page
            return redirect(url_for('profile'))

    # In any other case, direct user to login page
    return render_template('login.html')


# Used for viewing user profile
@app.route('/profile', methods=['GET','POST'])
def profile():
    # If user is logged in, send them to profile.html
    if 'id' in session:  # Check if the user is logged in
        return render_template('profile.html', username=get_username(session['id']))
    # If user is not logged in, send them to the login/signup pages
    else:
        return redirect(url_for('login'))  # Redirect to login page if not logged in


# Used for signing up
@app.route('/signup', methods = ['GET','POST']) # Specify HTTP methods allowed while on this page
def signup():
    # If new user posts a form, take username and password
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Check if account exists in MySQL Database
        mysqlcursor = mydb.cursor()

        # Grab DB Data
        mysqlcursor.execute('SELECT * FROM users WHERE username = %s',(username,))
        currentAccount = mysqlcursor.fetchone()

        # If account username already exists, redirect to login page
        if currentAccount:
            return redirect ( url_for ('login' ))
        # Else create new account and add to MySQL Database
        else:
            username = request.form['username']
            password = request.form['password']
            
            mysqlcursor.execute('INSERT INTO users VALUES(NULL, %s, %s)',(username, password))
            mydb.commit()

            mysqlcursor.close()

            # Return user to /login
            return redirect ( url_for ('login' ))

    # In any other case, direct user to signup page
    return render_template('signup.html')


# Game 1: Asteroids
@app.route('/asteroids')
def asteroids():
    return render_template('asteroids.html')


# Game 2: Invaders
@app.route('/invaders')
def invaders():
    return render_template('invaders.html')


# Game 3: Original
@app.route('/origins')
def origins():
    return render_template('original.html')


# Thank You Page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    

# Feedback Form
@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method == 'POST' and 'email' in request.form and 'subject' in request.form and 'message' in request.form:
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Establish connection to MySQL Database
        mysqlcursor = mydb.cursor()

        # Insert into database
        mysqlcursor.execute('INSERT INTO feedback VALUES(NULL, %s, %s, %s)',(email, subject, message))
        mydb.commit()

        # Close cursor connection
        mysqlcursor.close()

        # Direct user to thank you page
        return redirect(url_for('thankyou'))

    # In any other case, direct user to feedback page
    return render_template('feedback.html')


## Logout Information
@app.route('/logout')
def logout():
    # Close session to log user out
    session.pop('id', None)

    # Send user back to login page
    return redirect ( url_for ('login' ))


# Extra Command to assist in getting the username on the profile page
def get_username(id):
    mysqlcursor = mydb.cursor() # Create connection to DB
    mysqlcursor.execute('SELECT username FROM users WHERE user_id = %s', (id,)) # Grab specified data from DB
    username = mysqlcursor.fetchone() # Hold DB Information
    username = username[0] # Convert from JSON Data
    return username


## Run the Application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
