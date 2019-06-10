from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def play():
    return(render_template("game.html"))

@app.route("/help")
def help():
    return(render_template("instruction.html"))

@app.route("/about")
def about():
    return(render_template("base.html"))