from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.fields.core import RadioField
from wtforms.validators import AnyOf, DataRequired, InputRequired, NumberRange


class PredictDataForm(FlaskForm):
    passenger_class = IntegerField('Passenger class', validators=[InputRequired(), NumberRange(min=1, max=3, message='Possible classes: 1, 2 or 3.')])
    sex = RadioField('Sex', choices=[(0, 'Male'), (1, 'Female')], coerce=int)
    age = IntegerField('Age', validators=[InputRequired()])
    siblings_or_spouse = IntegerField('Number of siblings or spouses aboard', validators=[InputRequired()])
    parch = IntegerField('Number of parents or children aboard', validators=[InputRequired()])
    fare = IntegerField('Fare', validators=[InputRequired()])
    embarked = StringField('Embarked', validators=[InputRequired(), AnyOf(['cherbourg', 'queenstown', 'southampton'])])
    embarked = RadioField('Embarked', choices=[('cherbourg', 'Cherbourg'), ('queenstown', 'Queenstown') ,('southampton', 'Southampton')])
    submit = SubmitField('Submit')

