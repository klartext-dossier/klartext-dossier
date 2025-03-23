"""An example plugin lexer for Pygments."""

import re
from pygments.lexer import RegexLexer, DelegatingLexer, bygroups, using
from pygments.token import *
from pygments.lexers.markup import MarkdownLexer

class KtLexer(RegexLexer):

    name      = "Klartext Markup Language"
    aliases   = ["klartext", "kt"]
    filenames = ["*.kt"]
    mimetypes = ["text/x-klartext"]
    flags     = re.MULTILINE

    tokens = {
        'root': [           
            # directives
            (r'^([ \t]*)(!include|!import)([ \t]+)(\"[^\"]+\")(?:([ \t]+)(as)([ \t]+)(\w+))?(.*)$', bygroups(Whitespace, Keyword, Whitespace, Comment.PreprocFile, Whitespace, Keyword, Whitespace, Name.Namespace, Whitespace)),

            # tags
            (r'^([ \t]*)(\w+::)?([\w-]+)(:)([ \t]*)(#[\w\-\.]+)?([ \t]*)(?:([\w\-]+[ \t]*)(=)([ \t]*)(\"[^\"]*\")([ \t]*))*(.*)$', bygroups(Whitespace, Name.Namespace, Name.Tag, Operator, Whitespace, String.Symbol, Whitespace, Name.Attribute, Operator, Whitespace, String, Whitespace, Other)),

            # links
            (r'^([ \t]*)(\w+::)?([\w\-]+)(>)([ \t]*)([\w\-\.]+)([ \t]*)(?:([\w\-]+[ \t]*)(=)([ \t]*)(\"[^\"]*\")([ \t]*))*(.*)$', bygroups(Whitespace, Name.Namespace, Name.Tag, Operator, Whitespace, String.Symbol, Whitespace, Name.Attribute, Operator, Whitespace, String, Whitespace, Other)),

            # content
            (r'.*\n', Other)
        ]
    }


class KlartextLexer(DelegatingLexer):
    def __init__(self, **options):
        super().__init__(MarkdownLexer, KtLexer, **options)