#!bin/sh

sleep 5

#migrations
poetry run alembic upgrade head

#running
poetry run uvicorn --host 0.0.0.0 --port 8000 fastapi_zero.app:app