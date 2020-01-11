from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"]= "da3f071810a37f4d8984a3fca56014fe18f40a02"

posts = [
    {
        "author": "Kiprotich",
        "title": "First Blog post",
        "content": "My first content",
        "date_posted": "April 20, 2019"
    },
    {
        "author": "Kiprotich Dominic",
        "title": "First Blog post",
        "content": "My first content",
        "date_posted": "April 20, 2020"
    }
]


@app.route('/')
@app.route("/home")
def index():
    return render_template("index.html", posts = posts, title = "Home page")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title = "Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login")


if __name__ == '__main__':
    app.run()
