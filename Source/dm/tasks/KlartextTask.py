import io, logging

from dm.exceptions import TaskException
from dm.klartext import KlartextParser
from dm.tasks.Task import Task


class KlartextTask(Task):

    """ The klartext-to-xml task.

        Converts klartext to xml.
    """

    def tryConvertingToXML(self, context):
        try:
            kt = io.StringIO(self.content.data.getvalue().decode(self.content.encoding))
            parser = KlartextParser(kt, context)
            return parser.parse()
        except Exception as e:
            logging.error(f'Cannot convert klartext to xml')
            raise

    def run(self, context):
        self.load()
        xml = self.tryConvertingToXML(context)   
        self.content.setData(xml)
        self.save()
