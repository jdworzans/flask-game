from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
<<<<<<< HEAD
def index():
    return(render_template("base.html"))

@app.route("/play")
def play():
    return(render_template("jschessboard.html"))
=======


@app.route("/help")
def help():
    return(render_template("instruction.html"))

@app.route("/about")
def about():
    return(render_template("base.html"))
>>>>>>> a629b9973f1beaaf9732d63c8a726bbc6055c269
