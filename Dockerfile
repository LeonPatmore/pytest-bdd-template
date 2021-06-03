FROM python:3.8-buster
RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install
