from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AccomplishmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    discipline = StringField('Discipline', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')