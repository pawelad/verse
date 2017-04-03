<p align="center">
    <img src="https://cdn.rawgit.com/pawelad/verse/81bf68e6/verse/verse/static/img/logo.png" alt="Verse logo">
</p>

[![Build status](https://img.shields.io/travis/pawelad/verse.svg)][travis]
[![GitHub release](https://img.shields.io/github/release/pawelad/verse.svg)][github]
[![Test coverage](https://img.shields.io/coveralls/pawelad/verse.svg)][coveralls]
[![License](https://img.shields.io/github/license/pawelad/verse.svg)][license]

Verse is a RESTful API that checks the latest version of your favourite open
source project and simplifies the whole process to one HTTP request. Just like
that.

It comes with a bunch of [available projects][verse available projects] - with
much more on the way - and also allows using any GitHub repository as a source
of released versions, as long as it uses tags and [standardized][pep440]
version names. And if it doesn't - feel free to [suggest][github add issue]
adding it and I'll be happy to help.

Last seen at [verse.pawelad.xyz][verse], with [docs][verse docs] and a
[browsable API][verse browsable api].

The project is still in its early days so all help is appreciated - suggestions
for new features and projects to add, bug reports, help with design, etc.
Oh, and don't worry - a _cool_ domain is also on the list of things to do.

## Usage
<a href="https://asciinema.org/a/110529" target="_blank"><img src="https://asciinema.org/a/110529.png" alt="Verse usage" width="600px"></a>

## Contributions
Package source code is available at [GitHub][github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest enhancements,
add functionality and point out any mistakes. Thanks!

Also, take a look [here][verse running locally] if you want to run Verse
locally.

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

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Released under [Apache License 2.0][license].


[coveralls]: https://coveralls.io/github/pawelad/verse
[github]: https://github.com/pawelad/verse
[github add issue]: https://github.com/pawelad/verse/issues/new
[license]: https://github.com/pawelad/verse/blob/master/LICENSE
[pawelad]: https://github.com/pawelad
[pep440]: https://www.python.org/dev/peps/pep-0440/
[travis]: https://travis-ci.org/pawelad/verse
[verse]: https://verse.pawelad.xyz/
[verse browsable api]: https://verse.pawelad.xyz/projects/
[verse docs]: https://verse.pawelad.xyz/docs/
[verse running locally]: https://github.com/pawelad/verse/wiki/Running-Verse-locally
[verse available projects]: https://github.com/pawelad/verse/wiki/Available-projects
