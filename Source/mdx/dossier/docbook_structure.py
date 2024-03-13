"""
Wrap document content before sections into preface.

"""

import xml.etree.ElementTree as etree

from markdown import Extension
from markdown.treeprocessors import Treeprocessor


class DocBookStructureTreeprocessor(Treeprocessor):
    
    def run(self, doc):
        wrapper = []
        for child in doc.findall('*'):
            if child.tag in ['nav', 'section', 'div']:
                break
            else:
                wrapper.append(child)

        if len(wrapper) > 0:
            preface = etree.Element('section')
            preface.attrib["data-type"] = 'preface'
            for child in wrapper:
                preface.append(child)
                doc.remove(child)
            if preface.find('h1') is None:
                h1 = etree.Element('h1')
                h1.text = ' '
                preface.insert(0, h1)
            doc.insert(0, preface)


class NamespaceExtension(Extension):

    def extendMarkdown(self, md):
        md.treeprocessors.register(DocBookStructureTreeprocessor(md), 'DocBookStructure', 900)


def makeExtension(**kwargs):
    return NamespaceExtension(**kwargs)
