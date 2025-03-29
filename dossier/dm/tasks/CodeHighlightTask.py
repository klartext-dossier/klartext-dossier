import logging

import pygments, pygments.lexers

from lxml import etree

from dm.tasks.Content import Content
from dm.tasks.Task import Task


class CodeHighlightTask(Task):

    """ The code-highlight task.

        Adds highlighting to <code> tags.
    """

    def lookupLexer(self, language):
        if language is not None:
            try:                    
                return pygments.lexers.get_lexer_by_name(language.lstrip('language-'))
            except:
                logging.warning(f'{self.name} - cannot highlight language "{language}"; no lexer found.')
        return None                

    def tryHighlightingCode(self, child):
        language = child.get('class', None)
        lexer = self.lookupLexer(language)
        if lexer is None:
            if language is not None:
                logging.warn(f'{self.name} - no lexer for "{language}"')
            return child
        logging.debug(f'{self.name} - highlighting "{language}"')
        code = pygments.highlight(child.text, lexer, pygments.formatters.HtmlFormatter(nowrap=True, full=False))
        xml = etree.fromstring(code, parser=etree.HTMLParser()).find('body')
        if xml is not None:
            if xml.getchildren is not None:
                if 'p' == xml.getchildren()[0].tag:
                    xml = xml.getchildren()[0]
        xml.tag = 'code'
        xml.attrib['class'] = 'highlight'
        return xml

    def run(self, context):
        self.load()
        xml = self.content.getXML() 
        for child in xml.iter('{http://www.w3.org/1999/xhtml}code'):
            if child.getparent() is not None:
                child.getparent().replace(child, self.tryHighlightingCode(child))
        self.content.setData(etree.tostring(xml, encoding=Content.DEFAULT_ENCODING))
        self.content.encoding = Content.DEFAULT_ENCODING
        self.save()
