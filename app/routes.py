from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/car', methods = ["GET", "POST"])
def add_event_car():
    if request.method == "GET":
        print("hello u use a car")
        return render_template("newevent.html")
    else:
        print("world")
        
@app.route('/bus', methods = ["GET", "POST"])
def add_event_bus():
    if request.method == "GET":
        print("hello u use a bus")
        return render_template("newevent.html")
    else:
        print("world")

@app.route('/train', methods = ["GET", "POST"])
def add_event_train():
    if request.method == "GET":
        print("hello u use a train")
        return render_template("newevent.html")
    else:
        print("world")

@app.route('/plane', methods = ["GET", "POST"])
def add_event_plane():
    if request.method == "GET":
        print("hello u use a plane")
        return render_template("newevent.html")
    else:
        print("world")

@app.route('/walk', methods = ["GET", "POST"])
def add_event_walk():
    if request.method == "GET":
        print("hello u use a walk")
        return render_template("newevent.html")
    else:
        print("world")

@app.route('/bicycle', methods = ["GET", "POST"])
def add_event_bicycle():
    if request.method == "GET":
        print("hello u use a bicycle")
        return render_template("newevent.html")
    else:
        print("world")
 
@app.route('/boat', methods = ["GET", "POST"])
def add_event_bioat():
    if request.method == "GET":
        print("hello u use a boat")
        return render_template("newevent.html")
    else:
        print("world")