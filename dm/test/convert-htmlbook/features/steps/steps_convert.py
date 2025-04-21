from behave import when, then # pylint: disable=no-name-in-module

import tempfile
import shutil

import dmt.test


@when(u'converting the {markdown_file} to html')
def step_convert_md_html(context, markdown_file):
    with open(markdown_file, 'rb') as infile:
        context.tmp_html_file = dmt.test.run_conversion_pipeline(infile, 'md', 'html', { 'template': None, 'pretty': False, 'toolsdir': context.toolsdir })


@when(u'converting the {html_file} to PDF')
def step_convert_html_pdf(context, html_file):
    with open(html_file, 'rb') as infile:
        context.tmp_pdf_file = dmt.test.run_conversion_pipeline(infile, 'html', 'pdf', { 'template': None, 'pretty': False, 'toolsdir': context.toolsdir })


@then(u'the html output is equal to {html_file}')
def step_compare_html(context, html_file):
    with open(html_file, 'rb') as html:
        equal, diff = dmt.test.compare_html(html, context.tmp_html_file)
        assert equal, diff


@then(u'the PDF output is equal to {pdf_file}')
def step_compare_pdf(context, pdf_file):
    with tempfile.NamedTemporaryFile('wb+', suffix='.pdf') as tmpfile:
        shutil.copyfileobj(context.tmp_pdf_file, tmpfile)
        tmpfile.flush()
        equal, diff = dmt.test.compare_pdf(pdf_file, tmpfile.name)
        assert equal, diff