import difflib
from behave import when, then # pylint: disable=no-name-in-module

from klartext import Parser


def compare_xml(a, b):
    list_a = [ line.rstrip() for line in a.readlines() ]
    list_b = b.decode('utf-8').splitlines() 
    
    diff = list(difflib.unified_diff(list_a, list_b))    
    return (len(diff) == 0, diff)


@when(u'converting the {kt_file} to XML')
def step_convert_kt_xml(context, kt_file):
    with open(kt_file, mode='r', encoding='utf-8') as infile:
        parser = Parser()        
        context.xml = parser.parse(infile)


@then(u'the XML output is equal to {xml_file}')
def step_compare_xml(context, xml_file):
    with open(xml_file, mode='r', encoding='utf-8') as xml:
        equal, diff = compare_xml(xml, context.xml)
        assert equal, diff
