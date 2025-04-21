import tempfile
import logging

from os import path

from dm.utilities import guessToolsDir


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    context.tmp_xml_file = tempfile.TemporaryFile('wb+', suffix='.xml')
    
    context.toolsdir = guessToolsDir()

    if 'toolsdir' in context.config.userdata:
        context.toolsdir = context.config.userdata['toolsdir']
    logging.debug(f'toolsdir: {context.toolsdir}')
    

def after_scenario(context, feature):
    context.tmp_xml_file = None
