import io

from flask import Flask, render_template, Response, request, redirect, session
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from forms import gameForm, startForm
from gameboard import draw


app = Flask(__name__)
app.secret_key = b'technologie informacyjne'

@app.route('/', methods=["GET", "POST"])
def start():
    """Returns a start page."""
    form = startForm()
    if request.method == "POST":
        col1 = form.colour1.raw_data
        col2 = form.colour2.raw_data
        username1 = form.username1.data
        username2 = form.username2.data
        session["1"] = username1
        session['2'] = username2
        session['col1'] = col1
        session['col2'] = col2
        session['progress'] = []
        session["msg"] = ""
        session["win"] = False
        session['player'] = 2
        return redirect('play')
    return render_template('start.html', form=form)

@app.route("/play", methods=["GET", "POST"])
def play():
    """Returns win or draw or game template depending on 
    session status."""
    if session["win"]:
        return(render_template("win.html", context=session, str=str))
    if len(session['progress']) == 9:
        return(render_template("draw.html", context=session, str=str))
    session["player"] = session["player"]%2 + 1
    return(render_template("game.html", context=session, str=str))

@app.route("/play/<field>/")
def move(field):
    """Returns status of game.
    
    Args: 
        field (str): contains movement coords.
    
    Returns: 
        redirects session data to play function.  """
    winnings = [set([(1,1), (1,2), (1,3)]),
                set([(2,1), (2,2), (2,3)]),
                set([(3,1), (3,2), (3,3)]),
                set([(1,1), (2,1), (3,1)]),
                set([(1,2), (2,2), (3,2)]),
                set([(1,3), (2,3), (3,3)]),
                set([(1,1), (2,2), (3,3)]),
                set([(3,1), (2,2), (1,3)])
                ]
    row = int(field[0])
    col = int(field[1])
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
        
    return redirect('/play')


@app.route("/help")
def help():
    """ Renders instruction template."""
    return(render_template("instruction.html"))

@app.route("/about")
def about():
    """Renders about template."""
    return(render_template("about.html"))

@app.route('/plot.png')
def plot_png():
    """Returns a gameboard in png format"""
    fig = draw(session['progress'], session['col1'], session['col2'])
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')