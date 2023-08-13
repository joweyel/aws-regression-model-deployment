install:
	pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
	python3 -m pytest -vv tests.py

lint:
	pylint --disable=R,C main.py

all: install lint test