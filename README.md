# Simple http=>tcp proxy

## Purpose

Allow easy http exposure of syslog over tcp input service.
The tcp backend expects '\n' separated logs (this is but one variant of the syslog over tcp schemes)


## What it does

Listens in plain HTTP on port 5000.

Whenever some post request is received on /ingest, send the raw body as tcp data to the tcp backend.

If the body does not end with '\n', an '\n' is appended


## Requires

	python >=3.8.12
	flask >=2.1.2

## Run it with:



	FLASK_APP=bridge BACKEND_HOST=localhost BACKEND_PORT=12344 flask run

## Test it with:

	nc -lk 12344

	curl localhost:5000/ingest --data-binary @bob