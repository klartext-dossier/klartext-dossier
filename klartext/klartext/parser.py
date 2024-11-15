import logging, re, collections, os

from klartext import ParseError


class Parser:

    TAB_WIDTH = 4

    ATTR_RE = re.compile(r'\s*(?P<name>[\w_\-]+)\s*=\s*"(?P<value>[^"]*)"\s*')
    TAG_RE = re.compile(r'^\s*((?P<prefix>\w+)\:\:)?(?P<tag>[\w\-_]+)(\.(?P<class>[\w\-_]+))?:\s*(#(?P<id>[\w\-_\.]+)\s*)?(?P<rest>([\w\-_]+\s*=\s*"[^"]*"\s*)*)(?P<content>.*)?$')
    LINK_RE = re.compile(r'^\s*(?P<link>[\w\-_]+)>\s+(?P<ref>\S+)\s*(?P<rest>([\w\-_]+\s*=\s*"[^"]*"\s*)*)(?P<content>.*)?$')
    ID_RE = re.compile(r'\s+#(?P<id>[\w_]+)')
    INCLUDE_RE = re.compile(r'^\s*!include\s+"(?P<file>[^"]+)"\s*$')
    IMPORT_RE = re.compile(r'^\s*!import\s+"(?P<namespace>[^"]+)"\s+as\s+(?P<prefix>\w+)\s*$')
    VERB_RE = re.compile(r'^\s*```')


    @staticmethod
    def removeSurroundingBlankLines(text : str) -> str:     
        lines = collections.deque(text.splitlines())
        while (len(lines)>0) and (0 == len(lines[0].strip())):
            lines.popleft()
        while (len(lines)>0) and (0 == len(lines[len(lines)-1])):
            lines.pop()        
        return '\n'.join(lines)


    @staticmethod
    def indentSpaces(indent: int) -> str:
        return ' ' * Parser.TAB_WIDTH * indent
    

    @staticmethod
    def getAttributes(rest):  
        result = {}
        if rest:
            for match in re.finditer(Parser.ATTR_RE, rest):
                result[match.group('name')] = match.group('value')
        return result
    

    @staticmethod
    def tokenIs(tag, token):
        _, t, _ = token
        return tag == t


    @staticmethod
    def tokenIndent(token):
        i, _, _ = token
        return i
    

    @staticmethod
    def convertAttributes(attribs):
        result = ' '
        for key, value in attribs.items():
            result += f'{key}="{value}" '
        return result.rstrip()        


    @staticmethod
    def convertBlankLinesToText(tokens):
        # Convert required blank lines to text. Note that the range stops BEFORE the first element!
        for i in range(len(tokens)-1, 0, -1):
            if Parser.tokenIs('EMPTY', tokens[i]):
                if Parser.tokenIs('TEXT', tokens[i-1]):
                    indent, _, _ = tokens[i-1]
                    tokens[i] = (indent, 'TEXT', '')
                else:
                    del tokens[i]
        return tokens


    @staticmethod
    def replaceTabsWithSpaces(text):
        return text.rstrip().expandtabs(Parser.TAB_WIDTH)


    @staticmethod
    def lookupIncludeFile(filename, basedir):
        if basedir:
            return os.path.join(basedir, filename)
        return filename


    def __init__(self):
        self.context = []
        self.verbatim = False
        self.namespaces = {}
        self.lookup = None


    def getIndent(self, line: str) -> int:
        if 0 == len(line.strip()):
            return 0
        d = len(line) - len(line.lstrip())
        if (0 != (d % Parser.TAB_WIDTH)) and not self.verbatim:
            raise ParseError(f'Incorrect indentation: {d}, |{line}|')        
        return d // Parser.TAB_WIDTH


    def include(self, filename, indent):
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
        

    def readLine(self):

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
                return self.readLine()
            else:
                return ''

        return Parser.indentSpaces(indent) + line


    def nextToken(self):
        current_line = self.readLine()

        if '' == current_line:
            return (0, 'EOF', None) 
        
        current_line = Parser.replaceTabsWithSpaces(current_line)

        if len(current_line) == 0:
            return (0, 'EMPTY', None)  

        # verbatim environments         
        match_verb = self.VERB_RE.match(current_line)
        if match_verb:
            d = len(current_line) - len(current_line.lstrip())
            if not self.verbatim:
                self.verbatim = True
                self.verb_indent = self.getIndent(current_line)
            elif d == self.verb_indent*Parser.TAB_WIDTH:
                self.verbatim = False
            else:
                return (self.verb_indent, 'TEXT', current_line[self.verb_indent*Parser.TAB_WIDTH:])    
            return (self.verb_indent, 'TEXT', current_line[d:])
        if self.verbatim:
            return (self.verb_indent, 'TEXT', current_line[self.verb_indent*self.TAB_WIDTH:])

        # import directive
        match_import = self.IMPORT_RE.match(current_line)
        if match_import:
            namespace = match_import.group('namespace')
            prefix = match_import.group('prefix')
            if (prefix in self.namespaces) and (namespace != self.namespaces[prefix]):
                logging.warning(f'Namespace prefix "{prefix}" is already defined!')
            self.namespaces[prefix] = namespace
            logging.debug(f'Registered namespace "{namespace}" as prefix "{prefix}"')
            return self.nextToken()

        # get the current indent
        indent = self.getIndent(current_line)        
        current_line = current_line.lstrip()

        # include directive
        match_include = self.INCLUDE_RE.match(current_line)
        if match_include:       
            self.include(match_include.group('file'), indent)
            return self.nextToken()

        # tag
        match_tag = self.TAG_RE.match(current_line)
        if match_tag:
            a = Parser.getAttributes(match_tag.group('rest'))
            if match_tag.group('id'):
                a['id'] = match_tag.group('id')
            if match_tag.group('class'):
                a['class'] = match_tag.group('class')
            if match_tag.group('prefix'):
                prefix = match_tag.group('prefix')
                if prefix in self.namespaces:
                    namespace = self.namespaces[match_tag.group('prefix')]
                else:
                    raise ParseError(f'Namespace prefix "{prefix}" has not been imported')
            else:
                prefix = None
                namespace = None
                
            return (indent, 'TAG', { 'tag': match_tag.group('tag'), 'attribs': a, 'content': match_tag.group('content'), 'prefix': prefix, 'namespace': namespace } )
            
        # link
        match_link = self.LINK_RE.match(current_line)
        if match_link:
            attribs = Parser.getAttributes(match_link.group('rest'))
            attribs['ref'] = match_link.group('ref')
            return (indent, 'TAG', { 'tag': match_link.group('link'), 'attribs': attribs, 'content': match_link.group('content') } )

        # line of text
        return (indent, 'TEXT', current_line)


    def getTokens(self):
        tokens = []
        
        token = self.nextToken()
        tokens.append(token)
        while not Parser.tokenIs('EOF', token):           
            token = self.nextToken()
            tokens.append(token)

        return tokens


    def parse(self, infile, convert_text=removeSurroundingBlankLines, basedir=None, lookup=lookupIncludeFile):
        self.context = [(infile, 0, basedir)]
        self.verbatim = False
        self.namespaces = {}
        self.lookup = lookup

        tokens = self.getTokens()
        tokens = Parser.convertBlankLinesToText(tokens)

        # convert the tags to XML
        level = 0
        found = True
        while found:
            found = False
            i = 0
            while i < len(tokens):
                indent, tag, attribs = tokens[i]
                if (level == indent) and ('TAG' == tag):
                    found = True
                    
                    tagname = attribs.get('tag')
                    a = Parser.convertAttributes(attribs.get('attribs'))

                    content = attribs.get('content')
                    if content:
                        if content.startswith('"') and content.endswith('"'):
                            content = content[1:-1]
                        elif convert_text:
                            content = convert_text(Parser.removeSurroundingBlankLines(content))

                    prefix = attribs.get('prefix')
                    namespace = attribs.get('namespace')
                    if prefix and namespace:
                        tokens[i] = (indent, 'XML', Parser.indentSpaces(indent) + f'<{prefix}:{tagname} xmlns:{prefix}="{namespace}"{a}>{content}')
                    else:
                        tokens[i] = (indent, 'XML', Parser.indentSpaces(indent) + f'<{tagname}{a}>{content}')
                    for i in range(i+1, len(tokens)):
                        indent, _, _ = tokens[i]
                        if indent <= level:
                            break
                    if prefix and namespace:
                        tokens.insert(i, (level, 'XML', Parser.indentSpaces(level) + f'</{prefix}:{tagname}>'))
                    else:
                        tokens.insert(i, (level, 'XML', Parser.indentSpaces(level) + f'</{tagname}>'))
                i += 1
            level += 1

        # indent the text            
        for i in range(1, len(tokens)):
            l_i, tag_i, text_i = tokens[i]
            l_im, tag_im, _ = tokens[i-1]
            if ('TEXT' == tag_i) and ('TEXT' == tag_im) and (l_i > l_im):
                tokens[i] = (l_im, tag_i, Parser.indentSpaces(l_i - l_im) + text_i)

        # log tokens
        for token in tokens:
            i, t, a = token
            logging.debug(f'|{i:2} | {t:5} | {a}')

        # create the output text
        xml = ''
        i = 0
        while i <= len(tokens):
            indent, tag, text = tokens[i]
            if 'XML' == tag:
                xml += text + '\n'
            elif 'TEXT' == tag:
                text_content = ''
                while 'TEXT' == tag:
                    text_content += text +'\n'
                    i += 1
                    _, tag, text = tokens[i]                
                if convert_text:
                    xml += convert_text(Parser.removeSurroundingBlankLines(text_content)) + '\n'
                else:
                    xml += text_content
                continue
            elif 'EOF' == tag:
                break
            elif 'EMPTY' == tag:
                pass
            else:
                raise ParseError('Parse error', tokens[i])
            i += 1

        return xml.encode('utf-8')