#!/bin/bash
set -e


case "$1" in
    web)
        python manage.py migrate --noinput
        python manage.py collectstatic --noinput
        exec gunicorn web_app.wsgi:application \
              -b 0.0.0.0:8000 \
              -w $WORKERS_COUNT
        ;;
    *)
        exec "$@"
esac
