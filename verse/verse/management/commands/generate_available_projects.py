"""
Helper command for generating a markdown list of available projects
"""
from collections import OrderedDict
from itertools import groupby

from django.core.management.base import BaseCommand

from checkers.projects import AVAILABLE_CHECKERS


def get_checker_group(checker):
    """
    Helper function for getting checker group from its module name

    :param checker: checker instance
    :type checker: checkers.base.BaseChecker
    :returns: checker group
    :rtype: str
    """
    return checker.__module__.split('.')[-1]


class Command(BaseCommand):
    """
    Custom Django management command for generating a markdown list of
    available projects
    """
    help = 'Generate a markdown list of available projects'

    def handle(self, *args, **options):
        available_projects = list(AVAILABLE_CHECKERS.values())
        sorted_projects = sorted(available_projects, key=get_checker_group)

        grouped_projects = OrderedDict()
        for key, group in groupby(sorted_projects, key=get_checker_group):
            grouped_projects[key] = sorted(
                list(group), key=lambda p: p.name,
            )

        projects_markdown = ''
        for group, projects in grouped_projects.items():
            group_markdown = '\n### {group_name}\n\n'.format(group_name=group)
            projects_markdown += group_markdown

            for project in projects:
                project_markdown = (
                    '#### {0.name}  \n'
                    '**Name:** {0.name}  \n'
                    '**Slug:** {0.slug}  \n'
                    '**Homepage:** {0.homepage}  \n'
                ).format(project)

                if project.repository:
                    project_markdown += (
                        '**Repository:** {0.repository}  \n'.format(project)
                    )

                projects_markdown += project_markdown

        self.stdout.write(projects_markdown)
