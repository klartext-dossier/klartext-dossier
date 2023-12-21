'''
Meta data template extension
============================

Converts {meta:xyz} to the content of the 'xyz' meta data element.

Original code Copyright [Matthias Hölzer-Klüpfel](https://www.hoelzer-kluepfel.de/).
'''

import markdown


class TemplateMetaExtension(markdown.extensions.Extension):

    def __init__(self, **kwargs):
        super(TemplateMetaExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        TEMPLATE_RE = r'\{meta:(\w+)\}'
        templatePattern = TemplateInlineProcessor(TEMPLATE_RE, self.getConfigs())
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'template-meta', 80)


class TemplateInlineProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern, config):
        super(TemplateInlineProcessor, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        a = m.group(0)
        label = m.group(1).strip()
        if hasattr(self.md, 'Meta'):
            if label in self.md.Meta:
                a = self.md.Meta[label][0]

        return a, m.start(0), m.end(0)


def makeExtension(**kwargs):  # pragma: no cover
    return TemplateMetaExtension(**kwargs)
