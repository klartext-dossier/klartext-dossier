import logging
import io
import sys
from os import path


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    
    # determine tools directory
    if path.exists('/workspaces/dossier/Source/dm/Tools'):
        context.toolsdir = '/workspaces/dossier/Source/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/Source/dm/Tools'):
        context.toolsdir = '/workspaces/mono/dossier/Source/dm/Tools'
    if 'tools.dir' in context.config.userdata:
        context.toolsdir = context.config.userdata['tools.dir']
    logging.debug(f'toolsdir: {context.toolsdir}')
    context.exception = None

    # capture stdout
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock
    

def after_scenario(context, feature):
    context.exception = None
    sys.stdout = context.real_stdout