from flask import Flask, render_template, url_for

app = Flask(__name__)


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




if __name__ == "__main__":
    app.run(debug=True)
