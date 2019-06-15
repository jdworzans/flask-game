from flask import Flask, render_template, Response, request, redirect
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

app = Flask(__name__)

@app.route("/help")
def help():
    return(render_template("instruction.html"))

@app.route("/", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        return(render_template("game.html", context=request.args))
    return(render_template("game.html", context=[]))

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