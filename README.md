# verse
[![Build status](https://img.shields.io/travis/pawelad/verse.svg)][travis]
[![GitHub release](https://img.shields.io/github/release/pawelad/verse.svg)][github]
[![Test coverage](https://img.shields.io/coveralls/pawelad/verse.svg)][coveralls]
[![License](https://img.shields.io/github/license/pawelad/verse.svg)][license]

Verse is a RESTful API that checks the latest version of your favourite open
source project and simplifies the whole process to one HTTP request. Just like
that.

It comes with a bunch of supported projects - with much more on the way - and
also allows using any GitHub repository as a source, as long as it uses tags
and '[normal][pep440]' version names.

The project is still in its early days so all help is appreciated - suggestions
for new supported projects and features that you would find useful, bug
reports, help with design and frontend, etc.

## Usage
<a href="https://asciinema.org/a/110316" target="_blank"><img src="https://asciinema.org/a/110316.png" alt="Verse usage" width="600px"></a>

## Running locally
Verse is run in production with the help of `dokku`, `gunicorn` and
`whitenoise`, which means it's Heroku/Foreman/Honcho (and Procfile in general)
compatible:

```shell
$ pip3 install -r requirements.txt
$ export SECRET_KEY='...'
$ heroku local web
$ ...
$ foreman start
$ ...
$ honcho start
$ ...
```

It uses environment variables to manage configuration variables and you need
at least `SECRET_KEY` set to run it locally. Redis (for caching and Celery) is
also recommended but should't be required.

You can also run it as a regular Django project:

```shell
$ pip3 install -r requirements.txt
$ export SECRET_KEY='...'
$ python verse/manage.py migrate
$ python verse/manage.py runserver
```

## Configuration
Verse uses `python-decouple` and `dj-database-url` to manage configuration
variables. You can have a look at the settings file to see what values are
configurable, but for reference here are the ones that I use locally:

```shell
$ cat .env
SECRET_KEY='...'
DEBUG=True
DATABASE_URL='postgres://localhost/verse'
REDIS_CACHE_URL='redis://127.0.0.1:6379/0'
CELERY_BROKER_URL='redis://127.0.0.1:6379/1'
GITHUB_TOKEN='...'
```

## Tests
Package was tested with the help of `py.test` and `tox` on Python 3.4, 3.5
and 3.6 with Django 1.10 and Django REST Framework 3.6 (see `tox.ini`).

Code coverage is available at [Coveralls][coveralls].

To run tests yourself you need to set environment variable with Django secret
key before running `tox` inside the repository:

```shell
$ export SECRET_KEY='...'
$ pip install tox
$ tox
```

## Contributions
Package source code is available at [GitHub][github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest enhancements,
add functionality and point out any mistakes. Thanks!

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Released under [MIT License][license].


[coveralls]: https://coveralls.io/github/pawelad/verse
[github]: https://github.com/pawelad/verse
[license]: https://github.com/pawelad/verse/blob/master/LICENSE
[pawelad]: https://github.com/pawelad
[pep440]: https://www.python.org/dev/peps/pep-0440/
[travis]: https://travis-ci.org/pawelad/verse
