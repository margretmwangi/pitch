from flask import Flask, render_template,redirect,url_for

from wtform_fields import *
from models import *


# Configure app
app = Flask(__name__)
app.secret_key ='later'


# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://slxchntbrzumdb:6b63f8c71961cbd533796cd453f9c722ff9a4ecd44ee3d724620d96495572a06@ec2-3-222-30-53.compute-1.amazonaws.com:5432/d73usrh8cslhie'
db = SQLAlchemy(app)



@app.route("/",methods=['GET','POST'])
def index():

    # Updated database if validation success
 
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username =reg_form.username.data
        password = reg_form.password.data

        
        # Add user to DB
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect (url_for(login)

         return render_template("index.html",form=reg_form)

@app.route("/login",methods=['GET','POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        return "logged in finally"

        return render_template("login.html",form=login_form)
    if __name__ == __main__:
        app.run(debug=True)