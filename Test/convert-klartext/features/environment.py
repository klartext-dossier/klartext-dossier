import tempfile
import logging

from os import path


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    context.tmp_xml_file = tempfile.TemporaryFile('wb+', suffix='.xml')
    
    # determine tools directory
    if path.exists('/workspaces/dossier/Source/dm/Tools'):
        context.toolsdir = '/workspaces/dossier/Source/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/Source/dm/Tools'):
        context.toolsdir = '/workspaces/mono/dossier/Source/dm/Tools'
    if 'tools.dir' in context.config.userdata:
        context.toolsdir = context.config.userdata['tools.dir']
    logging.debug(f'toolsdir: {context.toolsdir}')
    

def after_scenario(context, feature):
    context.tmp_xml_file = None
