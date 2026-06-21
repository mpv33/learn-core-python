.PHONY: install run dev test migrate docker-up docker-down clean

install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

test:
	pytest tests/ -v

migrate:
	alembic upgrade head

migrate-new:
	@read -p "Migration message: " msg; alembic revision --autogenerate -m "$$msg"

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -f task_api.db
