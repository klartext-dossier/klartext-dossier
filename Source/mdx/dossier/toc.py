"""
Table of Contents Extension for Python-Markdown
===============================================

See <https://Python-Markdown.github.io/extensions/toc>
for documentation.

Oringinal code Copyright 2008 [Jack Miller](http://codezen.org)

All changes Copyright 2008-2014 The Python Markdown Project

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

"""

import re

import xml.etree.ElementTree as etree

from markdown import Extension
from markdown.treeprocessors import Treeprocessor


SKIPPED_TAGS = ['pre', 'code', 'blockquote']
HEADER_TAGS = re.compile("[Hh][123456]")
TOC_TAG = re.compile(r'\[TOC(,\s*(?P<title>[^,\]]+)(,\s*(?P<level>\d+))?)?\s*\]')

class TocTreeprocessor(Treeprocessor):
    
    def iterparent(self, node):
        ''' Iterator wrapper to get allowed parent and child all at once. '''
        for child in node:
            if not HEADER_TAGS.match(child.tag) and child.tag not in SKIPPED_TAGS:
                yield node, child
                for p, c in self.iterparent(child):
                    yield p, c

    def replace_marker(self, root):
        ''' Replace marker. '''

        nav = etree.Element('nav')
        nav.attrib["data-type"] = 'toc'

        for (p, c) in self.iterparent(root):
            text = ''.join(c.itertext()).strip()
            if not text:
                continue

            # To keep the output from screwing up the
            # validation by putting a <nav> inside of a <p>
            # we actually replace the <p> in its entirety.
            if c.text:
                m = TOC_TAG.match(c.text.strip())
                if m:
                    for i in range(len(p)):
                        if p[i] == c:
                            header = etree.SubElement(nav, "h1")
                            if m.group('title'):
                                header.text = m.group('title')
                            else:
                                header.text = "Table of Contents"

                            if m.group('level'):
                                nav.attrib['level'] = m.group('level')

                            p[i] = nav
                            break

        toc = self.md.serializer(nav)
        for pp in self.md.postprocessors:
            toc = pp.run(toc)


    def run(self, doc):

        self.replace_marker(doc)



class TocExtension(Extension):

    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.treeprocessors.register(TocTreeprocessor(md), 'toc', 5000)


def makeExtension(**kwargs):
    return TocExtension(**kwargs)
