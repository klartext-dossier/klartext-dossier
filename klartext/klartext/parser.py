""" Module providing a parser for the klartext markup language.
"""

import logging, re, collections, os, io, hashlib
from typing import Callable, Tuple
import markdown

from klartext import ParseError, Token


# reused instance of the markdown parser
markdownInstance = markdown.Markdown(extensions=['klartext.inline', 'klartext.glossary'])


class Parser:

    """ Parser for the klartext markup language.
    """

    TAB_WIDTH = 4

    # Regular expressions used for parsing
    ATTR_RE    = re.compile(r'\s*(?P<name>[\w_\-]+)\s*=\s*"(?P<value>[^"]*)"\s*')
    TAG_RE     = re.compile(r'^\s*'
                            r'((?P<prefix>\w+)\:\:)?(?P<tag>[\w\-_]+)(\.(?P<class>[\w\-_]+))?'
                            r'((:\s*(#((?P<idprefix>\w+)\:\:)?(?P<id>[\w\-_\.]+)\s*)?)|(>\s*((?P<refprefix>\w+)\:\:)?(?P<ref>\S+)))'
                            r'\s*'
                            r'(\[(?P<language>([a-zA-Z]{2,3}(-[a-zA-Z]{2,3})?))\]\s*)?'
                            r'(?P<rest>([\w\-_]+\s*=\s*"[^"]*"\s*)*)'
                            r'(?P<content>.*)?'
                            r'$')       
    INCLUDE_RE = re.compile(r'^\s*!include\s+"(?P<file>[^"]+)"\s*$')
    IMPORT_RE  = re.compile(r'^\s*!import\s+"(?P<namespace>[^"]+)"\s+as\s+(?P<prefix>\w+)\s*$')
    VERB_RE    = re.compile(r'^\s*```')


    @staticmethod
    def removeSurroundingBlankLines(text: str, namespaces: dict[str, str]) -> str:
        
        """ Default conversion for text content.
        
            Removes leading and trailing blank lines from text content.

            Args:
                text: The text content
                namespaces: The namespaces defined in the klartext file

            Returns:
                The text content without leading and trailing blank lines
        """        
        lines = collections.deque(text.splitlines())
        while (len(lines)>0) and (0 == len(lines[0].strip())):
            lines.popleft()
        while (len(lines)>0) and (0 == len(lines[len(lines)-1])):
            lines.pop()        
        return '\n'.join(lines)


    @staticmethod
    def convertMarkdown(text: str, namespaces: dict[str, str]) -> str:
        
        """ Markdown conversion for text content.
        
            Converts the text content from Markdown to xhtml.

            Args:
                text:       The text content
                namespaces: The namespaces defined in the klartext file

            Returns:
                The text content converted from Markdown to xhtml
        """        
        markdownInstance.namespaces = namespaces
        return markdownInstance.reset().convert(text)


    @staticmethod
    def _indentSpaces(indent: int) -> str:
        return ' ' * Parser.TAB_WIDTH * indent
    

    @staticmethod
    def _getAttributes(rest: str) -> dict:  
        result = {}
        if rest:
            for match in re.finditer(Parser.ATTR_RE, rest):
                result[match.group('name')] = match.group('value')
        return result
    

    @staticmethod
    def _convertAttributes(attribs: dict) -> str:
        result = ' '
        for key, value in attribs.items():
            result += f'{key}="{value}" '
        return result.rstrip()        


    @staticmethod
    def _convertBlankLinesToText(tokens: list[Token]) -> list[Token]:
        for i in range(len(tokens)-1, 0, -1):
            if Token.EMPTY == tokens[i]:
                if Token.TEXT == tokens[i-1]:
                    indent = tokens[i-1].indent()
                    tokens[i] = Token(indent, Token.TEXT, '')
                else:
                    del tokens[i]
        return tokens


    @staticmethod
    def _replaceTabsWithSpaces(text: str) -> str:
        return text.rstrip().expandtabs(Parser.TAB_WIDTH)


    @staticmethod
    def lookupIncludeFile(filename: str, basedir: str) -> str:

        """ Default lookup for include files.

            Tries to locate the include file relative to the basedir.
        
            Args:
                filename: Name of the include file to lookup
                basedir:  Base directory for the lookup
        """        
        if basedir:
            return os.path.join(basedir, filename)
        return filename


    def __init__(self) ->  None:

        """ Creates a parser.
        """
        self.context: list[Tuple[io.TextIOBase, int, str]] = []
        self.namespaces: dict[str, str] = {}
        self.lookup: Callable[[str, str], str] | None = None
        self.verbatim: bool = False


    def _getIndent(self, line: str) -> int:
        if 0 == len(line.strip()):
            return 0
        d = len(line) - len(line.lstrip())
        if (0 != (d % Parser.TAB_WIDTH)) and not self.verbatim:
            raise ParseError(f'Incorrect indentation: {d}, |{line}|')        
        return d // Parser.TAB_WIDTH


    def _include(self, filename: str, indent: int) -> None:
        try:
            _, _, basedir = self.context[-1]
            include_file_name = filename
            if self.lookup:
                include_file_name = self.lookup(filename, basedir)
            include_file = open(include_file_name, mode='r', encoding='utf-8')
            logging.info(f'Including klartext file "{include_file}"')        
            basedir = os.path.dirname(include_file_name)
            self.context.append((include_file, indent, basedir))    
        except:
            raise ParseError(f'Failed to include klartext file "{filename}"')  
        

    def _readLine(self) -> str:

        infile, indent, _ = self.context[-1]

        line = infile.readline()

        # ignore comment lines
        if not self.verbatim:
            while line.lstrip().startswith('//'):
                line = infile.readline()

        # end of file
        if line == '':
            if len(self.context) > 1:
                include_file, _, _ = self.context.pop()
                include_file.close()           
                return self._readLine()
            else:
                return ''

        return Parser._indentSpaces(indent) + line

    def _prefixed_id(self, id: str, prefix: str | None) -> str:
        if prefix:
            if prefix in self.namespaces:
                prefix = self.namespaces[prefix]
            else:
                raise ParseError(f'Namespace prefix "{prefix}" has not been imported')
            return hashlib.md5(prefix.encode('utf-8')).hexdigest() + "__" + id
        else:
            if id in self.namespaces:
                id = self.namespaces[id]
                return hashlib.md5(id.encode('utf-8')).hexdigest()
            else:
                return id

    def _nextToken(self) -> Token:
        current_line = self._readLine()

        if '' == current_line:
            return Token(0, Token.EOF, None) 
        
        current_line = Parser._replaceTabsWithSpaces(current_line)

        if len(current_line) == 0:
            return Token(0, Token.EMPTY, None)  

        # verbatim environments         
        match_verb = self.VERB_RE.match(current_line)
        if match_verb:
            d = len(current_line) - len(current_line.lstrip())
            if not self.verbatim:
                self.verbatim = True
                self.verb_indent = self._getIndent(current_line)
            elif d == self.verb_indent*Parser.TAB_WIDTH:
                self.verbatim = False
            else:
                return Token(self.verb_indent, Token.TEXT, current_line[self.verb_indent*Parser.TAB_WIDTH:])    
            return Token(self.verb_indent, Token.TEXT, current_line[d:])
        if self.verbatim:
            return Token(self.verb_indent, Token.TEXT, current_line[self.verb_indent*self.TAB_WIDTH:])

        # import directive
        match_import = self.IMPORT_RE.match(current_line)
        if match_import:
            namespace = match_import.group('namespace')
            prefix = match_import.group('prefix')
            if (prefix in self.namespaces) and (namespace != self.namespaces[prefix]):
                logging.warning(f'Namespace prefix "{prefix}" is already defined!')
            self.namespaces[prefix] = namespace
            logging.debug(f'Registered namespace "{namespace}" as prefix "{prefix}"')
            return self._nextToken()

        # get the current indent
        indent = self._getIndent(current_line)        
        current_line = current_line.lstrip()

        # include directive
        match_include = self.INCLUDE_RE.match(current_line)
        if match_include:       
            self._include(match_include.group('file'), indent)
            return self._nextToken()

        # tag
        match_tag = self.TAG_RE.match(current_line)
        if match_tag:
            a = Parser._getAttributes(match_tag.group('rest'))
            if match_tag.group('id'):
                a['id'] = self._prefixed_id(match_tag.group('id'), match_tag.group('idprefix'))
            if match_tag.group('ref'):
                a['ref'] = self._prefixed_id(match_tag.group('ref'), match_tag.group('refprefix'))
            if match_tag.group('class'):
                a['class'] = match_tag.group('class')
            if match_tag.group('language'):
                a['xml:lang'] = match_tag.group('language')
            if match_tag.group('prefix'):
                prefix = match_tag.group('prefix')
                if prefix in self.namespaces:
                    namespace = self.namespaces[match_tag.group('prefix')]
                else:
                    raise ParseError(f'Namespace prefix "{prefix}" has not been imported')
            else:
                prefix = None
                namespace = None
                
            return Token(indent, Token.TAG, { Token.TAG: match_tag.group('tag'), 'attribs': a, 'content': match_tag.group('content'), 'prefix': prefix, 'namespace': namespace } )

        # line of text
        return Token(indent, Token.TEXT, current_line)


    def _getTokens(self) -> list[Token]:
        tokens = []
        
        token = self._nextToken()
        tokens.append(token)
        while token != Token.EOF: 
            token = self._nextToken()
            tokens.append(token)

        return tokens


    def parse(self, infile: io.TextIOBase, convert_text: Callable[[str, dict[str,str]], str] = removeSurroundingBlankLines, basedir: str = "", lookup: Callable[[str, str], str] = lookupIncludeFile) -> bytes:

        """ Parse a klartext file.

            Parses a klartext file and returns an XML representation.

            Args:
                infile:       The text file to parse
                convert_text: Callback function to convert the content of text nodes
                basedir:      Directory used as base when looking up included files
                lookup:       Callback function used to lookup include files

            Returns:
                UTF-8 enoded byte string containing the XML representation of the klartext file
        """        
        self.context = [(infile, 0, basedir)]
        self.namespaces = {}
        self.lookup = lookup
        self.verbatim = False

        tokens = self._getTokens()
        tokens = Parser._convertBlankLinesToText(tokens)

        # convert the tags to XML
        level = 0
        found = True
        while found:
            found = False
            i = 0
            while i < len(tokens):
                indent = tokens[i].indent()
                attribs = tokens[i].content()

                if (level == indent) and (Token.TAG == tokens[i]):
                    found = True
                    
                    tagname = attribs.get(Token.TAG)
                    a = Parser._convertAttributes(attribs.get('attribs'))

                    content = attribs.get('content')
                    if content:
                        if content.startswith('"') and content.endswith('"'):
                            content = content[1:-1]
                        elif convert_text is not None:
                            content = convert_text(Parser.removeSurroundingBlankLines(content, self.namespaces), self.namespaces)

                    prefix = attribs.get('prefix')
                    namespace = attribs.get('namespace')
                    if prefix and namespace:
                        tokens[i] = Token(indent, Token.XML, Parser._indentSpaces(indent) + f'<{prefix}:{tagname} xmlns:{prefix}="{namespace}"{a}>{content}')
                    else:
                        tokens[i] = Token(indent, Token.XML, Parser._indentSpaces(indent) + f'<{tagname}{a}>{content}')
                    for i in range(i+1, len(tokens)):
                        indent = tokens[i].indent()
                        if indent <= level:
                            break
                    if prefix and namespace:
                        tokens.insert(i, Token(level, Token.XML, Parser._indentSpaces(level) + f'</{prefix}:{tagname}>'))
                    else:
                        tokens.insert(i, Token(level, Token.XML, Parser._indentSpaces(level) + f'</{tagname}>'))
                i += 1
            level += 1

        # indent the text            
        for i in range(1, len(tokens)):
            if (Token.TEXT == tokens[i]) and (Token.TEXT == tokens[i-1]) and (tokens[i].indent() > tokens[i-1].indent()):
                tokens[i] = Token(tokens[i-1].indent(), tokens[i].type(), Parser._indentSpaces(tokens[i].indent() - tokens[i-1].indent()) + tokens[i].content())

        # log tokens
        for token in tokens:
            logging.debug(f'|{token}')

        # create the output text
        xml = ''
        i = 0
        while i <= len(tokens):
            text = tokens[i].content()
            if Token.XML == tokens[i]:
                xml += text + '\n'
            elif Token.TEXT == tokens[i]:
                text_content = ''
                while Token.TEXT == tokens[i]:
                    text_content += text +'\n'
                    i += 1
                    text = tokens[i].content()                
                if convert_text is not None:
                    xml += convert_text(Parser.removeSurroundingBlankLines(text_content, self.namespaces), self.namespaces) + '\n'
                else:
                    xml += text_content
                continue
            elif Token.EMPTY == tokens[i]:
                pass
            elif Token.EOF == tokens[i]:
                break
            else:
                print(tokens[i])
                raise ParseError('Parse error', tokens[i])
            i += 1

        return xml.encode('utf-8')