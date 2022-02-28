import tempfile
import logging

import sys
from os import path


def before_scenario(context, feature):
    context.tmp_xml_file = tempfile.TemporaryFile('wb+', suffix='.xml')
    
    # determine tools directory
    if path.exists('/workspaces/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/dossier/Source/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/mono/dossier/Source/dm/Tools'
    if 'tools.dir' in context.config.userdata:
        context.tools_dir = context.config.userdata['tools.dir']
    logging.debug(f'tools_dir: {context.tools_dir}')
    

def after_scenario(context, feature):
    context.tmp_xml_file = None
