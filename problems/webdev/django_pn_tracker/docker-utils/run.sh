#!/bin/bash

echo "Starting uWSGI"
PROJECT_NAME="regcounter"


uwsgi --chdir ${SITE_DIR}proj/ \
    --module=${PROJECT_NAME}.wsgi:application \
    --master \
    --env DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings \
    --vacuum \
    --max-requests=5000 \
    --processes 2 \
    --${CONNECT_METHOD:=http} 0.0.0.0:8000 \
    --static-map /static=${SITE_DIR}htdocs/static/ \
    --python-autoreload=1 \
    --honour-stdin
