"""
verse.checkers.projects

Home of implemented projects checkers, loosely grouped into files
"""
from checkers.base import BaseVersionChecker

from checkers.projects.databases import (  # noqa
    MySQLVersionChecker, MySQLClusterVersionChecker, PostgreSQLVersionChecker,
    SQLiteVersionChecker,
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
from checkers.projects.javascript import (  # noqa
    AngularVersionChecker, BackboneVersionChecker, D3JSVersionChecker,
    EmberJSVersionChecker, jQueryVersionChecker, NodeJSVersionChecker,
    ReactVersionChecker, VueJSVersionChecker,
)
from checkers.projects.misc import (  # noqa
    LinuxKernelVersionChecker, RabbitMQVersionChecker,
    SupervisorVersionChecker, VagrantVersionChecker,
)
from checkers.projects.nosql import (  # noqa
    CassandraVersionChecker, ElasticsearchVersionChecker,
    MongoDBVersionChecker, RedisVersionChecker,
)
from checkers.projects.python import (  # noqa
    PythonVersionChecker, AnsibleVersionChecker, CeleryVersionChecker,
    DjangoVersionChecker, DjangoRESTFrameworkVersionChecker,
    FlaskVersionChecker, GunicornVersionChecker, RequestsVersionChecker,
    ScrapyVersionChecker,
)
from checkers.projects.ruby import (  # noqa
    RubyVersionChecker, RailsVersionChecker, JekyllVersionChecker,
)
from checkers.projects.webservers import (  # noqa
    ApacheVersionChecker, NginxVersionChecker,
)


AVAILABLE_CHECKERS = {
    checker.name: checker for checker in BaseVersionChecker.__subclasses__()
}
