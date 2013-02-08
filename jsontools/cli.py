"""JSON Tools

Usage:
    json [options] pluck JSON_PATH
    json [options] slice [KEY_NAME...]
    json [options] colorize
    json [options] render TEMPLATE

Handy dandy JSON toolkit to works on JSON documents, most often from curl,
but also handy when piped from local files.

Commands:
    pluck       Pluck out a sub-document with a . and [] notation path.
    slice       Keep only the specified key names in a document,
                discarding the rest. This will recurse the whole document.
    colorize    Pretty print a document, with colors, making it easier to read.
    render      Run the document through a mustache template

Parameters:
    JSON_PATH   Use .key and [index] to pick out a single subdocument,
                just pretend it is what you would type in JavaScript and
                you will likely get it right.
                ex: {'hello': {'a': 'world'}} with .hello.a
                    will give you 'world'
                    .hello will give you {'a': 'world}
    KEY_NAME    Just the string name of a key inside your document
    TEMPLATE    File path to a mustache template, the document context is
                supplied as a root variable called document


Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import clint
from docopt import docopt
from jsontools.version import __package_version__, __package_name__
from jsontools.openstruct import OpenStruct
import pystache
import json

def render(arguments, document):
    print(pystache.render(open(arguments.TEMPLATE).read(), {'document': document}).strip())

def pluck(arguments, document):
    target = OpenStruct(document)
    plucked = eval("target{0}".format(arguments.JSON_PATH))
    if isinstance(plucked, OpenStruct):
        print(json.dumps(repr(plucked)))
    else:
        print(json.dumps(plucked))

def main():
    arguments = docopt(__doc__, version="{0} {1}".format(__package_name__, __package_version__))
    document = json.loads(clint.piped_in())
    for key in arguments.keys():
        if key in globals() and arguments[key]:
            globals()[key](OpenStruct(arguments), document)


