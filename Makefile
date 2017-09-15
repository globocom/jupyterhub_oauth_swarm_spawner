
.PHONY: clean build test release

clean:
	@python setup.py clean --all

build: clean
	@python setup.py build

test: 
	@python -m unittest

release: clean
	@python setup.py sdist #upload -r pypi-local
	@python setup.py sdist #upload -r ipypi-local