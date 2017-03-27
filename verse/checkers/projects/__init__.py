"""
verse.checkers.projects

Home of implemented projects checkers, loosely grouped into files
"""
from checkers.base import BaseVersionChecker
from checkers.projects.go import (  # noqa
    GoVersionChecker, DockerVersionChecker, KubernetesVersionChecker,
)
from checkers.projects.python import (  # noqa
    PythonVersionChecker, CeleryVersionChecker, DjangoVersionChecker,
    DjangoRESTFrameworkVersionChecker, FlaskVersionChecker,
    GunicornVersionChecker, RequestsVersionChecker, ScrapyVersionChecker,
)
from checkers.projects.webservers import (
    NginxVersionChecker,
)


AVAILABLE_CHECKERS = {
    checker.name: checker for checker in BaseVersionChecker.__subclasses__()
}
