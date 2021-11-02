from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)


def query_model(data):
    query_df = pd.DataFrame({
        'age': pd.Series(data[0][0]),
        'health': pd.Series(data[1][0]),
        'absences': pd.Series(data[2][0]),
        'G2': pd.Series(data[3][0])
    })
    prediction = clf.predict(query_df)
    return jsonify(np.asscalar(prediction))


@app.route('/')
def hello():
    return "try the predict route it is great!"


@app.route('/predict')
def predict():
    # use entries from the query string here but could also use json
    age = request.args.get('age')
    absences = request.args.get('absences')
    health = request.args.get('health')
    g2 = request.args.get('G2')
    data = [[age], [health], [absences], [g2]]
    return query_model(data)


@app.route('/predictjson', methods=['POST'])
def predictjson():
    age = request.json['age']
    absences = request.json['absences']
    health = request.json['health']
    g2 = request.json['G2']
    data = [[age], [health], [absences], [g2]]
    return query_model(data)


if __name__ == '__main__':
    clf = joblib.load('/apps/improved_model.pkl')
    app.run(host="0.0.0.0", debug=True)
