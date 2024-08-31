from flask import Flask, render_template, url_for
from forms import RegestrationForm, loginForm

app = Flask(__name__)

app.config ('SECRET_KEY') = '3a433bd12bc06288549ab103ad3df277'

posts = [
    {
        'author': 'menna',
        'title': 'love',
        'content': 'she have my heart ',
        'date_posted': 'april 21 , 2024'
    },
    {
        'author': 'braa abd elmoaty',
        'title': 'coding',
        'content': 'learning flask',
        'date_posted': 'june 16 2003'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts =posts)

@app.route("/about")
def about():
    return render_template("about.html", title= 'about')

@app.route("/regestration")
def regestration():
    form = RegestrationForm()
    return render_template("regestration.html", title='regestration', form = RegestrationForm )

@app.route("/login")
def login():
    form = loginForm()
    return render_template("login.html", title='login', form = loginForm)



if __name__ == "__main__":
    app.run(debug=True)
