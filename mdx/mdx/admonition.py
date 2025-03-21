""" Module providing the admonition extension for Markdown.

    This code is largely based on the original admonition extension provided with Python Markdown.

    Below is the original module comment:

    Admonition extension for Python-Markdown
    ========================================

    Adds rST-style HTMLBOOK_ADMONITIONS. Inspired by [rST]() feature with the same name.

    [rST]: http://docutils.sourceforge.net/docs/ref/rst/directives.html#specific-HTMLBOOK_ADMONITIONS  # noqa

    See <https://Python-Markdown.github.io/extensions/admonition>
    for documentation.

    Original code Copyright [Tiago Serafim](http://www.tiagoserafim.com/).

    All changes Copyright The Python Markdown Project

    License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import re

import xml.etree.ElementTree as etree

from markdown import Extension, Markdown
from markdown.blockprocessors import BlockProcessor


HTMLBOOK_ADMONITIONS = ['note', 'warning', 'tip', 'caution', 'important', 'sidebar']


class AdmonitionProcessor(BlockProcessor):

    CLASSNAME = 'admonition'
    CLASSNAME_TITLE = 'admonition-title'
    RE = re.compile(r'(?:^|\n)!!! ?([\w\-]+(?: +[\w\-]+)*)(?: +"(.*?)")? *(?:\n|$)')
    RE_SPACES = re.compile('  +')

    def test(self, parent: etree.Element, block: str) -> bool:

        sibling = self.lastChild(parent)

        match = self.RE.search(block)
        if match is not None:
            return True

        return (block.startswith(' ' * self.tab_length) and sibling is not None and sibling.get('data-type', '') in HTMLBOOK_ADMONITIONS)


    def run(self, parent: etree.Element, blocks: list[str]) -> None:

        div = self.lastChild(parent)
        block = blocks.pop(0)
        m = self.RE.search(block)

        if m:
            block = block[m.end():]  # removes the first line

        block, theRest = self.detab(block)

        if m:
            klass, title = self.get_class_and_title(m)
            div = etree.SubElement(parent, 'div')

            if not klass in HTMLBOOK_ADMONITIONS:
                klass = 'note'
            div.set('data-type', klass)

            if title:
                p = etree.SubElement(div, 'h1')
                p.text = title

            if 'sidebar' == klass:
                div.tag = 'aside'                                

        if div is not None:
            self.parser.parseChunk(div, block)

        if theRest:
            # This block contained unindented line(s) after the first indented
            # line. Insert these lines as the first block of the master blocks
            # list for future processing.
            blocks.insert(0, theRest)


    def get_class_and_title(self, match: re.Match) -> tuple[str, str]:

        klass, title = match.group(1).lower(), match.group(2)
        klass = self.RE_SPACES.sub(' ', klass)

        if title is None:
            # no title was provided, use the capitalized classname as title
            title = klass.split(' ', 1)[0].capitalize()
        elif title == '':
            # an explicit blank title should not be rendered
            title = None

        return klass, title


class AdmonitionExtension(Extension):

    """ Extension for Admonitions.

        Converts markdown admonitions into htmlbook compliant xhtml.

        Examples:

            The input:

                !!! note "Note title"
                    Any number of other indented markdown elements.

            will be converted to:

                <div data-type="note">
                    <h1>Note title</h1>
                    <p>Any number of other indented markdown elements.</p>
                </div>
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.parser.blockprocessors.register(AdmonitionProcessor(md.parser), 'admonition', 105)


def makeExtension(**kwargs):

    return AdmonitionExtension(**kwargs)
