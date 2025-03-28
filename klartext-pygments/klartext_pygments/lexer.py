"""An example plugin lexer for Pygments."""

import re
from pygments.lexer import RegexLexer, DelegatingLexer, bygroups
from pygments.token import *
from pygments.lexers.markup import MarkdownLexer

__all__ = [ 'KtLexer' ]

class KtLexer(RegexLexer):

    name      = "Klartext Markup Language"
    aliases   = ["klartext", "kt"]
    filenames = ["*.kt"]
    mimetypes = ["text/x-klartext"]

    flags = re.MULTILINE

    tokens = {
        'root': [           
            # empty lines
            (r'^[ \t]*\n', Whitespace),

            # comments
            (r'^[ \t]*//.*\n', Comment.Singleline),

            # directives
            (r'^([ \t]*)(!include|!import)([ \t]+)(\"[^\"]+\")(?:([ \t]+)(as)([ \t]+)(\w+))?(.*\n)', bygroups(Whitespace, Keyword, Whitespace, Comment.PreprocFile, Whitespace, Keyword, Whitespace, Name.Namespace, Whitespace)),

            # links
            (r'^([ \t]*)(\w+::)?([\w\-]+)(>)([ \t]*)([\w\-\.]+)([ \t]*)(?:([\w\-]+[ \t]*)(=)([ \t]*)("[^"]*")([ \t]*))*(.*\n)', bygroups(Whitespace, Name.Namespace, Name.Tag, Operator, Whitespace, String.Symbol, Whitespace, Name.Attribute, Operator, Whitespace, String, Whitespace, Other)),

            # tags
            (r'^([ \t]*)(\w+::)?([\w-]+)(:)([ \t]*)(#[\w\-\.]+)?([ \t]*)(?:([\w-]+[ \t]*)(=)([ \t]*)("[^"]*")([ \t]*))*(.*)(\n)', bygroups(Whitespace, Name.Namespace, Name.Tag, Operator, Whitespace, String.Symbol, Whitespace, Name.Attribute, Operator, Whitespace, String, Whitespace, Other, Whitespace)),

            # content
            (r'.*?\n', Other)
        ]
    }


# class KlartextLexer(DelegatingLexer):

#     name      = "Klartext Markup Language"
#     aliases   = ["klartext", "kt"]
#     filenames = ["*.kt"]
#     mimetypes = ["text/x-klartext"]

#     def __init__(self, **options):
#         super().__init__(MarkdownLexer, KtLexer, **options)