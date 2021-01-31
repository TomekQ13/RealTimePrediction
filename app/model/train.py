import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import numpy as np
import json
import joblib

model_folder = Path('app/model/')

def trainModel():
    train = pd.read_csv(model_folder / 'train.csv')
    train['Sex'].replace({'male': 0, 'female':1}, inplace = True)
    train = train[train['Age'].isnull() == False]
    train = train[train['Embarked'].isnull() == False]
    train = pd.concat([train,  pd.get_dummies(train['Embarked'], prefix = 'Embarked')], axis=1)
    train.drop(columns=['Name', 'Ticket' ,'Cabin', 'Embarked', 'Embarked_C', 'PassengerId'], inplace = True)

    scaling_params = {
    'age_std': train['Age'].std(),
    'age_mean': train['Age'].mean(),
    'fare_std': train['Fare'].std(),
    'fare_mean': train['Fare'].mean()    
    }
    with open(model_folder / 'scaling_params.json', 'w') as result:
        json.dump(scaling_params, result)

    train['Age'] = (train['Age'] - scaling_params['age_std'])/scaling_params['age_mean']
    train['Fare'] = (train['Fare'] - scaling_params['fare_std'])/scaling_params['fare_mean']

    y = train['Survived'].copy()
    X = train.drop(columns='Survived')

    classifier = RandomForestClassifier()
    classifier.fit(X,y)

    filename = model_folder / 'model_params.sav'
    joblib.dump(classifier, open(filename, 'wb'))

if __name__ == '__main__':
    trainModel()