.PHONY: install build run
install:
	pipenv install

build:
	pipenv run pyinstaller main.py

run: dist/main/main
	dist/main/main
