import tempfile
import logging

import sys
from os import path


def before_scenario(context, feature):
    context.tmp_html_file = tempfile.TemporaryFile('wb+', suffix='.html')
    context.tmp_tex_file = tempfile.TemporaryFile('w+', encoding='utf-8', suffix='.tex')
    context.tmp_docx_file = tempfile.TemporaryFile('wb+', suffix='.docx')
    context.tmp_pdf_file = tempfile.TemporaryFile('wb+', suffix='.pdf')
    
    # determine tools directory
    if path.exists('/workspaces/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/dossier/Source/dm/Tools'
    elif path.exists('/workspaces/mono/dossier/Source/dm/Tools'):
        context.tools_dir = '/workspaces/mono/dossier/Source/dm/Tools'
    if 'tools.dir' in context.config.userdata:
        context.tools_dir = context.config.userdata['tools.dir']
    logging.debug(f'tools_dir: {context.tools_dir}')
    

def after_scenario(context, feature):
    context.tmp_html_file = None
    context.tmp_tex_file = None
    context.tmp_docx_file = None
    context.tmp_pdf_file = None
