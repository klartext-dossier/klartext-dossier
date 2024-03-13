import logging, re, os

from dm.utilities import tryLocatingFile
import dm.markdown_parser, dm.exceptions


class KlartextParser:

    TAB_WIDTH = 4

    ATTR_RE = re.compile(r'\s*(?P<name>[\w_\-]+)\s*=\s*"(?P<value>[^"]*)"\s*')
    TAG_RE = re.compile(r'^\s*((?P<prefix>\w+)\:\:)?(?P<tag>[\w\-_]+)(\.(?P<class>[\w\-_]+))?:\s*(#(?P<id>[\w\-_\.]+)\s*)?(?P<rest>([\w\-_]+\s*=\s*"[^"]*"\s*)*)(?P<content>.*)?$')
    LINK_RE = re.compile(r'^\s*(?P<link>[\w\-_]+)>\s+(?P<ref>\S+)\s*(?P<rest>([\w\-_]+\s*=\s*"[^"]*"\s*)*)(?P<content>.*)?$')
    ID_RE = re.compile(r'\s+#(?P<id>[\w_]+)')
    INCLUDE_RE = re.compile(r'^\s*!include\s+"(?P<file>[^"]+)"\s*$')
    IMPORT_RE = re.compile(r'^\s*!import\s+"(?P<namespace>[^"]+)"\s+as\s+(?P<prefix>\w+)\s*$')
    VERB_RE = re.compile(r'^\s*```')


    def __init__(self, infile, context):

        self.context = context
        self.context.set_infile(infile) # TODO: Do this at the caller?! Add another context?
        self.initial_contexts = len(self.context.scopes)
        self.line = None     
        self.verbatim = False   
        self.verb_indent = 0


    @staticmethod
    def getIndent(line):

        if len(line.strip()) == 0:
            return 0
        d = len(line) - len(line.lstrip())
        if 0 != (d % KlartextParser.TAB_WIDTH):
            logging.warning(f'Incorrect indentation: {d}, |{line}|')            
        return d // KlartextParser.TAB_WIDTH


    @staticmethod
    def getAttributes(rest):  

        result = {}
        if rest:
            for match in re.finditer(KlartextParser.ATTR_RE, rest):
                result[match.group('name')] = match.group('value')
        return result
    

    def tokenIs(self, tag, token):

        _, t, _ = token
        return tag == t


    def tokenIndent(self, token):

        i, _, _ = token
        return i


    def dump(self, token):

        i, t, a = token
        logging.debug(f'|{i:2} | {t:5} | {a}')


    def include(self, filename, indent):

        try:
            include_file = tryLocatingFile(filename, self.context.basedir())
            f = open(include_file, mode='r', encoding='utf-8')
            basedir = None
            if len(include_file) > 0:
                basedir = os.path.dirname(include_file)
            self.context.__enter__()
            self.context.set_indent(indent)
            self.context.set_basedir(basedir)
            self.context.set_infile(f)
            logging.info(f'Including klartext file "{include_file}"')
            logging.debug(self.context)
        except Exception as e:
            logging.error(f'Failed to include klartext file "{filename}"')
            raise


    def readLine(self):

        infile = self.context.infile()
        indent = self.context.indent()

        line = infile.readline()
        if not self.verbatim:
            while line.lstrip().startswith('//'):
                line = infile.readline()

        if line == '':
            if len(self.context.scopes) > self.initial_contexts:
                f = self.context.infile()
                f.close()
                self.context.__exit__()
                logging.debug(self.context)
                return self.readLine()
            else:
                return ''

        return ' ' * KlartextParser.TAB_WIDTH * indent + line


    def nextToken(self):

        # read a new line
        self.line = self.readLine()
        if '' == self.line:
            return (0, 'EOF', None)

        # replace tabs with spaces
        self.line = self.line.rstrip().expandtabs(self.TAB_WIDTH)

        # empty line
        if len(self.line) == 0:
            self.line = None
            return (0, 'EMPTY', None)  

        # verbatim environments         
        match_verb = self.VERB_RE.match(self.line)
        if match_verb:
            d = len(self.line) - len(self.line.lstrip())
            if not self.verbatim:
                self.verbatim = True
                self.verb_indent = KlartextParser.getIndent(self.line)
            elif d == self.verb_indent*self.TAB_WIDTH:
                self.verbatim = False
            else:
                return (self.verb_indent, 'TEXT', self.line[self.verb_indent*self.TAB_WIDTH:])    
            return (self.verb_indent, 'TEXT', self.line[d:])
        if self.verbatim:
            return (self.verb_indent, 'TEXT', self.line[self.verb_indent*self.TAB_WIDTH:])

        # include directive
        match_include = self.INCLUDE_RE.match(self.line)
        if match_include:
            filename = match_include.group('file')
            self.include(filename, KlartextParser.getIndent(self.line))
            return self.nextToken()

        # import directive
        match_import = self.IMPORT_RE.match(self.line)
        if match_import:
            namespace = match_import.group('namespace')
            prefix = match_import.group('prefix')
            if (prefix in self.context.namespaces()) and (namespace != self.context.namespaces()[prefix]):
                logging.warn(f'Namespace prefix "{prefix}" is already defined!')
            self.context.namespaces()[prefix] = namespace
            logging.debug(f'Registered namespace "{namespace}" as prefix "{prefix}"')
            return self.nextToken()

        # get the current indent
        indent = KlartextParser.getIndent(self.line)        
        self.line = self.line.lstrip()

        # tag
        match_tag = self.TAG_RE.match(self.line)
        if match_tag:
            self.line = None

            a = KlartextParser.getAttributes(match_tag.group('rest'))
            if match_tag.group('id'):
                a['id'] = match_tag.group('id')
            if match_tag.group('class'):
                a['class'] = match_tag.group('class')
            if match_tag.group('prefix'):
                prefix = match_tag.group('prefix')
                if prefix in self.context.namespaces():
                    namespace = self.context.namespaces()[match_tag.group('prefix')]
                else:
                    logging.warn(f'Namespace prefix "{prefix}" is not defined!')
                    namespace = None
                    prefix = None
            else:
                prefix = None
                namespace = None
                
            return (indent, 'TAG', { 'tag': match_tag.group('tag'), 'attribs': a, 'content': match_tag.group('content'), 'prefix': prefix, 'namespace': namespace } )
            
        # link
        match_link = self.LINK_RE.match(self.line)
        if match_link:
            self.line = None
            attribs = KlartextParser.getAttributes(match_link.group('rest'))
            attribs['ref'] = match_link.group('ref')
            return (indent, 'TAG', { 'tag': match_link.group('link'), 'attribs': attribs, 'content': match_link.group('content') } )

        # line of text
        t = self.line
        # print(f'|{indent}|{self.line}| -> TEXT')
        self.line = None
        return (indent, 'TEXT', t)


    def getTokens(self):
        
        tokens = []
        
        token = self.nextToken()
        tokens.append(token)
        while not self.tokenIs('EOF', token):           
            token = self.nextToken()
            tokens.append(token)

        return tokens


    def convertAttributes(self, attribs):

        result = ' '
        for key, value in attribs.items():
            result += f'{key}="{value}" '
        return result.rstrip()
        

    def cleanText(self, text):     

        lines = text.splitlines()
        while 0 == len(lines[0].strip()):
            lines.remove(0)
        while 0 == len(lines[len(lines)-1]):
            lines.pop()        
        return '\n'.join(lines)


    def parse(self, convert_markdown=True):

        tokens = self.getTokens()        

        # Convert needed empty lines to text. Note that the range stops BEFORE the first element!
        for i in range(len(tokens)-1, 0, -1):
            if self.tokenIs('EMPTY', tokens[i]) and not self.tokenIs('TEXT', tokens[i-1]):
                del tokens[i]
            elif self.tokenIs('EMPTY', tokens[i]) and self.tokenIs('TEXT', tokens[i-1]):
                indent, _, _ = tokens[i-1]
                tokens[i] = (indent, 'TEXT', '')

        # convert the tags into XML
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
                    a = self.convertAttributes(attribs.get('attribs'))

                    content = attribs.get('content')
                    if content:
                        if content.startswith('"') and content.endswith('"'):
                            content = content[1:-1]
                        else:
                            content = dm.markdown_parser.processMarkdownContent(self.cleanText(content))
                    prefix = attribs.get('prefix')
                    namespace = attribs.get('namespace')
                    if prefix and namespace:
                        tokens[i] = (indent, 'XML', '    '*indent + f'<{prefix}:{tagname} xmlns:{prefix}="{namespace}" {a}>{content}')
                    else:
                        tokens[i] = (indent, 'XML', '    '*indent + f'<{tagname}{a}>{content}')
                    for i in range(i+1, len(tokens)):
                        indent, _, _ = tokens[i]
                        if indent <= level:
                            break
                    if prefix and namespace:
                        tokens.insert(i, (level, 'XML', '    '*level + f'</{prefix}:{tagname}>'))
                    else:
                        tokens.insert(i, (level, 'XML', '    '*level + f'</{tagname}>'))
                i += 1
            level += 1

        # indent the text            
        for i in range(1, len(tokens)):
            l_i, tag_i, text_i = tokens[i]
            l_im, tag_im, _ = tokens[i-1]
            if ('TEXT' == tag_i) and ('TEXT' == tag_im) and (l_i > l_im):
                tokens[i] = (l_im, tag_i, '    '*(l_i - l_im) + text_i)

        for token in tokens:
            self.dump(token)

        # create the output text
        xml = ''
        i = 0
        while i <= len(tokens):
            _, tag, text = tokens[i]
            if 'XML' == tag:
                xml += text + '\n'
            elif 'TEXT' == tag:
                markdown = ''
                while 'TEXT' == tag:
                    markdown += text +'\n'
                    i += 1
                    _, tag, text = tokens[i]
                if convert_markdown:
                    xml += dm.markdown_parser.processMarkdownContent(self.cleanText(markdown)) + '\n'
                else:
                    xml += self.cleanText(markdown)
                continue
            elif 'EOF' == tag:
                break
            elif 'EMPTY' == tag:
                pass
            else:
                logging.error(f'Parse error: {tokens[i]}')
                raise dm.exceptions.TaskException('Parse error')
            i += 1

        return xml.encode('utf-8')