''' Module providing the xhtml extension for Markdown.
'''

import xml.etree.ElementTree as etree
from markdown import Extension, Markdown
from markdown.treeprocessors import Treeprocessor


class XHTMLProcessor(Treeprocessor):
    
    def run(self, root: etree.Element) -> etree.Element | None:

        for child in root:
            child.attrib['xmlns'] = 'http://www.w3.org/1999/xhtml'
            
        return root


class XHTMLExtension(Extension):

    """ Extension for xhtml.

        Adds the xhtml namespace ('http://www.w3.org/1999/xhtml') to the top level elements.
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.treeprocessors.register(XHTMLProcessor(md), 'XHTML', 10000)


def makeExtension(**kwargs):

    return XHTMLExtension(**kwargs)
