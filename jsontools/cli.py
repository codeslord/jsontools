"""JSON Tools

Usage:
    json [options] pluck JSON_PATH
    json [options] slice [KEY_NAME...]
    json [options] colorize [SPACES]
    json [options] indent [SPACES]
    json [options] render TEMPLATE

A command line toolkit for slicing and dicing JSON documents.

Commands:
    pluck       Pluck out a sub-document with a . and [] notation path
    slice       Keep only the specified key names in a document,
                discarding the rest. This will recurse the whole document
    colorize    Pretty print a document, with colors, making it easier to read
    indent      Just indent a JSON stream to be human readable
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
    SPACES      Integer number of spaces to indent


Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
from jsontools.version import __package_version__, __package_name__
from jsontools.openstruct import OpenStruct
from jsontools.colors import color_wrap
import pystache
import json
import sys
import re
import select
import os

JSON_NAME_MATCHER = re.compile(r'"([^"]*)":')


def input_content():
    if select.select([sys.stdin,],[],[],0.0)[0]:
        return json.loads(sys.stdin.read())
    else:
        return {}

def render(arguments, document):
    print(pystache.render(open(arguments.TEMPLATE).read(),
        {
            'document': document,
            'environment': {k:v for k, v in os.environ.iteritems()}
        }).strip())

def pluck(arguments, document):
    target = OpenStruct(document)
    plucked = eval("target{0}".format(arguments.JSON_PATH))
    if isinstance(plucked, OpenStruct):
        print(json.dumps(plucked.__wrap__))
    elif isinstance(plucked, unicode):
        print(plucked.encode('utf-8'))
    elif isinstance(plucked, str):
        print(plucked)
    else:
        print(json.dumps(plucked))

def colorize(arguments, document):
    if document == {}:
        return ''
    as_json = json.dumps(document, indent=(int(arguments.SPACES) if arguments.SPACES else 1))
    print(JSON_NAME_MATCHER.sub('"{0}":'.format(color_wrap(r'\1', 'bright green')), as_json))

def indent(arguments, document):
    if document == {}:
        return ''
    as_json = json.dumps(document, indent=(int(arguments.SPACES) if arguments.SPACES else 1))
    print as_json

def slice(arguments, document):
    keep = set(arguments.KEY_NAME)
    def _(root):
        if isinstance(root, dict):
            return {k:v for k, v in root.iteritems() if k in keep}
        elif isinstance(root, list):
            return [_(v) for v in root]
        else:
            return root
    print json.dumps(_(document))

def main():
    arguments = docopt(__doc__, version="{0} {1}".format(__package_name__, __package_version__))
    document = input_content()
    for key in arguments.keys():
        if key in globals() and arguments[key]:
            globals()[key](OpenStruct(arguments), document)


