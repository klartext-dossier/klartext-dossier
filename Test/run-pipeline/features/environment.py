import logging
import io
import sys
from os import path


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    
    # determine tools directory
    if path.exists('/workspaces/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/dossier/Source/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/mono/dossier/Source/dm/Tools'
    if 'tools.dir' in context.config.userdata:
        context.tools_dir = context.config.userdata['tools.dir']
    logging.debug(f'tools_dir: {context.tools_dir}')
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