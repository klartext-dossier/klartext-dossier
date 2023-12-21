'''
Inline tags extension
=====================

Copyright [Matthias Hölzer-Klüpfel](https://www.hoelzer-kluepfel.de/).
'''

import xml.etree.ElementTree as etree
import markdown


class InlineTagsProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern):
        super(InlineTagsProcessor, self).__init__(pattern)
        
    def handleMatch(self, m, data):
        tag = m.group('tag')
        text = m.group('text')

        t = etree.Element(tag)
        t.text = text

        if m.group('class'):
            t.set('class', m.group('class'))
        
        return t, m.start(0), m.end(0)


class GlossaryTagsProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern):
        super(GlossaryTagsProcessor, self).__init__(pattern)
        
    def handleMatch(self, m, data):
        text = m.group('text')

        t = etree.Element('g', xmlns='http://www.hoelzer-kluepfel.de/dossier')
        t.text = text
        
        return t, m.start(0), m.end(0)

class SymbolsProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern):
        super(SymbolsProcessor, self).__init__(pattern)
        
    def handleMatch(self, m, data):
        text = m.group('text')

        t = etree.Element('span')
        t.set('class', 'symbol')
        t.set('symbol', text)
        t.text = text
        
        return t, m.start(0), m.end(0)

class InlineTagsExtension(markdown.extensions.Extension):

    def __init__(self, **kwargs):
        super(InlineTagsExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        templatePattern = InlineTagsProcessor(r'/(?P<tag>[\w\-_]+)(\.(?P<class>[\w\-_]+))?/(?P<text>[^/]*)/')
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'inl', 80)

        templatePattern = GlossaryTagsProcessor(r'{(?P<text>\w[^}]+)}')
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'gls', 81)

        templatePattern = SymbolsProcessor(r'(?P<text>[♠♥♦♣⚠])')
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'sym', 82)


def makeExtension(**kwargs):  # pragma: no cover
    return InlineTagsExtension(**kwargs)
