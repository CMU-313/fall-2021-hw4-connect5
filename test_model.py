import joblib
import sklearn
import pytest
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd


@pytest.fixture
def data():
    np.random.seed(17313)
    df = pd.read_csv('data/student-mat.csv', sep=';')
    include = ['health', 'absences','age','G2','G3']
    df.drop(columns=df.columns.difference(include), inplace=True)
    df['qual_student'] = np.where(df['G3']>=15, 1, 0)
    df.drop(columns='G3', inplace=True)
    dependent_variable = 'qual_student'
    x = df[df.columns.difference([dependent_variable])]
    y = df[dependent_variable]
    _, x_test, _, y_test= train_test_split(x, y, test_size=0.2)
    return x_test, y_test

@pytest.fixture
def model():
    return joblib.load('dockerfile/apps/improved_model.pkl')

def test_f1score(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.f1_score(y_test, pred, average='binary')
    assert score >= .9

def test_accuray(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.accuracy_score(y_test, pred)
    assert score >= .95

def test_log_loss(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.log_loss(y_test, pred)
    assert score <= 1.5
