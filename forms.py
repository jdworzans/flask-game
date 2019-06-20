from flask_wtf import FlaskForm
from wtforms.fields import RadioField, StringField
from wtforms_components import ColorField


class gameForm(FlaskForm):
    row = RadioField(choices=[(1, "1"), (2, "2"), (3, "3")], default=1)
    col = RadioField(choices=[(1, "A"), (2, "B"), (3, "C")], default=1)

class startForm(FlaskForm):
    colour1 = ColorField("Kolor pierwszego gracza", default="#ff0000")
    colour2 = ColorField("Kolor drugiego gracza", default="#000000")
    username1 = StringField("Nazwa pierwszego gracza", default="Gracz 1")
    username2 = StringField("Nazwa drugiego gracza", default="Gracz 2")


