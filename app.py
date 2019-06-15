from flask import Flask, render_template, Response, request, redirect, session
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from forms import gameForm

app = Flask(__name__)
app.secret_key = b'technologie informacyjne'

@app.route("/help")
def help():
    return(render_template("instruction.html"))

@app.route("/", methods=["GET", "POST"])
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
        return(render_template("game.html", form=form, context=session))
    session['progress'] = []
    session["msg"] = ""
    return(render_template("game.html", form=form, context=session))

@app.route("/about")
def about():
    return(render_template("about.html"))

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig