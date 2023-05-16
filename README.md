# Tokens counter API-service
Basic service counts amount of tokens for provided text.
Optional param: `DEFAULT_MODEL` with default value set to `gpt-3.5-turbo`.
All the supported models are described here:
https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

## Use
```shell
docker build --platform linux/amd64 -t tokens_counter .
docker run --platform linux/amd64 -p 8000:8000 -e DEFAULT_MODEL=davinci tokens_counter
```
API docs: http://0.0.0.0:8000/docs

## Contribute
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```
