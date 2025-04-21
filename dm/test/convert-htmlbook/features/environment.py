import tempfile, logging

from os import path

from dm.utilities import guessToolsDir


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    context.tmp_tex_file = tempfile.TemporaryFile('w+', encoding='UTF-8', suffix='tex')
    context.tmp_docx_file = tempfile.TemporaryFile('w+b', suffix='docx')
    context.tmp_pdf_file = tempfile.TemporaryFile('w+b', suffix='pdf')
    
    context.toolsdir = guessToolsDir()

    if 'toolsdir' in context.config.userdata:
        context.toolsdir = context.config.userdata['toolsdir']
    logging.debug(f'toolsdir: {context.toolsdir}')


def after_scenario(context, feature):
    context.tmp_tex_file = None
    context.tmp_docx_file = None
    context.tmp_pdf_file = None