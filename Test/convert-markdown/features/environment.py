import tempfile
import logging

from os import path

from dm.utilities import guessToolsDir

def before_scenario(context, feature):
    logging.disable(logging.INFO)
    context.tmp_html_file = tempfile.TemporaryFile('wb+', suffix='.html')
    context.tmp_tex_file = tempfile.TemporaryFile('w+', encoding='utf-8', suffix='.tex')
    context.tmp_docx_file = tempfile.TemporaryFile('wb+', suffix='.docx')
    context.tmp_pdf_file = tempfile.TemporaryFile('wb+', suffix='.pdf')
    
    context.toolsdir = guessToolsDir()

    if 'tools.dir' in context.config.userdata:
        context.toolsdir = context.config.userdata['tools.dir']
    logging.debug(f'toolsdir: {context.toolsdir}')
    

def after_scenario(context, feature):
    context.tmp_html_file = None
    context.tmp_tex_file = None
    context.tmp_docx_file = None
    context.tmp_pdf_file = None
