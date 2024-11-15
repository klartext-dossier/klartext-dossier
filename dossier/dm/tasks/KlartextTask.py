import io, logging

from klartext import Parser

from dm.tasks.Task import Task
from dm.markdown_parser import processMarkdownContent
from dm.utilities import tryLocatingFile


class KlartextTask(Task):

    """ The klartext-to-xml task.

        Converts klartext to xml.
    """

    def tryConvertingToXML(self, context):
        try:
            kt = io.StringIO(self.content.data.getvalue().decode(self.content.encoding))
            parser = Parser()
            return parser.parse(kt, basedir=context.basedir(), convert_text=processMarkdownContent, lookup=tryLocatingFile)
        except Exception as e:
            logging.error(f'Cannot convert klartext to xml')
            raise

    def run(self, context):
        self.load()
        xml = self.tryConvertingToXML(context)   
        self.content.setData(xml)
        self.save()
