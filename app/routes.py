from flask import render_template
from flask.blueprints import Blueprint
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import json

from app.forms import PredictDataForm
from app.model.modelLoaderSaver import modelLoaderSaver

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    classifier = RandomForestClassifier()
    loader = modelLoaderSaver(classifier)
    loader.load('app\model\model_params.txt')

    with open('app\model\scaling_params.json') as file:
        scaling_params = json.load(file)

    form = PredictDataForm()
    if form.validate_on_submit():
        if form.embarked.data == 'cherbourg':
            embarked_q = 0
            embarked_s = 0
        elif form.embarked.data == 'queenstown':
            embarked_q = 1
            embarked_s = 0
        elif form.embarked.data == 'southampton':
            embarked_q = 0
            embarked_s = 1
        else:
            raise ValueError('Incorrect embarked value. Value must cherbourg, queenstown or southampton.')

        values = np.array([
            form.passenger_class.data,
            int(form.is_female.data),
            (form.age.data - scaling_params['age_std'])/scaling_params['age_mean'],
            form.siblings_or_spouse.data,
            form.parch.data,
            (form.fare.data - scaling_params['fare_std'])/scaling_params['fare_mean'],
            embarked_q,
            embarked_s
        ], dtpye=np.int64)

        prediction = classifier.predict_proba(np.reshape(values,(1,-1)))
        return render_template('home.html', prediction=prediction)

    return render_template('home.html')
