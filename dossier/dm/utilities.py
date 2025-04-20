""" Module providing useful functions used in several places.
"""

import os, logging, pkg_resources, sys

from dm.exceptions import TaskException


def guessToolsDir() -> str:

    """ Tries to locate the directory of the tools files.

        Returns:
            The path to the tools directory.
    """

    # we are running inside the IDE
    if os.path.exists('/workspaces/dossier/dossier/dm/Tools'):
        return '/workspaces/dossier/dossier/dm/Tools'
    
    # we are running in Azure
    if '/usr/local/bin/behave' == os.path.abspath(sys.argv[0]):
        return '/__w/1/s/Source/dm/Tools'

    # we are running the executable
    return os.path.join(os.path.dirname(sys.argv[0]), 'Tools')


def tryLocatingFile(filename: str, basedir: str|None=None) -> str:
    
    """ Tries to locate a file.

        The functions will try to locate a file by:

        1. Checking if the file with an absolute path exists
        2. Checking if the file relative to the basedir exists
        3. Checking if the file exists in the current directory

        Args:
            filename: The name of the file to locate
            basedir:  The base directory to lookup files. Optional.

        Returns:
            The absolute filename, if the file has been found.

        Raises:
            TaskException: if the file has not been found. 
    """

    logging.debug(f'Trying to locate "{filename}" with basedir="{basedir}"')
    
    # if the file is absolute, try it
    logging.debug(f'Trying "{filename}')
    if os.path.isabs(filename):
        if os.path.exists(filename):
            logging.debug(f'Located in "{filename}"')                
            return filename 
        raise TaskException(f'File "{filename}" does not exist')

    # try to find the file relative to the basedir
    if basedir:
        path = os.path.join(basedir, filename)
        logging.debug(f'Trying "{path}')
        if os.path.exists(path):
            logging.debug(f'Located in "{path}"')                
            return path

    # try to find the file in the current directory
    path = os.path.join(os.getcwd(), filename)
    logging.debug(f'Trying "{path}')
    if os.path.exists(path):
        logging.debug(f'Located in "{path}"')                
        return path

    logging.error(f'Cannot locate file "{filename}"')
    raise TaskException(f'Cannot locate file "{filename}"')


def tryLocatingToolsFile(filename: str, tool_type: str, toolsdir: str) -> str:
    
    """ Tries to locate a tools file.

        The functions will try to locate a tools file by:

        1. Checking if the tools file with an absolute path exists
        2. Checking if the tools file exists in the current directory
        3. Checking if the tools file exists in the tools directory
        4. Checking if the tools file is part of the python package
        5. 

        Args:
            filename:  The name of the file to locate
            tool_type: The type of the tool, e.g., `css` for css files
            toolsdir:  The tools directory

        Returns:
            The absolute filename, if the file has been found.

        Raises:
            TaskException: if the file has not been found. 
    """

    logging.debug(f'Trying to locate {tool_type} tools file "{filename}"')
    
    # if the file is absolute, try it
    if os.path.isabs(filename):
        if os.path.exists(filename):
            logging.debug(f'Located in "{filename}"')                
            return filename 
        raise TaskException(f'File "{filename}" does not exist')

    # try to find the file in the current directory
    path = os.path.join(os.getcwd(), filename)
    if os.path.exists(path):
        logging.debug(f'Located in "{path}"')                
        return path

    # try to find the file in the tools directory, in the tools_type subdir
    path = os.path.join(toolsdir, tool_type, filename)
    if os.path.exists(path):
        logging.debug(f'Located in "{path}"')                
        return path

    # try to find the file in the tools directory
    path = os.path.join(toolsdir, filename)
    if os.path.exists(path):
        logging.debug(f'Located in "{path}"')                
        return path

    # try to find the file in the package, in the tools_type subdir
    if pkg_resources.resource_exists(__name__, tool_type + '/' + filename):
        path = pkg_resources.resource_filename(__name__, tool_type + '/' + filename)
        logging.debug(f'Located in "{path}"')                
        return path

    # try to find the file in the package
    if pkg_resources.resource_exists(__name__, filename):
        path = pkg_resources.resource_filename(__name__, filename)
        logging.debug(f'Located in "{path}"')                
        return path

    logging.error(f'Cannot locate file "{filename}"')
    raise TaskException(f'Cannot locate file "{filename}", toolsdir="{toolsdir}"')
