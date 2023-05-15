# Basic tokens counter API-service

# Use
```shell
docker build -t tokens_counter .
docker run -p 8000:8000 tokens_counter:latest
```

API docs: http://0.0.0.0:8000/docs

# Contribute
```shell
poetry install
poetry run uvicorn src.main:app
```
