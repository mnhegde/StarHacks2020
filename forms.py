from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class NewFarmForm(FlaskForm):

    
    farmname = StringField('Farm name:', validators=[DataRequired()])
    address = StringField('Cords:', validators=[DataRequired()])
    farmtype = StringField('Farm Type:', validators=[DataRequired()])
    about = StringField('About:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')