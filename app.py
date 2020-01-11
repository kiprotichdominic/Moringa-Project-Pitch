from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "da3f071810a37f4d8984a3fca56014fe18f40a02"
app.config["SQLALCHEMY_DATABASE_URL"]= "sqlite:///site.db"
db= SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique= True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    image_file = db.COlumn(db.String(20),nullable = False, default="default.jpg")
    password = db.Column(db.String(60), nullable = False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


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
def home():
    return render_template("index.html", posts=posts, title="Home page")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
