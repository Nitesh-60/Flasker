from flask import Flask, render_template


# 1. create a flask instance
app = Flask(__name__)

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
