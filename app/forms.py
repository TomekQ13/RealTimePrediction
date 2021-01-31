from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.fields.core import RadioField
from wtforms.validators import AnyOf, InputRequired

class FieldsRequiredForm(FlaskForm):
    """Require all fields to have content. This works around the bug that WTForms radio
    fields don't honor the `DataRequired` or `InputRequired` validators.
    """

    class Meta:
        def render_field(self, field, render_kw):
            render_kw.setdefault('required', True)
            return super().render_field(field, render_kw)

class PredictDataForm(FieldsRequiredForm):
    passenger_class = RadioField('Passenger class', choices=[(1, 'First'), (2, 'Second'), (3, 'Third')], coerce=int)
    sex = RadioField('Sex', choices=[(0, 'Male'), (1, 'Female')], coerce=int)
    age = IntegerField('Age', validators=[InputRequired()])
    siblings_or_spouse = IntegerField('Number of siblings or spouses aboard', validators=[InputRequired()])
    parch = IntegerField('Number of parents or children aboard', validators=[InputRequired()])
    fare = IntegerField('Fare', validators=[InputRequired()])
    embarked = StringField('Embarked', validators=[InputRequired(), AnyOf(['cherbourg', 'queenstown', 'southampton'])])
    embarked = RadioField('Embarked', choices=[('cherbourg', 'Cherbourg'), ('queenstown', 'Queenstown') ,('southampton', 'Southampton')])
    submit = SubmitField('Submit')

