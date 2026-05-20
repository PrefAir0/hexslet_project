install:
	uv sync

brain-games:
	uv run brain-games

build: 
	uv build

init:
	uv run ruff check brain_games

	