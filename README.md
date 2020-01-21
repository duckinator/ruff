# ruff [![Build Status][build-status-link]][build-status-img]

A single-file frontend for building [PEP 517](https://www.python.org/dev/peps/pep-0517/) compliant projects.


Ruff is a paper-thin wrapper around the pep517 library. If you want
something more full-featured, check out [Bork](https://github.com/duckinator/bork).

Ruff requires Python 3.5 or newer.

[build-status-link]: https://api.cirrus-ci.com/github/duckinator/ruff.svg
[build-status-img]: https://cirrus-ci.com/github/duckinator/ruff

## Installation

Copy `ruff.py` to the project you want to use it for, or plop it in a
directory in your `$PATH`.

## Usage

Assuming a project is PEP 517 compliant, you can just do:

```
$ ./ruff.py init  # Creates pyproject.toml and setup.cfg, if they don't exist.
$ vim setup.cfg   # And follow the instructions in the file.
$ ./ruff.py clean # Remove anything in build/, dist/, *.egg-info/
$ ./ruff.py build # Build the project
```
