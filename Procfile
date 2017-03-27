web: gunicorn --pythonpath verse verse.wsgi
worker: celery -A verse worker --workdir verse --loglevel info