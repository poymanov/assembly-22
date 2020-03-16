.DEFAULT_GOAL := start

init_env:
	cp .env.example .env

migrate:
	docker-compose run web flask db upgrade

start:
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs -f

flush:
	docker-compose down -v --rmi all

import:
	docker-compose run web python import.py

init: init_env migrate import