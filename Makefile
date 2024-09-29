.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: python
python:
	docker compose exec python-alerter bash
