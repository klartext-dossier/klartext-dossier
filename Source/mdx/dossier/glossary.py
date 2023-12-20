'''
Glossary extension
==================

Copyright [Matthias Hölzer-Klüpfel](https://www.hoelzer-kluepfel.de/).
'''

import re

import markdown


def reference(term):
    return re.sub(r'[^\w]+', '_', term)
    
    
class GlossaryInlineProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern, config):
        super(GlossaryInlineProcessor, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        text = m.group('term')
        label = reference(text)
        if m.group('reference'):
            text = m.group('reference')

        a = etree.Element('a')
        a.text = text
        a.set('href', '#' + label)
        a.set('data-type', 'xref')        

        return a, m.start(0), m.end(0)


class GlossaryExtension(markdown.extensions.Extension):

    def __init__(self, **kwargs):
        super(GlossaryExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        templatePattern = GlossaryInlineProcessor(r'\{g:(?P<term>[^:\}]+)(:(?P<reference>[^\}]+))?\}', self.getConfigs())
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'gls', 80)


def makeExtension(**kwargs):  # pragma: no cover
    return GlossaryExtension(**kwargs)
