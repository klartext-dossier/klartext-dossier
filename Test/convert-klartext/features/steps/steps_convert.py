from behave import when, then # pylint: disable=no-name-in-module

import dmt.test


@when(u'converting the {kt_file} to XML')
def step_convert_kt_xml(context, kt_file):
    with open(kt_file, 'rb') as infile:
        context.tmp_xml_file = dmt.test.run_conversion_pipeline(infile, 'kt', 'xml', { 'template': None, 'pretty': False, 'tools_dir': context.tools_dir })


@then(u'the XML output is equal to {xml_file}')
def step_compare_xml(context, xml_file):
    with open(xml_file, 'rb') as xml:
        equal, diff = dmt.test.compare_xml(xml, context.tmp_xml_file)
        assert equal, diff
