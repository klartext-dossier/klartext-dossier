from behave import when, then # pylint: disable=no-name-in-module

from lxml import etree
from klartext import Parser

import dmt.test
import dm.tasks.SequenceTask
from dm.markdown_parser import processMarkdownContent


@when(u'running the pipeline {pipeline_file}.dm')
def step_run(context, pipeline_file):
    try:
        with open(pipeline_file+'.dm', 'r', encoding='utf-8') as infile:            
            parser = Parser()
            inp = parser.parse(infile, convert_text=processMarkdownContent)
            xml = etree.fromstring(inp)
            task = dm.tasks.SequenceTask(xml, 'pipeline', context.toolsdir)
            task.run()
    except Exception as e:
        print(e)
        context.exception = e


@then(u'the file {output_file}__o.test.xml is equal to {original_file}__o.xml')
def step_compare_xml(context, output_file, original_file):
    with open(output_file+'__o.test.xml', 'rb') as output:
        with open(original_file+'__o.xml', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff


@then(u'the file {output_file}__o.test.txt is equal to {original_file}__o.txt')
def step_compare_xml(context, output_file, original_file):
    with open(output_file+'__o.test.txt', 'rb') as output:
        with open(original_file+'__o.txt', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff

