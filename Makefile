install:
	pip install --upgrade pip &&\
	pip install -r requeriments.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C *.py
		
run:
	python main.py

all: install lint test format run