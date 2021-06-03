
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

buildLocal:  ## Build local environment.
	pipenv install --ignore-pipfile

buildDocker:  ## Build the docker image.
	docker build -t pytest-bdd:latest .

runDocker: buildDocker  ## Run the docker image.
	docker run pytest-bdd:latest

run: buildLocal  ## Run tests locally.
	pipenv run python -m pytest --alluredir=./results/my_allure_results
