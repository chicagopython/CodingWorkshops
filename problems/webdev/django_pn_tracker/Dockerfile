FROM python:3.7
LABEL maintainer="Joe Jasinski"

# install OS dependencies
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

ENV SITE_DIR=/app/

# add application user and group
RUN groupadd -r app && \
    useradd -r -g app -d ${SITE_DIR} -s /sbin/nologin -c "Docker image user" app

# create that base directory with proper permissions
RUN install -g app -o app -d ${SITE_DIR}

# set the default working directory to the app dir
WORKDIR ${SITE_DIR}

# Create a few more directories for use by the app and set permissions
RUN install -g app -o app -d proj/ htdocs/ htdocs/static/
RUN find ${SITE_DIR} -type d -exec chmod g+s {} \;
RUN chmod -R g+w ${SITE_DIR}

# from here on, run everything as the "app" user
USER app

RUN pip install pip 

COPY requirements.txt requirements.txt

RUN  pip install --no-cache-dir --user --upgrade  -r requirements.txt

COPY . proj/

EXPOSE 8000
CMD ["./docker-utils/run.sh"]
ENTRYPOINT ["./docker-utils/entrypoint.sh"]