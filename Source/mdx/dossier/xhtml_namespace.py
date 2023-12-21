"""
Adds the xhtml namespace declaration to the root element.

"""

from markdown import Extension
from markdown.treeprocessors import Treeprocessor


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
