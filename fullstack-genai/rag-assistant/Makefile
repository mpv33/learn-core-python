.PHONY: install dev backend frontend test clean

install:
	cd backend && python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
	cd frontend && npm install

dev:
	@echo "Starting backend :8000 and frontend :3000"
	@(cd backend && .venv/bin/uvicorn app.main:app --reload --host 127.0.0.1 --port 8000) & \
	(cd frontend && npm run dev)

backend:
	cd backend && .venv/bin/uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

frontend:
	cd frontend && npm run dev

test:
	cd backend && .venv/bin/pytest tests/ -v

clean:
	rm -rf backend/data backend/.venv frontend/node_modules frontend/.next
