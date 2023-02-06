from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class searchPoke(FlaskForm):
    searchBody = StringField('Search', validators=[DataRequired(), Length(min=1, max=45)])
    search = SubmitField('Search')