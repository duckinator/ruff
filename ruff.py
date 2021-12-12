#!/usr/bin/env python3

from pathlib import Path
import shutil
from subprocess import check_call
import sys
from textwrap import dedent

__author__ = 'Ellen Marie Dash'
__version__ = '2.0.0'

# Latest source: https://github.com/duckinator/ruff/blob/master/ruff.py

# Released under the MIT license.
# Copyright (c) 2018, 2021 Ellen Marie Dash
# https://opensource.org/licenses/MIT

# Notable changes:
#   1.0.0 - initial release
#   2.0.0 - switched from `pep517.build` (which is deprecated) to `build`

def _try_rmtree(path):
    if Path(path).is_dir():
        shutil.rmtree(path)
    elif Path(path).exists():
        raise RuntimeError("'{}' is not a directory".format(path))


def _write_if_needed(filename, text):
    path = Path.cwd() / filename
    if path.exists():
        print('{} exists; skipping.'.format(filename))
    else:
        path.write_text(text)


def init(_script):
    _write_if_needed('pyproject.toml', dedent("""\
        [build-system]
        requires = ["setuptools", "wheel"]
        build-backend = "setuptools.build_meta"
        """))

    _write_if_needed('setup.cfg', dedent("""\
        [metadata]
        # Replace MODULE with the module name, AUTHOR with your name, and
        # EMAIL with your email address. Then delete this comment. :)
        name = MODULE
        version = 0.0.1
        author = AUTHOR
        author_email = EMAIL
        """))


def build(_script, *args):
    if not Path(Path.cwd(), 'pyproject.toml').exists():
        sys.exit("error: pyproject.toml doesn't exist.")

    if not args:
        args = ['.']

    if len(args) != 1:
        sys.exit(f"usage: {sys.argv[0]} build [SOURCE_DIRECTORY]\nSOURCE_DIRECTORY\tthe root directory of the project being built")

    source_directory = args[0]

    try:
        import build
    except ModuleNotFoundError:
        check_call([sys.executable, '-m', 'pip', 'install', '-qq', 'build'])
        import build

    builder = build.ProjectBuilder(source_directory)
    builder.build('sdist', './dist/')
    builder.build('wheel', './dist/')


def clean(_script):
    _try_rmtree("./build")
    _try_rmtree("./dist")
    for name in Path.cwd().glob('*.egg-info'):
        if name.is_dir():
            _try_rmtree(name)


def help(script):
    print("Usage: {} [init | build | clean]".format(script))
    print()
    print("init     Create basic pyproject.toml and setup.cfg files.")
    print("build    Build the project.")
    print("clean    Clean up build artifacts.")
    print("version  Print version information.")


def main(argv):
    if len(argv) == 1:
        argv = [argv[0], 'help']
    script, command, *args = argv

    function = {
        'init': init,
        'build': build,
        'clean': clean,
        'version': lambda s: print(s, __version__, 'by', __author__)
    }.get(command, help)

    function(script, *args)


if __name__ == '__main__':
    main(sys.argv)
