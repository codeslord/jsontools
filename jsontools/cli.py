"""JSON Tools

Usage:
    json [options] pluck <json_path>
    json [options] slice [<key_name>...]
    json [options] colorize

Handy dandy JSON toolkit to works on streams of JSON, most often from curl,
but also handy when piped from local files.

Commands:
    pluck       Pluck out a sub-document with a . and [] notation path.
    slice       Keep only the specified key names in a document,
                discarding the rest. This will recurse the whole document.
    colorize    Pretty print a document, with colors, making it easier to read.

Parameters:
    json_path   Use .key and [index] to pick out a single subdocument,
                just pretend it is what you would type in JavaScript and
                you will likely get it right.
                ex: {'hello': {'a': 'world'}} with .hello.a
                    will give you 'world'
                    .hello will give you {'a': 'world}
    key_name    Just the string name of a key inside your document


Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import clint
from docopt import docopt
from jsontools.version import __package_version__, __package_name__
from jsontools.openstruct import OpenStruct

def slice(arguments):
    for stream in [clint.piped_in] + map(open, arguments.file):
        print stream

if __name__ == '__main__':
    arguments = docopt(__doc__, version="{0} {1}".format(__package_name__, __package_version__))
    print arguments


