from behave import when, then # pylint: disable=no-name-in-module

import tempfile
import shutil
import logging

from lxml import etree

import dmt.test
import dm.tasks.SequenceTask
import dm.klartext


@when(u'running the pipeline {pipeline_file}.dm')
def step_run(context, pipeline_file):
    try:
        with open(pipeline_file+'.dm', 'r', encoding='utf-8') as infile:            
            parser = dm.klartext.KlartextParser(infile)
            inp = parser.parse(convert_markdown=False)
            xml = etree.fromstring(inp)
            task = dm.tasks.SequenceTask(xml, 'pipeline', context.tools_dir)
            task.run()
    except Exception as e:
        print(e)
        context.exception = e

@then(u'the file {output_file}__o.test.md is equal to {original_file}__o.md')
def step_compare_md(context, output_file, original_file):
    with open(output_file+'__o.test.md', 'rb') as output:
        with open(original_file+'__o.md', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.xhtml is equal to {original_file}__o.xhtml')
def step_compare_xhtml(context, output_file, original_file):
    with open(output_file+'__o.test.xhtml', 'rb') as output:
        with open(original_file+'__o.xhtml', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.tex is equal to {original_file}__o.tex')
def step_compare_tex(context, output_file, original_file):
    with open(output_file+'__o.test.tex', 'rb') as output:
        with open(original_file+'__o.tex', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.docx is equal to {original_file}__o.docx')
def step_compare_docx(context, output_file, original_file):
    with open(output_file+'__o.test.docx', 'rb') as output:
        with open(original_file+'__o.docx', 'rb') as original:
            equal, diff = dmt.test.compare_docx(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.xml is equal to {original_file}__o.xml')
def step_compare_xml(context, output_file, original_file):
    with open(output_file+'__o.test.xml', 'rb') as output:
        with open(original_file+'__o.xml', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.kt is equal to {original_file}__o.kt')
def step_compare_md(context, output_file, original_file):
    with open(output_file+'__o.test.kt', 'rb') as output:
        with open(original_file+'__o.kt', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

@then(u'the file {output_file}__o.test.pdf is equal to {original_file}__o.pdf')
def step_compare_pdf(context, output_file, original_file):   
    equal, diff = dmt.test.compare_pdf(output_file+'__o.test.pdf', original_file+'__o.pdf')
    assert equal, diff

@then(u'no exception is thrown')
def step_no_exception(context):
    assert None == context.exception

@then(u'a {exception} is thrown')
def step_exception(context, exception):
    assert exception == type(context.exception).__name__

@then(u'it displays "{text}"')
def step_display(context, text):
    # TODO: Capture the output!
    # output = context.stdout_mock.getvalue()    
    # assert text == output
    pass