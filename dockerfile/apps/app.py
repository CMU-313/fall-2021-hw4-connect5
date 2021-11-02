from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)


def query_model(data):
    # Note: param order matters, need to match order when calling `clf.fit()`
    query_df = pd.DataFrame({
        'G2': pd.Series(data[0][0]),
        'absences': pd.Series(data[1][0]),
        'age': pd.Series(data[2][0]),
        'health': pd.Series(data[3][0])
    })
    prediction = clf.predict(query_df)
    return jsonify(np.asscalar(prediction))


@app.route('/')
def hello():
    return "try the predict route it is great!"


@app.route('/predict')
def predict():
    required_params = ['age', 'absences', 'health', 'G2']
    # Check that all required parameters are present and of the correct type
    for param in required_params:
        if not param in request.args:
            # Return HTTP 400 error if missing parameter
            return "Missing parameter: " + param, 400

        if request.args.get(param, type=float) is None:
            # Return HTTP 400 error if parameter is of the wrong type
            return f"Invalid type for {param}. Expected int/float.", 400

    age = request.args.get('age', type=float)
    absences = request.args.get('absences', type=float)
    health = request.args.get('health', type=float)
    g2 = request.args.get('G2', type=float)

    data = [[g2], [absences], [age], [health]]
    return query_model(data)


@app.route('/predictjson', methods=['POST'])
def predictjson():
    required_params = ['age', 'absences', 'health', 'G2']
    # Check that all required parameters are present and of the correct type
    for param in required_params:
        if not param in request.json:
            # Return HTTP 400 error if missing parameter
            return "Missing parameter: " + param, 400

        if (not isinstance(request.json[param], float) and
                not isinstance(request.json[param], int)):
            # Return HTTP 400 error if parameter is of the wrong type
            return f"Invalid type for {param}. Expected int/float.", 400

    age = request.json['age']
    absences = request.json['absences']
    health = request.json['health']
    g2 = request.json['G2']

    data = [[g2], [absences], [age], [health]]
    return query_model(data)


if __name__ == '__main__':
    clf = joblib.load('/apps/improved_model.pkl')
    app.run(host="0.0.0.0", debug=True)
