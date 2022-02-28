import os, logging, pkg_resources

from dm.exceptions import TaskException


def tryLocatingFile(filename, basedir=None):
    
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


def tryLocatingToolsFile(filename, tool_type, tools_dir):
    
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
    path = os.path.join(tools_dir, tool_type, filename)
    if os.path.exists(path):
        logging.debug(f'Located in "{path}"')                
        return path

    # try to find the file in the tools directory
    path = os.path.join(tools_dir, filename)
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
    raise TaskException(f'Cannot locate file "{filename}"')
