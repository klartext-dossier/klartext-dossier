import sys, os, logging, copy, io


class Scope:

    def __init__(self, indent : int =0, namespaces : dict = dict(), infile : str = ""):

        self.basedir : str = ""
        self.toolsdir : str = ""
        self.filename : str = ""
        self.indent = indent
        self.namespaces = namespaces
        self.infile : str = infile


    def __str__(self):

        return f'Scope(basedir="{self.basedir}", file_name="{self.filename}", toolsdir="{self.toolsdir}, indent={self.indent}, namespaces={self.namespaces}", infile={self.infile})'


class Context:

    def __init__(self, basedir : str = os.getcwd(), toolsdir : str = os.path.join(os.path.dirname(sys.argv[0]), 'Tools'), indent : int = 0, namespaces : dict = dict(), infile : str = ""):

        self._flags = []
        self.scopes = [Scope(indent, namespaces, infile)]
        self.tempfiles = {}

        self.scope().basedir = os.path.abspath(basedir)
        self.scope().toolsdir = os.path.abspath(toolsdir)


    def scope(self):

        return self.scopes[-1]


    def __str__(self):

        s = io.StringIO()

        level = 0
        for scope in self.scopes:
            s.write(f'{scope}|')
            level += 1

        return s.getvalue()
    

    def toolsdir(self):

        return self.scope().toolsdir


    def basedir(self):

        return self.scope().basedir
        

    def set_basedir(self, dir):

        self.scope().basedir = dir


    def set_filename(self, filename):

        if not os.path.isabs(filename):
            filename = os.path.abspath(os.path.join(self.basedir(), filename))
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


    def __enter__(self):

        s = copy.copy(self.scopes[-1])
        self.scopes.append(s)


    def __exit__(self, type=None, value=None, traceback=None):

        self.scopes.pop()