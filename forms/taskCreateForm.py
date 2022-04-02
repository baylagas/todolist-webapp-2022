from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length


class TaskCreateForm(FlaskForm):
    description = StringField(
        validators=[
            InputRequired(),
            Length(min=3, max=80),
        ],
        render_kw={"placeholder": "description..."},
    )

    isFinished = BooleanField()

    submit = SubmitField("create")
