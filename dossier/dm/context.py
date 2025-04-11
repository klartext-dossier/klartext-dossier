""" Module providing the contest of a pipeline execution.
"""

import os, copy, io
from importlib.resources import files


class Scope:

    """ Stores one state of the pipeline execution.
    """

    def __init__(self, indent: int = 0, namespaces: dict[str, str] = dict(), infile: str = "") -> None:

        """ Initializer.

            Args:
                indent:     the current line indent
                namespaces: a dictionary of the defined namespaces, mapping the prefix to an URL
                infile:     name of the current input file
        """

        self.basedir: str = ""
        self.toolsdir: str = ""
        self.filename: str = ""
        self.indent: int = indent
        self.namespaces: dict[str, str] = namespaces
        self.infile: str = infile


    def __str__(self):

        return f'Scope(basedir="{self.basedir}", file_name="{self.filename}", toolsdir="{self.toolsdir}, indent={self.indent}, namespaces={self.namespaces}", infile={self.infile})'


class Context:

    """ Stores the complete state of a pipeline execution.

        The context is a stack of Scopes. Whenever a file is included, a new state will be pushed on the stack and remove, when the included file has been processed.

        This class acts as a context manager.
    """

    def __init__(self, basedir: str = os.getcwd(), toolsdir: str = files('dm').joinpath('Tools'), indent: int = 0, namespaces: dict[str, str] = dict(), infile: str = "") -> None:

        """ Initializer.

            Args:
                basedir:    the base directory for including files
                toolsdir:   the directory where the helper files are located
                indent:     the initial indent
                namespaces: a dictionary of the defined namespaces, mapping the prefix to an URL
                infile:     the name of the input file
        """
        
        self._flags: list[str] = []
        self.scopes = [Scope(indent, namespaces, infile)]
        self.tempfiles: dict[str, str] = {}

        self.scope().basedir = os.path.abspath(basedir)
        self.scope().toolsdir = os.path.abspath(toolsdir)


    def scope(self) -> Scope:

        """ The current scope.

            Returns:
                The current Scope, i.e., the Scope at the top of the stack.
        """

        return self.scopes[-1]


    def __str__(self):

        s = io.StringIO()

        level = 0
        for scope in self.scopes:
            s.write(f'{scope}|')
            level += 1

        return s.getvalue()
    

    def toolsdir(self) -> str:

        """ The toolsdir.
        
            Returns:
                The directory where the helper files are stored.
        """
        
        return self.scope().toolsdir


    def basedir(self) -> str:

        """ The basedir.

            Returns:
                The base directory for including files.
        """
        
        return self.scope().basedir
        

    def set_basedir(self, dir: str) -> None:

        """ Sets the base directory.
        
            Args:
                dir: the base directory to set
        """
        
        self.scope().basedir = dir


    def set_filename(self, filename: str) -> None:

        """ Sets the current file name.
        
            Also sets the basedir to the directory of the current file.
        """
        
        if not os.path.isabs(filename):
            filename = os.path.abspath(os.path.join(self.basedir(), filename))
        self.scope().basedir = os.path.dirname(filename)
        self.scope().filename = os.path.basename(filename)


    def indent(self) -> int:

        """ The current indent.
        
            Returns:
                The current indent
        """

        return self.scope().indent
    

    def set_indent(self, indent: int) -> None:

        """ Sets the current indent.
        
            Args:
                indent: the current indent
        """

        self.scope().indent = indent


    def namespaces(self) -> dict[str, str]:

        """ The current namespace mapping.
        
            Returns:
                a dictionary of the defined namespaces, mapping the prefix to an URL#
        """
        
        return self.scope().namespaces


    def infile(self) -> str:

        """ The current input file.
        
            Returns:
                the current input file
        """

        return self.scope().infile


    def set_infile(self, infile: str) -> None:

        """ Set the current input file.
        
            Args:
                infile: the current input file
        """

        self.scope().infile = infile


    def flags(self) -> list[str]:

        """ The flags.

            Returns:
                a list of flags passed via command line, using --set flag,flag,...
        """

        return self._flags


    def set_flags(self, flags: list[str]) -> None:

        """ Set flags.
        
            Args:
                flags: a list of flags passed via command line, using --set flag,flag,...
        """

        self._flags = flags
        

    def add_tempfile(self, name: str, tempfile: str) -> None:

        """ Add a temporary file.
        
            Args:
                name:     name of the temporary file
                tempfile: the temporary file
        """

        self.tempfiles[name] = tempfile


    def __enter__(self):

        s = copy.copy(self.scopes[-1])
        self.scopes.append(s)


    def __exit__(self, type=None, value=None, traceback=None):

        self.scopes.pop()