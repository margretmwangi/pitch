import os
from flask import Flask, render_template,redirect,url_for
from flask_login import LoginManager,login_user,current_user,login_required,logout_user

from wtform_fields import *
from models import *


# Configure app
app = Flask(__name__)
app.secret_key =os.environ.get("SECRET")


# Configure database
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Configure flask login
login = LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):

    return User.query.get(init(id))

    User.query.get(init(id))

@app.route("/",methods=['GET','POST'])
def index():

    # Updated database if validation success
 
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username =reg_form.username.data
        password = reg_form.password.data
        # Hash password

    hashed_pswd =pbkdf2_sha256.hash(password)


        
        # Add user to DB
user = User(username=username,password=password)
db.session.add(user)
db.session.commit()

flash('Registered successfully.Please log in.','success')
return redirect (url_for(login)


    return render_template("index.html",form=reg_form)

@app.route("/login",methods=['GET','POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
        user_object=
        User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return  redirect(url_for('pitch'))

      
        return render_template("login.html",form=login_form)

        @app.route("/pitch",methods=['GET','POST'])
        
        def pitch():

            if  not current_user.username.is authenticated:
                flash ('Please login', 'danger')
                return "please log in to access the pitch page"

        return "pitch with me"

        @app.route("/logout",methods=['GET'])
        def logout():

            logout_user()
            flash('You are logged out successfully','success')
            
            return redirect (url_for('pitch'))


    if __name__ == __main__:
        app.run(debug=True)