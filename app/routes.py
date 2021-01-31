from flask import render_template, flash, url_for, redirect
from flask.blueprints import Blueprint
from pathlib import Path
import numpy as np
import json
import joblib

from app.forms import PredictDataForm
from app.model.train import trainModel

main = Blueprint('main', __name__)
model_folder = Path('app/model/')

@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    filename = model_folder / 'model_params.sav'    
    classifier = joblib.load(filename)

    with open(model_folder / 'scaling_params.json') as file:
        scaling_params = json.load(file)

    embarked_q = 0
    embarked_s = 0
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
        values = np.array([
            form.passenger_class.data,
            form.sex.data,
            (form.age.data - scaling_params['age_std'])/scaling_params['age_mean'],
            form.siblings_or_spouse.data,
            form.parch.data,
            (form.fare.data - scaling_params['fare_std'])/scaling_params['fare_mean'],
            embarked_q,
            embarked_s
        ])

        prediction = classifier.predict_proba(np.reshape(values,(1,-1)))[0][1]
        return render_template('home.html', form=form, prediction=prediction)

    return render_template('home.html', form=form)

@main.route('/train')
def train():
    try:
        trainModel()
        flash('The model has been retrained', 'success')
    except Exception as e:
        flash('There were issues when attempting to retrain the model. The model has not been retraied', 'warning')
        
    return redirect(url_for('main.home'))