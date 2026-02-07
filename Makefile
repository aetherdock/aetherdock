up:
	docker compose up -d --build
down:
	docker compose down
logs:
	aetherdock logs -f app
test:
	docker compose run --rm app uv run pytest -v