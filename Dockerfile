FROM docker.io/tiangolo/meinheld-gunicorn-flask:python3.8

# prepare image
RUN rm /app/prestart.sh /app/main.py
ENV MODULE_NAME=app
RUN pip3 install --no-cache-dir -U pip pipenv

# install python dependencies
WORKDIR /app
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --ignore-pipfile

# add remaining sources
COPY app.py /app/
COPY content /app/content/
COPY static /app/static/
COPY templates /app/templates/

# add image metadata
LABEL org.opencontainers.image.source = "https://github.com/timonegk/group-ctf.de"

