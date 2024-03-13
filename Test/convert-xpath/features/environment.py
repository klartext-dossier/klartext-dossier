import logging, io, sys

from os import path

from dm.utilities import guessToolsDir


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    
    context.toolsdir = guessToolsDir()

    if 'tools.dir' in context.config.userdata:
        context.toolsdir = context.config.userdata['tools.dir']
    logging.debug(f'toolsdir: {context.toolsdir}')

    # capture stdout
    context.real_stdout = sys.stdout
    context.stdout_mock = io.StringIO()
    sys.stdout = context.stdout_mock
    

def after_scenario(context, feature):
    context.exception = None
    sys.stdout = context.real_stdout