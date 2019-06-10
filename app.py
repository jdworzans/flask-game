from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("base.html"))

@app.route("/play")
def play():
    return(render_template("jschessboard.html"))
