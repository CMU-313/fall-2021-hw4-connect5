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

### Improvement from the Baseline Model
By taking in G2 as an additional feature, our retrained model achieves an f1 score of `0.986 `on the test set. In comparison, the f1 score of the baseline model on the test set is `0.519`.

Thus, our retrained model has a significantly better out-of-sample accuracy than the baseline model, which indicates better model quality.

## Testing
We had two categories of tests: unit tests on the model and integration tests for the microservice. The model unit tests take the model
and run predictions on the test data. It ensures that the model reaches desired thresholds on a number of metrics. We set the thresholds
based on what we believed to be a good accuracy goal.

The integration tests on the microservice essentially make sure that it works. It does this by sending both get and post requests to
the service and ensures they get appropriate responses. These tests require that the microservice be running already.

To run the test suite, first deploy the microservice on port 5000. Then run pytest in the parent directory.