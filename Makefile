.PHONY: build run
build:
	pipenv run pyinstaller --clean main.py

run:
	dist/main/main
