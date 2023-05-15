# Tokens counter API-service
Basic service counts amount of tokens for provided text.
Optional param: `DEFAULT_MODEL` with default value set to `gpt-3.5-turbo`.
All the supported models are described here:
https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

## Use
```shell
docker build -t tokens_counter .
docker run -p 8000:8000 -e DEFAULT_MODEL=gpt-4 tokens_counter:latest
```
API docs: http://0.0.0.0:8000/docs

## Contribute
```shell
poetry install
poetry run uvicorn src.main:app
```
