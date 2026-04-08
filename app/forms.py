# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, TextAreaField
from wtforms.validators import DataRequired,InputRequired, ValidationError
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired("Please enter the title")], render_kw={"placeholder": "Enter the movie title"})
    description = TextAreaField('Description', validators=[DataRequired("Please enter the description")], render_kw={"placeholder": "Enter the movie description"})
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Only JPG and PNG files are allowed")], render_kw={"placeholder": "Upload a movie poster"})