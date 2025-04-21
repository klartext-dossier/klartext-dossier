import logging
import io
import sys
from os import path


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    
    # determine tools directory
    if path.exists('/workspaces/dossier/dm/dm/Tools'):
        context.toolsdir = '/workspaces/dossier/dm/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/dm/dm/Tools'):
        context.toolsdir = '/workspaces/mono/dossier/dm/dm/Tools'
    if 'toolsdir' in context.config.userdata:
        context.toolsdir = context.config.userdata['toolsdir']
    logging.debug(f'toolsdir: {context.toolsdir}')
    context.exception = None

    # capture stdout
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock

    # capture error code
    context.error_code = -2
    

def after_scenario(context, feature):
    context.exception = None
    sys.stdout = context.real_stdout