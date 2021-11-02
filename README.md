# Software Engineering for Machine Learning Assignment (Machine Learning Microservice)
This microservice uses a machine learning model to predict a student's likelihood of success based on **fill**, **this**, and **in**. The machine learning model is based on a **random forest (confirm?)** and the microservice is available via **HTTP request** to the endpoint **predict**, which can be called while the microservice is **deployed** as discussed in [API Documentation](https://github.com/CMU-313/fall-2021-hw4-connect5#api-documentation) below.

## Deploying the Microservice
The microservice is built in Python using Flask for the API and can be deployed in a **Docker** container.

To **build** the container, use `docker build -t ml:latest .` from the dockerfile directory, e.g.
```sh
$ pwd
path/to/fall-2021-hw4-connect5/dockerfile
$ docker build -t ml:latest .
containerIDstring
```

To **run** the container (on port 5000), use `docker run -d -p 5000:5000 ml`

## API Documentation
The **predict** endpoint, which returns a prediction of a student's success based on relevant features, can be accessed by either adding query parameters to the URL or sending an HTTP request with JSON containing the arguments.

### Parameters
**(what are the parameters, what do they mean, and why were they selected for the model?)**
**(why is this better than the baseline?)**

### Output
A single value is returned from the model. **(what is that value? how do we interpret the model's output?)**

### Query Parameters in URL
Query parameters can be appended to the URL as shown in the following example: [http://localhost:5000/predict?age=1&absences=2&health=3&G2=4](http://localhost:5000/predict?age=1&absences=2&health=3&G2=4). Make sure to include all of the arguments.

### Query with JSON
An HTTP request containing JSON can also be used to query the API. An example `curl` query follows:
```sh
$ curl \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"age":"1","absences":"2","health":"3","G2":"4"}' \
    http://localhost:5000/predictjson
```

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
**(what testing have we done? How do we run tests?)**
