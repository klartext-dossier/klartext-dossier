from behave import when, then # pylint: disable=no-name-in-module

from lxml import etree

import dmt.test

import dm.pipeline


@when(u'running the pipeline {pipeline_file}.dm')
def step_run(context, pipeline_file):
    try:
        with open(pipeline_file+'.dm', 'r', encoding='utf-8') as infile:            
            pipe = dm.pipeline.Pipeline(infile)
            pipe.run(context=context.context, input=None, input_encoding='utf-8', output=None, output_encoding='utf-8')
    except Exception as e:
        print(e)
        context.exception = e


@then(u'the file {output_file}.test.xml is equal to {original_file}__o.xml')
def step_compare_xml(context, output_file, original_file):
    with open(output_file+'.test.xml', 'rb') as output:
        with open(original_file+'__o.xml', 'rb') as original:
            equal, diff = dmt.test.compare_bytes(output, original)
            assert equal, diff
