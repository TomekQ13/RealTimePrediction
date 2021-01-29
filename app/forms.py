from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, SubmitField
from wtforms.validators import AnyOf, DataRequired, NumberRange


class PredictDataForm(FlaskForm):
    passenger_class = IntegerField('Passenger class', validators=[DataRequired(), NumberRange(min=1, max=3)])
    is_female = BooleanField('Gender', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    siblings_or_spouse = IntegerField('Number of siblings or spouses aboard', validators=[DataRequired()])
    parch = IntegerField('Number of parents or children aboard', validators=[DataRequired()])
    fare = IntegerField('Fare', validators=[DataRequired()])
    embarked = StringField('Embarked', validators=[DataRequired(), AnyOf(['cherbourg', 'queenstown', 'southampton'])])
    submit = SubmitField('Submit')
