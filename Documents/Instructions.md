## Pip Install Requirements

This application requires multiple installations on your machine to ensure that it works properly. Run the below command:


pip install Flask Flask-Login Flask-Bcrypt mysql-connector-python


## Flask App

Now that all tools have been properly installed on the system, the rest of the flask application must be set up. It is recommended to break this into four different phases: Importing Tools, Page Routes, Signup Features, and Login Features

(1) Importing Tools

First, write all the import statements for the Flask Application. These tools are essential to the rest of the Flask application. Then, you must instantiate the Flask Object and Database Instance.

The next step is to configure the database. The mysql.connector library is important use here: it allows the creator to form that intitial connection between the Flask Application and the MySQL Database. Set up the database on the host machine with specified credentials. Add those credentials to the file.

(2) Page Routes

The next phase of the Flask Application is ensuring that all pages are accessible. Before beginning this step, ensure that all HTML files are stored in the templates directory. using render_template() allows the creator to reference these pages.

Each page route will have a general format, as seen below:


@app.route('/')

def function():

  // Conditions and function work
  
  return render_template('page.html')
  


After all page routes have been defined, the creator is able to begin working on the signup and login/logout functions.


(3) Signup Features

One important feature of this function is setting the methods. This page requires GET and POST for full functionality. The general steps to follow are:


a. Determine if the request method was POST and that it contained the required information

b. Create the cursor connection to the database. This, in coordination with the execute(), fetchone(), commit(), and close() commands, will allow the page to interact with the database. These commands allow the user to add information to the database without manually logging in every time.

c. Determine if the account already exists and act accordingly.


(4) Login Features

One important feature of this function is setting the methods. This page requires GET and POST for full functionality. Additionally, this phase requires two functions: Login and Logout.


Login:

a. Determine if the request method was POST and that it contained the required information

b. Create the cursor connection to the database. This, in coordination with the execute() and fetchone() commands, will allow the page to interact with the database. These commands allow the user to compare information in the darabase without manually logging in every time.

c. Determine if the account credentials are valid and act accordingly.


Logout:

a. Pop all session details. This clears all user session data.

b. Automatically push the user back to the login page.


## Running the Program

After designing the Flask application, configure it to run at a certain location. The command to run it on the localhost in port 4444 is below:


```if __name__ == '__main__':

    app.run(host='0.0.0.0', port=4444, debug=True)```


In the terminal, simply execute the following command to begin the system:


python3 app.py


## Note - comments were added throughout app.py to assist in overall organization of the system.
