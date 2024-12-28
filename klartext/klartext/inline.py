''' Module providing the inline tags extension for Markdown.
'''

import xml.etree.ElementTree as etree
import markdown, re
from typing import Any


class InlineTagsProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern: str) -> None:

        super(InlineTagsProcessor, self).__init__(pattern)
        

    def handleMatch(self, m: re.Match[str], data: str) -> tuple[etree.Element | str | None, int | None, int | None]: # type: ignore[override]
    
        tag = m.group('tag')
        text = m.group('text')

        t = etree.Element(tag)
        t.text = text

        if m.group('class'):
            t.set('class', m.group('class'))
        
        return t, m.start(0), m.end(0)


class InlineTagsExtension(markdown.extensions.Extension):

    """ Extension for inline tags.

        Extends Markdown with the concept of inline tags.

        Example:
            The input:

                This is /em/some/ markup.

            will be converted to:

                This is <em>some</em> markup.
    """

    def extendMarkdown(self, md: markdown.Markdown) -> None:
       
        templatePattern = InlineTagsProcessor(r'/(?P<tag>[\w\-_]+)(\.(?P<class>[\w\-_]+))?/(?P<text>[^/]*)/')
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'inl', 80)


def makeExtension(**kwargs):
  
    return InlineTagsExtension(**kwargs)
