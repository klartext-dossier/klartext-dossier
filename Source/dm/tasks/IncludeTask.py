import io, logging, os, glob, copy

import markdown, python_markdown_comments

from lxml import etree

from dm.exceptions import TaskException
from dm.klartext import KlartextParser
from dm.tasks.Task import Task


class IncludeTask(Task):

    """ The include task.

        Includes several files into one.
    """

    def tryInputGlobbing(self, input):
        pattern = input.text.strip()
        if (r'*' in pattern) or (r'?' in pattern):
            logging.info(f'{self.name} - trying to glob "{pattern}"')
            inputs = []
            for path in glob.glob(pattern, recursive=True):
                logging.debug(f'{self.name} - found "{path}"')
                i = copy.deepcopy(input)
                i.text = path
                inputs.append(i)
            return inputs
        return [input]

    def tryLoadingInclude(self, filename):
        with open(filename, 'rb') as infile:
            logging.info(f'{self.name} - loading {filename}')
            return infile.read().decode('utf-8')

    def tryParsingKlartext(self, klartext, context):
        try:
            kt = io.StringIO(klartext)
            parser = KlartextParser(kt, context)
            return parser.parse()
        except Exception as e:
            logging.error(f'{self.name} - parsing klartext document failed')
            raise

    def tryParsingMarkdown(self, md):
        # TODO: Replace with dm.markdown!
        try:
            if len(md.strip()) == 0:
                md = '<!-- -->'
            return markdown.markdown(md, extensions=['mdx_asciimathml', 'markdown.extensions.attr_list', 'markdown.extensions.tables', 'markdown.extensions.meta', 'markdown.extensions.fenced_code', 'markdown.extensions.sane_lists', 'markdown.extensions.def_list', 'mdx.dossier.admonition', 'mdx.dossier.toc', python_markdown_comments.CommentsExtension(), 'mdx.dossier.template_meta', 'mdx.dossier.template_host', 'mdx.dossier.template_net', 'mdx.dossier.glossary', 'mdx.dossier.outline', 'mdx.dossier.checkbox', 'mdx.dossier.inline_tags', 'mdx.dossier.xhtml_namespace'])
        except Exception as e:
            raise TaskException('{self.name} - cannot convert markdown to XHTML!', e)

    def run(self, context):

        self.root = self.getAttribute('root', default='root')
        self.checkNumberOfElements('input', multiple=True, required=True)
        
        root = etree.Element(self.root)
        
        inputs = []
        for child in self.element.findall('input'):
            inputs.extend(self.tryInputGlobbing(child))
        
        for child in inputs:
            
            include_file = child.text.strip()
            include_tag = child.get('tag', 'content')
            _, extension = os.path.splitext(include_file)
            include_format = child.get('format', extension).lower()

            logging.debug(f'{self.name} - trying to include "{include_file}", format "{include_format}", into tag "{include_tag}"')

            include = self.tryLoadingInclude(include_file)
            basedir = os.path.dirname(include_file)
            if include_format in ['kt', '.kt', 'klartext']:
                with context:
                    context.set_base_dir(basedir)
                    xml = self.tryParsingKlartext(include, context)
                    root.append(etree.fromstring(xml, parser=etree.XMLParser()))            
            elif include_format in ['md', '.md', 'markdown']:
                md = f'<{include_tag}>' + self.tryParsingMarkdown(include) + f'</{include_tag}>'
                root.append(etree.fromstring(md))
            else:
                raise TaskException(f'{self.name} - cannot include file "{include_file}"')

        self.content.setData(etree.tostring(root, encoding='utf-8'))
        self.content.encoding = 'utf-8'
        self.save()
