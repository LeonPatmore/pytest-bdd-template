FROM python:3.8-buster
RUN pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile
RUN pipenv install
COPY features features
COPY tests tests

ENTRYPOINT ["pipenv", "run", "python", "-m", "pytest"]
CMD ["--alluredir=./results", "--clean-alluredir"]
