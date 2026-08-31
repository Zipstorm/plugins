.PHONY: build validate test check clean

build:
	python3 scripts/build.py

validate:
	python3 scripts/validate.py

test:
	python3 -m unittest discover -s tests -v

check: validate test

clean:
	python3 scripts/build.py --clean
