# Serverless Flask Sample

Simple fully managed API server using API Gateway, Lambda, DynamoDB and Flask. And deploy the infrastructure by [serverless framework](https://serverless.com/).

## Tools & Packages

* [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
* [serverless](https://serverless.com/) 1.27.3 (npm package)
* [serverless-wsgi](https://github.com/logandk/serverless-wsgi) 1.4.8
* [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements) 4.1.0
* [Flask](http://flask.pocoo.org/) 1.0.2 (API server)
* Python 3.6.1 (by pyenv)
* aws-cli 1.15.45 (by pyenv)
* node v10.5.0 (by ndenv)

## Prerequisite

* node.js (npm) greater than or equal to v4
* aws account
* awscli

## Setup & Deploy

```
# Download source
git clone git@github.com:nipe0324/serverless-flask-sample.git
cd serverless-flask-sample

# Install serverless globally
npm install serverless -g

# Deploy to aws
serverless deploy -v

# Remove deplyed resources
serverless remove
```

## Samples

```
export SLS_ENDPOINT=https://m56ha23xqf.execute-api.ap-northeast-1.amazonaws.com/dev

# get all todo list
curl ${SLS_ENDPOINT}/todos
> [ ]

# get a todo
curl ${SLS_ENDPOINT}/todos/1
> {"error":"Not found"}

# create a todo
curl ${SLS_ENDPOINT}/todos -X POST -H "Content-Type: application/json" -d '{"title": "Shopping"}'
> {"id":"1","title":"Shopping"}

# get a todo again
curl ${SLS_ENDPOINT}/todos/1
> {"id":"1","title":"Shopping"}

# update a todo
curl ${SLS_ENDPOINT}/todos/1 -X PUT -H "Content-Type: application/json" -d '{"title": "Shopping 2"}'
> {"id":"1","title":"Shopping 2"}

# get all todo list
curl ${SLS_ENDPOINT}/todos
> [{"id":"1","title":"Shopping 2"}]

# remove a todo
curl ${SLS_ENDPOINT}/todos/1 -X DELETE -H "Content-Type: application/json"
> {"success":true}

# get all todo list
curl ${SLS_ENDPOINT}/todos
> [ ]
```
