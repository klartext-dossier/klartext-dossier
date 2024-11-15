'''
Net data template extension
===========================

Converts {net:xyz} to the net information 'xyz'.

Original code Copyright [Matthias Hölzer-Klüpfel](https://www.hoelzer-kluepfel.de/).
'''

import socket

import markdown


class TemplateInlineProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern, config):
        super(TemplateInlineProcessor, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        a = m.group(0)
        label = m.group(1).strip()
        if ('name' == label):
            a = socket.getfqdn()

        return a, m.start(0), m.end(0)


class TemplateNetExtension(markdown.extensions.Extension):

    def extendMarkdown(self, md):
        TEMPLATE_RE = r'\{net:(\w+)\}'
        templatePattern = TemplateInlineProcessor(TEMPLATE_RE, self.getConfigs())
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'template-net', 80)


def makeExtension(**kwargs):
    return TemplateNetExtension(**kwargs)
