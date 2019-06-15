from flask_wtf import FlaskForm
from wtforms.fields import RadioField


class gameForm(FlaskForm):
    row = RadioField(choices=[(1, "1"), (2, "2"), (3, "3")], default=1)
    col = RadioField(choices=[(1, 'A'), (2, 'B'), (3, 'C')], default=1)
