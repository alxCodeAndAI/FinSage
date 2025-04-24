install:
	pip install --upgrade pip &&\
	pip install -r requeriments.txt

test:
	python -m pytest -vv test_*.py

format:	
	black *.py 

lint:
	pylint  *.py
		
all: install lint test format 