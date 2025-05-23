''' Module providing the glossary extension for Markdown.
'''

import xml.etree.ElementTree as etree
import markdown, re, hashlib

from klartext import ParseError


def reference(term):
    return re.sub(r'[^\w]+', '_', term).lower()
    
    
class GlossaryInlineProcessor(markdown.inlinepatterns.InlineProcessor):

    def __init__(self, pattern: str) -> None:
        super(GlossaryInlineProcessor, self).__init__(pattern)

    def handleMatch(self, m: re.Match[str], data: str) -> tuple[etree.Element | str | None, int | None, int | None]: # type: ignore[override]
        prefix = m.group('prefix')
        text = m.group('term')
        href = reference(text)

        if prefix:
            if prefix in self.md.namespaces:
                href = hashlib.md5(self.md.namespaces[prefix].encode('utf-8')).hexdigest() + '__' + href
            else:
                raise ParseError(f'Namespace prefix "{prefix}" has not been imported')

        a = etree.Element('a')
        a.text = text
        a.set('href', '#' + href)
        a.set('data-type', 'xref')        
        a.set('data-xrefstyle', 'glossary')        

        return a, m.start(0), m.end(0)


class GlossaryExtension(markdown.extensions.Extension):

    """ Extension for marking glossary entries.

        Extends Markdown with a simple method to mark glossary entries.

        Example:
            The input:

                This is {Markdown} markup.

            will be converted to:

                This is <a data-type="xref" data-xrefstyle="glossary" href="#markdown">Markdown</a>.
    """

    def extendMarkdown(self, md: markdown.Markdown) -> None:
        templatePattern = GlossaryInlineProcessor(r'{((?P<prefix>\w+):)?(?P<term>\w[^}]+)}')
        templatePattern.md = md
        md.inlinePatterns.register(templatePattern, 'gls', 80)


def makeExtension(**kwargs):
    return GlossaryExtension(**kwargs)
