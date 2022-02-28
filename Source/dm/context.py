import sys
import os
import logging
import copy


class scope:

    def __init__(self):
        self.basedir = None
        self.toolsdir = None
        self.filename = None
        self.indent = 0
        self.namespaces = dict()
        self.infile = None

    def log(self, level):
        logging.debug(f'scope[{level}] (base_dir="{self.basedir}", file_name="{self.filename}", tools_dir="{self.toolsdir}, indent={self.indent}, namespaces={self.namespaces}", infile={self.infile})')


class Context:

    def __init__(self, base_dir=None, tools_dir=None, indent=0, namespaces=dict(), infile=None):
        self._flags = []
        self.scopes = [scope()]
        self.tempfiles = {}

        self.scope().indent = indent
        self.scope().namespaces = namespaces
        self.scope().infile = infile

        if base_dir:
            self.scope().basedir = os.path.abspath(base_dir)
        else:
            self.scope().basedir = os.path.abspath(os.getcwd())
        if tools_dir:
            self.scope().toolsdir = os.path.abspath(tools_dir)
        else:
            self.scope().toolsdir = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'Tools'))

    def scope(self):
        return self.scopes[-1]

    def log(self):
        level = 0
        for scope in self.scopes:
            scope.log(level)
            level += 1

    def tools_dir(self):
        return self.scope().toolsdir

    def base_dir(self):
        return self.scope().basedir
        
    def set_base_dir(self, dir):
        self.scope().basedir = dir

    def set_filename(self, filename):
        if not os.path.isabs(filename):
            filename = os.path.abspath(os.path.join(self.base_dir(), filename))
        self.scope().basedir = os.path.dirname(filename)
        self.scope().filename = os.path.basename(filename)

    def indent(self):
        return self.scope().indent
    
    def set_indent(self, indent):
        self.scope().indent = indent

    def namespaces(self):
        return self.scope().namespaces

    def infile(self):
        return self.scope().infile

    def set_infile(self, infile):
        self.scope().infile = infile

    def flags(self):
        return self._flags

    def set_flags(self, flags):
        self._flags = flags
        
    def add_tempfile(self, name, tempfile):
        self.tempfiles[name] = tempfile

    def get_tempfile(self, name):
        return self.tempfiles[name]
        
    def enter(self):
        s = copy.copy(self.scopes[-1])
        self.scopes.append(s)

    def exit(self):
        self.scopes.pop()

    def __enter__(self):
        self.enter()

    def __exit__(self, type, value, traceback):
        self.exit()