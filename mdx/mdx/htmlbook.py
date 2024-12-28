''' Module providing the htmlbook extension for Markdown.
'''

import xml.etree.ElementTree as etree
from markdown import Extension, Markdown
from markdown.treeprocessors import Treeprocessor


class HtmlBook(Treeprocessor):
    
    def run(self, root: etree.Element) -> etree.Element | None:

        wrapper = []
        for child in root.findall('*'):
            if child.tag in ['nav', 'section', 'div']:
                break
            else:
                wrapper.append(child)

        if len(wrapper) > 0:
            preface = etree.Element('section')
            preface.attrib["data-type"] = 'preface'
            for child in wrapper:
                preface.append(child)
                root.remove(child)
            if preface.find('h1') is None:
                h1 = etree.Element('h1')
                h1.text = ' '
                preface.insert(0, h1)
            root.insert(0, preface)

        return root
    

class HtmlBookExtension(Extension):

    """ Extension for HtmlBook.

        Wraps all content prior to the first section into preface sections.
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.treeprocessors.register(HtmlBook(md), 'HtmlBook', 900)


def makeExtension(**kwargs):

    return HtmlBookExtension(**kwargs)
