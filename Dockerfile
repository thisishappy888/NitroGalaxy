FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry

RUN pip install --upgrade poetry

RUN poetry install --no-root 

COPY . .

CMD ["poetry", "run", "python", "bot.py"]
