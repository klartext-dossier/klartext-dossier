"""An example plugin lexer for Pygments."""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class KlartextLexer(RegexLexer):

    name      = "Klartext Markup Language"
    aliases   = ["klartext", "kt"]
    filenames = ["*.kt"]
    mimetypes = ["text/x-klartext"]

    tokens = {
        'root': [           
            # tags
            (r'^(\s*)(\w+::)?([\w_-]+)(\.[\w_-]+)?(:)(\s*)(#[\w\-_\.]+\s*)?(?:([\w\-_]+\s*)(=)(\s*)(\"[^\"]*\")(\s*))*(.*)$', bygroups(Whitespace, Name.Namespace, Name.Tag, Name.Class, Operator, Whitespace, String.Symbol, Name.Attribute, Operator, Whitespace, String, Whitespace, Text)),

            # directives
            (r'^(\s*)(!)(include|import)(\s+)(\"[^\"]+\")(?:(\s+)(as)(\s+)(\w+))?(.*)$', bygroups(Whitespace, Keyword, Keyword, Whitespace, Comment.PreprocFile, Whitespace, Keyword, Whitespace, Name.Namespace, Whitespace)),

            # other text
            (r'.*\n', Text),
        ]
    }