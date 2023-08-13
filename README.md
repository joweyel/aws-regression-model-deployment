# aws-regression-model-deployment
Example code for a regression model that can be deployed in AWS.

## How to use the model on AWS
- Get the Github Repository or create a new one with your own code
- Open AWS and create a new `Cloud9`-Instance
- Use the console to create a pair of ssh-keys
  ```bash
  ssh-keygen -t rsa # other key-types also available
  ```
- Add the public ssh-key to Github
- The `Makefile` is already generated and contains the following rules
```make
install:
    pip install --upgrade pip &&\
		    pip install -r requirements.txt

test:
    python3 -m pytest -vv test_model.py

lint:
    pylint --disable=R,C main.py

all: install lint test
```

- The requirements-file include the following Python-packages:
```
pylint
pytest
pytest-cov
black
click
numpy
matplotlib
scikit-learn
```

- To install the requirements, create a Python virtual environment with the following commands
```bash
python3 -m venv ~/.reg-env
source ~/.reg-env/bin/activate
```

- Code for the Regression Model can be found in the following locations
    - `Main Program`: [main.py](./main.py)
    - `Utility-functions`: [util.py](./util.py)
    - `Test Code`: [tests.py](./tests.py)

- Run make all which will `install`, `lint` and `test` the code.
- Now the configuration for Github Actions is set up as [aws-ml-app.yml](.github/workflow/aws-ml-app.yml)

