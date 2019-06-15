from flask import Flask, render_template, Response, request, redirect, session
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from forms import gameForm, startForm
from plansza import rysuj
from colour import Color

app = Flask(__name__)
app.secret_key = b'technologie informacyjne'

@app.route('/', methods=["GET", "POST"])
def start():
    form = startForm()
    if request.method == "POST":
        col1 = form.colour1.raw_data
        col2 = form.colour2.raw_data
        session['col1'] = col1
        session['col2'] = col2
        session['player'] = False
        return redirect('play')
    return render_template('start.html', form=form)

@app.route("/play", methods=["GET", "POST"])
def play():
    form = gameForm()
    if request.method == "POST":
        row = int(form.row.data)
        col = int(form.col.data)
        cords = [row, col]
        if cords in session['progress']:
            session["msg"]="Wybierz inne pole, to już jest zajęte."
        else:
            session['progress'] = session['progress'] + [cords]
            session["msg"]= ""
            session["player"] = not session["player"]
        return(render_template("game.html", form=form, context=session))
    session['progress'] = []
    session["msg"] = ""
    return(render_template("game.html", form=form, context=session))

@app.route("/help")
def help():
    return(render_template("instruction.html"))

@app.route("/about")
def about():
    return(render_template("about.html"))

@app.route('/plot.png')
def plot_png():
    fig = rysuj(session['progress'], session['col1'], session['col2'])
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')