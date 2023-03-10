from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 1. create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"

#  Create a form class
class NamerForm(FlaskForm):
    name = StringField("Whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

# 2. create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello world!</h1>"


# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


def index():
    first_name = "Nitesh"
    stuff = "This is bold tag"
    numbers_lst = [1,2,"twenty two","Thirty three",8]
    return render_template("index.html",
        first_name=first_name,
        stuff=stuff,
        numbers_lst = numbers_lst)


# 3. localhost:5000/user/Nitesh
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name = name)

# 4. Create a custom error page

# invalid url error
@app.errorhandler(404)

def page_not_defined(e):
    return render_template("404.html"), 404


# Internal server error
@app.errorhandler(500)

def page_not_defined(e):
    return render_template("500.html"), 500

# Create a name page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    # Validate stuff
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form submitted Successful")
    return render_template("name.html",
    name = name,
    form = form)