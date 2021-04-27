from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username":"Ruairi"}
    posts =[
        {
            "author":{"username":"John"},
            "body":"Beautiful day in Portland"
        },
        {
            "author": {"username":"Susan"},
            "body": "The Avengers movie was so cool"
        }
    ]
    return render_template("index.jinja", title="Home", user=user, posts=posts)
