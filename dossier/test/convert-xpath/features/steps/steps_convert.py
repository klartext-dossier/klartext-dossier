from behave import when, then # pylint: disable=no-name-in-module

from lxml import etree

import dmt.test

from dm.pipeline import Pipeline


@when(u'running the pipeline {pipeline_file}.dm')
def step_run(context, pipeline_file):
    try:
        with open(pipeline_file+'.dm', 'r', encoding='utf-8') as infile:            
            pipe = dm.Pipeline.Pipeline(infile)
            pipe.run(context=context)
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

