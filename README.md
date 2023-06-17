# vicunapi
Overly simplistic API serving vicuna 13b via fastapi

# build and run

## using docker
if you are using poetry and messed with dependencies, make sure to persist them in requirements.txt by running (w/o hashes to reduce time to resolve dependencies):
`poetry export --without-hashes --format=requirements.txt > requirements.txt`

otherwise simply run:
* `docker build -t vicunapi .`
* `docker run --rm -p 5444:8000 vicunapi`

-- will take a while as it downloads vicuna 13b (approx 9GB) into the container

## locally
use poetry
* `poetry install`
* `poetry run python vicunapi.py`

# use
check out http://0.0.0.0/5444/docs to play around with the single `/prompt` endpoint

# TODO
* find way to respond async
* option to stream result
* use authentication and sessions
* make compatible with llamaindex and other popular wrappers