# emoji-snake

Snake with emojis in the terminal.

![emoji snake](./docs/snake.gif)

## Quick start

### Run

```sh
sh <(curl tea.xyz) poetry install
sh <(curl tea.xyz) poetry run python emoji-snake
```

### Build and run single binary

```sh
sh <(curl tea.xyz) poetry run pyinstaller -F emoji-snake/__main__.py -n emoji-snake
./dist/emoji-snake
```

## Development

Enable debugging:

```sh
DEBUG=1 pipenv run python main.py
```
