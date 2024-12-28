import os, copy, io
from importlib.resources import files


class Scope:

    def __init__(self, indent: int = 0, namespaces: dict[str, str] = dict(), infile: str = "") -> None:

        self.basedir: str = ""
        self.toolsdir: str = ""
        self.filename: str = ""
        self.indent: int = indent
        self.namespaces: dict[str, str] = namespaces
        self.infile: str = infile


    def __str__(self):

        return f'Scope(basedir="{self.basedir}", file_name="{self.filename}", toolsdir="{self.toolsdir}, indent={self.indent}, namespaces={self.namespaces}", infile={self.infile})'


class Context:

    def __init__(self, basedir: str = os.getcwd(), toolsdir = files('dm').joinpath('Tools'), indent: int = 0, namespaces: dict[str, str] = dict(), infile: str = "") -> None:

        self._flags: list[str] = []
        self.scopes = [Scope(indent, namespaces, infile)]
        self.tempfiles: dict[str, str] = {}

        self.scope().basedir = os.path.abspath(basedir)
        self.scope().toolsdir = os.path.abspath(toolsdir)


    def scope(self) -> Scope:

        return self.scopes[-1]


    def __str__(self):

        s = io.StringIO()

        level = 0
        for scope in self.scopes:
            s.write(f'{scope}|')
            level += 1

        return s.getvalue()
    

    def toolsdir(self) -> str:

        return self.scope().toolsdir


    def basedir(self) -> str:

        return self.scope().basedir
        

    def set_basedir(self, dir: str) -> None:

        self.scope().basedir = dir


    def set_filename(self, filename: str) -> None:

        if not os.path.isabs(filename):
            filename = os.path.abspath(os.path.join(self.basedir(), filename))
        self.scope().basedir = os.path.dirname(filename)
        self.scope().filename = os.path.basename(filename)


    def indent(self) -> int:

        return self.scope().indent
    

    def set_indent(self, indent: int) -> None:

        self.scope().indent = indent


    def namespaces(self) -> dict[str, str]:

        return self.scope().namespaces


    def infile(self) -> str:

        return self.scope().infile


    def set_infile(self, infile: str) -> None:

        self.scope().infile = infile


    def flags(self) -> list[str]:

        return self._flags


    def set_flags(self, flags: list[str]) -> None:

        self._flags = flags
        

    def add_tempfile(self, name: str, tempfile: str) -> None:

        self.tempfiles[name] = tempfile


    def get_tempfile(self, name: str) -> str:

        return self.tempfiles[name]


    def __enter__(self):

        s = copy.copy(self.scopes[-1])
        self.scopes.append(s)


    def __exit__(self, type=None, value=None, traceback=None):

        self.scopes.pop()