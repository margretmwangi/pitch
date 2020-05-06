from flask import Flask, render_template

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

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username =reg_form.username.data
        password = reg_form.password.data

        # Check username exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "name taken!"
        
        # Add user to DB
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return "good work"

    return render_template("index.html",form=reg_form)


    if __name__ == __main__:
        app.run(debug=True)