''' Module providing the htmlbook extension for Markdown.

    This code is largely based on the original mdx_outline extension found at: https://github.com/aleray/mdx_outline

    Copyright
    - 2011, 2012 [The active archives contributors](http://activearchives.org/)
    - 2011, 2012 [Michael Murtaugh](http://automatist.org/)
    - 2011, 2012, 2017 [Alexandre Leray](http://stdin.fr/)

    This software is released under the modified BSD License.
''' 

# This code is largely based on the original mdx_outline extension found at: https://github.com/aleray/mdx_outline

# Below is part of the original module comment:

# Outline extension for Python-Markdown
# =====================================

# Wraps the document logical sections (as implied by h1-h6 headings).

# By default, the wrapper element is a section tag having a class attribute
# "sectionN", where N is the header level being wrapped. Also, the header
# attributes get moved to the wrapper.

# Copyright
# ---------

# - 2011, 2012 [The active archives contributors](http://activearchives.org/)
# - 2011, 2012 [Michael Murtaugh](http://automatist.org/)
# - 2011, 2012, 2017 [Alexandre Leray](http://stdin.fr/)

# All rights reserved.

# This software is released under the modified BSD License.
# See LICENSE.md for details.

# Further credits
# ---------------

# This is a rewrite of the
# [mdx_addsection extension](http://git.constantvzw.org/?p=aa.core.git;a=blob;f=aacore/mdx_addsections.py;h=969e520a42b0018a2c4b74889fecc83a7dd7704a;hb=HEAD)

import re, string

import xml.etree.ElementTree as etree

from markdown import Extension, Markdown
from markdown.treeprocessors import Treeprocessor
from markdown.postprocessors import Postprocessor


class HtmlBookDocument(Postprocessor):

    def run(self, text: str) -> str:

        templates = dict()
        templates['text'] = text
        templates['meta'] = ""

        if hasattr(self.md, 'Meta'):
            if 'title' in self.md.Meta:
                templates['title'] = string.Template('<title>$title</title>\n').safe_substitute(title=self.md.Meta['title'][0])
            else:
                templates['title'] = "<title> </title>"
            m = ''
            for key, values in self.md.Meta.items():
                m += string.Template('<meta name="$name" content="$content"/>\n        ').safe_substitute(name=key, content=values[0])
            if m:
                templates['meta'] = m

        doc  = string.Template('''\
<?xml version="1.0" encoding="UTF-8" ?>

<html xmlns="http://www.w3.org/1999/xhtml">

    <head>
        $title $meta
        <link rel="stylesheet" type="text/css" href="htmlbook.css"/>
    </head>

    <body data-type="book">
        $text
    </body>

</html>''')

        return doc.safe_substitute(templates)


class HtmlBookOutline(Treeprocessor):
    
    def process_titlepage(self, node: etree.Element) -> None:

        wrapper = []
        header = None
        for child in list(node):
            if child.tag in ['nav', 'section', 'div']:
                break
            elif child.tag in ['h1', 'header']:
                header = child
            else:
                wrapper.append(child)

        if len(wrapper) > 0:
            preface = etree.Element('section')
            preface.attrib["data-type"] = 'preface'
            for child in wrapper:
                preface.append(child)
                node.remove(child)
            if preface.find('h1') is None:
                h1 = etree.Element('h1')
                h1.text = ' '
                preface.insert(0, h1)
            node.insert(0, preface)

        if header is not None:
            node.remove(header)
            titlepage = etree.Element('section')
            titlepage.attrib["data-type"] = 'titlepage'
            titlepage.append(header)
            node.insert(0, titlepage)


    def process_outline(self, node: etree.Element) -> None:
    
        stack: list[tuple[etree.Element, int]] = []

        in_part = False

        pattern = re.compile(r'^h(\d)')

        for child in list(node):

            # work on the <h1> - <h6> attributes
            match = pattern.match(child.tag.lower())
            if match:                
                depth = int(match.group(1))            

                if depth > 1:
                
                    # a part ends when a new depth 2 element is seen
                    if (in_part) and (2 == depth):
                        in_part = False

                    # create a wrapper tag
                    if (2 == depth) and (child.get('class') == 'part'):
                        section = etree.SubElement(node, 'div')
                        in_part = True
                    else:
                        section = etree.SubElement(node, 'section')                    

                    # move attributes to the wrapper tag
                    for key, value in list(child.attrib.items()):
                        section.set(key, value)
                        del child.attrib[key]

                    # set the data-type and header
                    if in_part:
                        section.attrib['data-type'] = ['part', 'chapter', 'sect1', 'sect2', 'sect3', 'sect4', 'sect5'][depth-2]
                        child.tag = ['h1', 'h1', 'h1', 'h2', 'h3', 'h4', 'h5'][depth-2]
                    else:
                        section.attrib['data-type'] = ['chapter', 'sect1', 'sect2', 'sect3', 'sect4', 'sect5'][depth-2]
                        child.tag = ['h1', 'h1', 'h2', 'h3', 'h4', 'h5'][depth-2]
                    
                    # correct the data-type for structural elements
                    if (2 == depth) and (section.get('class') in ['preface', 'halftitlepage', 'titlepage', 'copyright-page', 'dedication', 'colophon', 'acknowledgments', 'conclusion', 'bibliography', 'glossary', 'appendix']):
                        klass = section.get('class')
                        if klass is not None:
                            section.set('data-type', klass)
                    
                    # convert a .toc section to a table of contents
                    if (2 == depth) and (section.get('class') == 'toc'):                    
                         section.tag = 'nav'
                         section.set('data-type', 'toc')
                    
                    # do not use class when data-type is enough
                    if section.get('class') == section.get('data-type'):
                        del section.attrib['class']

                    # replace the child node with the wrapper
                    section.append(child)
                    node.remove(child)
                else:
                    continue

                while stack:
                    container, container_depth = stack[-1]
                    if depth <= container_depth:
                        stack.pop()
                    else:
                        container.append(section)
                        node.remove(section)
                        break

                stack.append((section, depth))

            elif stack:
                container, container_depth = stack[-1]
                container.append(child)
                node.remove(child)


    def run(self, root: etree.Element) -> etree.Element | None:
    
        self.process_outline(root)
        self.process_titlepage(root)

        return root


class HtmlBookExtension(Extension):

    """ Extension for HtmlBook.

        Wraps all content prior to the first section into preface sections.
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.postprocessors.register(HtmlBookDocument(md), 'htmlbook_document', 400)
        md.treeprocessors.register(HtmlBookOutline(md), 'htmlbook_outline', 7)


def makeExtension(**kwargs):

    return HtmlBookExtension(**kwargs)
