touch ./web/creek/logs/gunicorn.log
touch ./web/creek/logs/access.log
tail -n 0 -f /creek/logs/*.log &

function start_development(){
    echo Starting Flask at port 5000...
    FLASK_APP=./web/creek/app.py flask run --host=0.0.0.0 --port=5000
}

function start_production(){
    echo Starting Gunicorn...
    exec gunicorn --pythonpath ./web/creek/ app:app \
    --bind 127.0.0.1:8000 \
    --workers 3 \
    --log-level=info    \
    --log-file=./web/creek/logs/gunicorn.log   \
    --access-logfile=./web/creek/logs/access.log &
}

if [ ${PRODUCTION} == "false" ]; then
    # use development server
    start_development
else
    # use production server
    start_production
fi

exec service nginx start
