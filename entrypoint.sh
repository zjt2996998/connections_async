#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "mysql started"
fi

# hypercorn --bind 0.0.0.0:5000 manage:app
exec "$@"