""" Module providing the outline extension for Markdown.

    This code is largely based on the original mdx_outline extension found at: https://github.com/aleray/mdx_outline

    Below is part of the original module comment:

    Outline extension for Python-Markdown
    =====================================

    Wraps the document logical sections (as implied by h1-h6 headings).

    By default, the wrapper element is a section tag having a class attribute
    "sectionN", where N is the header level being wrapped. Also, the header
    attributes get moved to the wrapper.

    Copyright
    ---------

    - 2011, 2012 [The active archives contributors](http://activearchives.org/)
    - 2011, 2012 [Michael Murtaugh](http://automatist.org/)
    - 2011, 2012, 2017 [Alexandre Leray](http://stdin.fr/)

    All rights reserved.

    This software is released under the modified BSD License.
    See LICENSE.md for details.

    Further credits
    ---------------

    This is a rewrite of the
    [mdx_addsection extension](http://git.constantvzw.org/?p=aa.core.git;a=blob;f=aacore/mdx_addsections.py;h=969e520a42b0018a2c4b74889fecc83a7dd7704a;hb=HEAD)
"""

import re

import xml.etree.ElementTree as etree

from markdown import Extension, Markdown
from markdown.treeprocessors import Treeprocessor


class OutlineProcessor(Treeprocessor):

    def process_nodes(self, node: etree.Element) -> None:

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

        self.process_nodes(root)

        return root


class OutlineExtension(Extension):

    """ Extension for Outline.

        Converts markdown outline into htmlbook compliant xhtml.
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.treeprocessors.register(OutlineProcessor(md), 'outline', 1000)


def makeExtension(**kwargs):

    return OutlineExtension(**kwargs)
