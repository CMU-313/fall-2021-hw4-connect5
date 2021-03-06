# Software Engineering for Machine Learning Assignment (Machine Learning Microservice)
This microservice uses a machine learning model to predict a student's likelihood of success based on age, absences, health, and their second period grades. The machine learning model is based on a **random forest classifier** and the microservice is available via **HTTP request** through the `/predict` and `/predictjson` endpoints, which can be called while the microservice is **deployed** as discussed in [API Documentation](https://github.com/CMU-313/fall-2021-hw4-connect5#api-documentation) below.

## Deploying the Microservice
The microservice is built in Python using Flask for the API and can be deployed in a **Docker** container.

To **build** the container, use `docker build -t ml:latest .` from the dockerfile directory, e.g.
```sh
$ pwd
path/to/fall-2021-hw4-connect5/dockerfile
$ docker build -t ml:latest .
containerIDstring
```

To **run** the container (on port `5000`), use `docker run -d -p 5000:5000 ml`

## API Documentation
There are two available API endpoints for accessing the model: `/predict` and `/predictjson`.

### `/predict`
The `/predict` endpoint accepts a `GET` request with the following required query arguments:
|Parameter|Description|
|---|---|
|`age`|Student's age (numeric: 15 to 22)|
|`absences`|Number of school absences (numeric: 0 to 93)|
|`health`|Current health status (numeric: 1 (very bad) to 5 (very good))|
|`G2`|Second period grade (numeric: 0 to 20)|

An example request is [http://localhost:5000/predict?age=1&absences=2&health=3&G2=4](http://localhost:5000/predict?age=1&absences=2&health=3&G2=4)

### `/predictjson`
The `/predictjson` endpoint accepts a `POST` request with the same required arguments as `/predict` but specified as JSON in the *body* of the request as seen in the example below (all numeric values as placeholders):
```json
{
    "age": 1,
    "absences": 2,
    "health": 3,
    "G2": 4
}
```

An example `curl` query follows:
```sh
$ curl \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"age":1,"absences":2,"health":3,"G2":4}' \
    http://localhost:5000/predictjson
```

### Output
The output is a scalar value: `0` or `1`, which corresponds to whether or not a student is predicted to be successful by the end of the year, as measured by their final grade. A value of `1` means that a student is predicted to be successful whereas `0` means otherwise.

## Model Description

### Input Features
The features we used in training our model are `health`, `absences`, `age`, and `G2`.

We decided to based our model on these 4 features because through our experimentations, we found that `health`, `absences`, `age`, and `G2` are the top 4 most influential features for predicting `G3`.

### Improvement from the Baseline Model
By taking in `G2` as an additional feature, our retrained model achieves 

1. 0.9285714285714286 f1 score on the test set.
2. 0.9746835443037974 accuracy on the test set.
3. 0.874409523889261 log loss on the test set.

In comparison, the baseline model only has

1. 0.17391304347826086 f1 score on the test set.
2. 0.759493670886076 accuracy on the test set.
3. 8.306865173231825 log loss on the test set.

Thus, our retrained model has a significantly better out-of-sample performance than the baseline model, which indicates better model quality.

## Testing
We had two categories of tests: unit tests on the model and integration tests for the microservice. 

The model unit tests take the model
and run predictions on the test data. It ensures that the model reaches desired thresholds on a number of metrics. We set the thresholds
based on what we believed to be a good accuracy goal. We chose these unit tests to establish an idea of when our model would be "good enough".

The integration tests on the microservice ensure that the API works as expected. It does this by sending both `GET` and `POST` requests to
the service and ensures they get appropriate responses. These tests require that the microservice be running already.

To run the test suite, first deploy the microservice on port `5000`. Then run `pytest` in the parent directory.

These tests are automatically run on GitHub Actions for every commit and pull request to the master branch.
