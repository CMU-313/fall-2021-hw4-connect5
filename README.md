# Software Engineering for Machine Learning Assignment (Machine Learning Microservice)
This microservice uses a machine learning model to predict a student's likelihood of success based on **fill**, **this**, and **in**. The machine learning model is based on a **random forest (confirm?)** and the microservice is available via **HTTP request** to the endpoint **predict**, which can be called as discussed below in **API Documentation** while the microservice is **deployed**.

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
Query parameters can be appended to the URL as shown in the following example: [http://localhost:5000/predict?age=10&absences=5&health=1](http://localhost:5000/predict?age=10&absences=5&health=1) **(replace with whatever is actually decided on)**). Make sure to include all of the arguments.

### Query with JSON
An HTTP request containing JSON can also be used to query the API. An example `curl` query follows:
```sh
$ curl \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"age":"10","absences":"5","health":"1"}' \
    http://localhost:5000/predictjson
```

## Testing
**(what testing have we done? How do we run tests?)**