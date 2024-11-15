'''
Host data template extension
============================

Converts {host:xyz} to the host information 'xyz'.

Original code Copyright [Matthias Hölzer-Klüpfel](https://www.hoelzer-kluepfel.de/).
'''

import platform

import markdown


class TemplateInlineProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern, config):
        super(TemplateInlineProcessor, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        a = m.group(0)
        label = m.group(1).strip()
        if ('machine' == label):
            a = platform.machine()
        elif ('node' == label):
            a = platform.node()
        elif ('platform' == label):
            a = platform.platform()
        elif ('processor' == label):
            a = platform.processor()
        elif ('release' == label):
            a = platform.release()
        elif ('system' == label):
            a = platform.system()
        elif ('version' == label):
            a = platform.version()

        return a, m.start(0), m.end(0)


class TemplateHostExtension(markdown.extensions.Extension):

    def extendMarkdown(self, md):
        TEMPLATE_RE = r'\{host:(\w+)\}'
        templatePattern = TemplateInlineProcessor(TEMPLATE_RE, self.getConfigs())
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'template-host', 80)


def makeExtension(**kwargs):
    return TemplateHostExtension(**kwargs)
