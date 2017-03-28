"""
verse.checkers.projects

Home of implemented projects checkers, loosely grouped into files
"""
from checkers.base import BaseVersionChecker

from checkers.projects.databases import (  # noqa
    MySQLVersionChecker, MySQLClusterVersionChecker, PostgreSQLVersionChecker,
)
from checkers.projects.frontend_frameworks import (  # noqa
    BootstrapVersionChecker, FontAwesomeVersionChecker, MDLVersionChecker,
)
from checkers.projects.git import (  # noqa
    GitVersionChecker, GitLabVersionChecker, GogsVersionChecker,
)
from checkers.projects.go import (  # noqa
    GoVersionChecker, DockerVersionChecker, KubernetesVersionChecker,
)
from checkers.projects.python import (  # noqa
    PythonVersionChecker, AnsibleVersionChecker, CeleryVersionChecker,
    DjangoVersionChecker, DjangoRESTFrameworkVersionChecker,
    FlaskVersionChecker, GunicornVersionChecker, RequestsVersionChecker,
    ScrapyVersionChecker,
)
from checkers.projects.webservers import (  # noqa
    ApacheVersionChecker, NginxVersionChecker,
)


AVAILABLE_CHECKERS = {
    checker.name: checker for checker in BaseVersionChecker.__subclasses__()
}
