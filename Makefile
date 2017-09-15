
.PHONY: clean build test release

clean:
	@python setup.py clean --all

build: clean
	@python setup.py build

test: 
	@python -m unittest

release: clean
	@python setup.py sdist
	@python setup.py sdist