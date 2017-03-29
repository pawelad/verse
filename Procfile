web: gunicorn --pythonpath verse verse.wsgi
worker: celery -A verse worker -B --workdir verse --loglevel info