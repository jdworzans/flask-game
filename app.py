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
        session['progress'] = []
        session["msg"] = ""
        session["win"] = False
        session['player'] = 1
        return redirect('play')
    return render_template('start.html', form=form)

@app.route("/play", methods=["GET", "POST"])
def play():
    if session["win"]:
        return(render_template("win.html", context=session))
    if len(session['progress']) == 9:
        return(render_template("draw.html", context=session))
    return(render_template("game.html", context=session))

@app.route("/play/<pole>/")
def move(pole):
    winnings = [set([(1,1), (1,2), (1,3)]),
                set([(2,1), (2,2), (2,3)]),
                set([(3,1), (3,2), (3,3)]),
                set([(1,1), (2,1), (3,1)]),
                set([(1,2), (2,2), (3,2)]),
                set([(1,3), (2,3), (3,3)]),
                set([(1,1), (2,2), (3,3)]),
                set([(3,1), (2,2), (1,3)])
                ]
    row = int(pole[0])
    col = int(pole[1])
    cords = (row, col)
    if cords in session['progress']:
        session["msg"]="Wybierz inne pole, to już jest zajęte."
    else:
        session['progress'].append(cords)
        moves = set(session['progress'][session['player']-1::2])
        for win in winnings:
            if win.issubset(moves):
                session["win"] = True
        session["msg"]= ""
        session["player"] = session["player"]%2 + 1
    return redirect('/play')


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