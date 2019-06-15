from flask_wtf import FlaskForm
from wtforms.fields import RadioField
from wtforms_components import ColorField


class gameForm(FlaskForm):
    row = RadioField(choices=[(1, "1"), (2, "2"), (3, "3")], default=1)
    col = RadioField(choices=[(1, 'A'), (2, 'B'), (3, 'C')], default=1)

class startForm(FlaskForm):
    colour1 = ColorField(label="colour1", default="#ff0000")
    colour2 = ColorField(label="colour2", default="#000000")
