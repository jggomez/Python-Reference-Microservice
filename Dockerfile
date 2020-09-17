FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY src/ /app/
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev --no-interaction
# set enviroment variables
ENV NEO4J_USER=neo4j
