PY=python3
VENV=.venv
PIP=$(VENV)/bin/pip
PYBIN=$(VENV)/bin/python
IMAGE_NAME=rag-project
DOCKER_TAG=rag-project:latest

.PHONY: help venv install test nbconvert docker-build docker-run publish

help:
	@echo "make venv - create virtualenv"
	@echo "make install - install dependencies"
	@echo "make test - run tests"
	@echo "make docker-build - build docker image"
	@echo "make docker-run - run docker container"

venv:
	$(PY) -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

test:
	$(PYBIN) -m pytest -q

docker-build:
	docker build -t $(DOCKER_TAG) .

docker-run:
	docker run --rm -p 8080:8080 $(DOCKER_TAG)
