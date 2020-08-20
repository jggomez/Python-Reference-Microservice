FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY src/ /app/
COPY Pipfile /app
COPY Pipfile.lock /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
# set enviroment variables
ENV NEO4J_USER=neo4j
