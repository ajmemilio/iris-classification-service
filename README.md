# Iris dataset classification - API

This project aims to train a XGBoost model to classify iris flower. 

https://archive.ics.uci.edu/ml/datasets/iris

### Building and run

API based on:

* nginx: high performance proxy server
* gunicorn: a python Web Server Gateway Interface HTTP server
* Flask: a popular python web server library
* Flask-RESTPlus: an extension of Flask for quickly building REST APIs

#### Requirements

* Docker

* Docker Compose

To run the application just run the following commands:

```
docker build -t iris-classification .
docker-compose up
```

Then http://0.0.0.0:8000 is available with a ```POST``` resource and body like:

```
{
	"sepal_length": 6.7, 
	"sepal_width": 3.2,
	"petal_length": 5.1, 
	"petal_width": 2.5
}
```


