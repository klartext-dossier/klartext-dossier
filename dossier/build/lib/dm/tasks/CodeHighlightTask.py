import logging

import pygments, pygments.lexer, pygments.lexers, pygments.formatters, pygments.token
from pygments.lexers.markup import MarkdownLexer

from lxml import etree

from dm.tasks.Content import Content
from dm.tasks.Task import Task


class KlartextLexer(pygments.lexer.RegexLexer):
    name = 'klartext'
    aliases = ['kt']
    filenames = ['*.kt']

    tokens = {
        'root': [
            # Whitespace at the beginning of the line
            (r'^\s+', pygments.token.Whitespace),

            # Comments
            (r'//.*$', pygments.token.Comment.Single),


            # Tags
            (r'(\w+::)?([\w_\-]+)(\.[\w_\-]+)?(:)', pygments.lexer.bygroups(pygments.token.Name.Namespace, pygments.token.Name.Class, pygments.token.Name.Class, pygments.token.Name.Class), 'tag'),

            # Links
            (r'(\w+::)?([\w_\-]+)(\.[\w_\-]+)?(>)',  pygments.lexer.bygroups(pygments.token.Name.Namespace, pygments.token.Name.Class, pygments.token.Name.Class, pygments.token.Name.Class), 'link'),

            # Directives
            (r'(#include)(\s+)("[^"]*")(\s*$)', pygments.lexer.bygroups(pygments.token.Comment.Preproc, pygments.token.Whitespace, pygments.token.String.Double, pygments.token.Whitespace)),
            (r'(#import)(\s+)("[^"]*")(\s+as\s+)(.*$)', pygments.lexer.bygroups(pygments.token.Comment.Preproc, pygments.token.Whitespace, pygments.token.String.Double, pygments.token.Name.Class, pygments.token.Name.Namespace,)),
            
            # Text lines containing a colon
            (r'\S+\s.*:.*$', pygments.lexer.using(MarkdownLexer)),

            # Text
            (r'.+', pygments.lexer.using(MarkdownLexer))
        ],
        "tag": [ 
            (r'$', pygments.token.Whitespace, '#pop'),
            (r'\s+', pygments.token.Whitespace),
            (r'#[\w_\-]+', pygments.token.Number),
            (r'([\w\-_]+)(\s*=\s*)("[^"]*")', pygments.lexer.bygroups(pygments.token.Name.Attribute, pygments.token.Punctuation, pygments.token.String.Double)),
            (r'.+', pygments.lexer.using(MarkdownLexer))
        ],
        "link": [
            (r'$', pygments.token.Literal, '#pop'),
            (r'\s+', pygments.token.Whitespace),
            (r'([\w\-_]+)(\s*=\s*)("[^"]*"\s*)', pygments.lexer.bygroups(pygments.token.Name.Attribute, pygments.token.Punctuation, pygments.token.String.Double)),
            (r'[\w_\-]+', pygments.token.Number),
            (r'.+', pygments.lexer.using(MarkdownLexer))
        ]
    }


class CodeHighlightTask(Task):

    """ The code-highlight task.

        Adds highlighting to <code> tags.
    """

    def lookupLexer(self, language):
        if language is not None:
            try:                    
                if 'language-klartext' == language:
                    return KlartextLexer()
                else:
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
