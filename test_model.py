import joblib
import sklearn
import pytest


@pytest.fixture
def data():
    return joblib.load('dockerfile/apps/model-data.pkl')

@pytest.fixture
def model():
    return joblib.load('dockerfile/apps/model.pkl')

def test_f1score(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.f1_score(y_test, pred, average='binary')
    assert score >= .8

def test_accuray(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.accuracy_score(y_test, pred)
    assert score >= .9

def test_log_loss(model, data):
    x_test, y_test = data
    pred = model.predict(x_test)
    score = sklearn.metrics.log_loss(y_test, pred)
    assert score <= 0.2