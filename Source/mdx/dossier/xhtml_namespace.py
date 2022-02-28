"""
Adds the xhtml namespace declaration to the root element.

"""

import re

from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree


class NamespaceTreeprocessor(Treeprocessor):
    
    def run(self, doc):
        for child in doc:
            child.attrib['xmlns'] = 'http://www.w3.org/1999/xhtml'



class NamespaceExtension(Extension):

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.treeprocessors.register(NamespaceTreeprocessor(md), 'Namespace', 10000)


def makeExtension(**kwargs):
    return NamespaceExtension(**kwargs)
