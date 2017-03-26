"""
verse.checkers.projects

Home of implemented projects checkers, loosely grouped into files
"""
from checkers.base import BaseVersionChecker
from checkers.projects.python import (
    PythonVersionChecker, CeleryVersionChecker, DjangoVersionChecker,
    DjangoRESTFrameworkVersionChecker, FlaskVersionChecker,
)


AVAILABLE_CHECKERS = {
    checker.name: checker for checker in BaseVersionChecker.__subclasses__()
}
