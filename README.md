# Pytest BDD Template

## Requirements

- Python3
- Pipenv
- Docker

## Best Practices

- Each feature should have its own test definition.
  - Ensures each feature can run individually.
  - Test failure reporting is clearer.
- Feature files can become large and complicated. Keep them separated by functionality.
- Each feature file should have an individual directory.
- Re-use global steps as much as possible.

## Structure

- `./features`: The folder container all feature files.
- `./tests`: All the given, when and then steps plus the test definitions.
  - `/{feature}`: A folder for a feature file.
    - `given.py`: A file containing given steps specific to this feature.
    - `when.py`: A file containing when steps specific to this feature.
    - `then.py`: A file containing then steps specific to this feature.
    - `test_.py`: A file containing the test definitions.
  - `given.py`: Global given steps.
  - `when.py`: Global when steps.
  - `then.py`: Global then steps.

## Local

Build: `make buildLocal`

Run: `make run`

## Docker

Build: `make buildDocker`

Run: `make runDocker`

## Reporting

Reporting is done via Allure with a pytest BDD integration.

### How it Works

1. Running a test will generate JSON results files into `./results`.

2. Run Allure over `./results` folder to generate output HTML reports in `./reports`.

### Running Allure on Results

There are two ways to generate the Allure HTML report:

1. Use the Allure CLI.

2. Run allure docker service: `make allure`. This automatically checks for new results
and generates reports for them. **Best for local testing.**

## Logging

- Passing tests will not log.
- Failing tests will log debug.
