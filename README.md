# irc-backend-api

Work in progress Web API for accessing IRC chat logs stored in Elasticsearch.

_License: GNU AGPLv3_

#### Notes

Elasticsearch (written for version 7) must be installed in the default configuration locally (without passwords etc.) for the script to work.

### irc_api.py

Web REST API using FastAPI to process requests for IRC data.

### irc_elastic.py

Interface for submitting IRC queries and working with Elasticsearch.

## Python Setup

1. Setup a Python virtual environment (optional): `virtualenv -p python3 pyenv`
1. Enter the Python virtual environment (optional): `source pyenv/bin/activate`
2. Install Requirements using pip: `pip install -r requirements.txt`
