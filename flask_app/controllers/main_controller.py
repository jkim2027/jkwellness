from flask_app import app
from flask import render_template, redirect, url_for

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/supplements")
def supplements():
    return render_template("supps.html")

@app.route("/work-with-me")
def work():
    return render_template("work_with_me.html")

@app.route("/login")
def login():
    return render_template("login.html")