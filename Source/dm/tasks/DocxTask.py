from lxml import etree

from dm.exceptions import TaskException
from dm.word import WordWriter
from dm.tasks.Task import Task


class DocxTask(Task):

    """ The xhtml-to-docx task.

        This task converts an XHTML file to Docx.
    """

    def tryParsingXHTML(self):
        try:
            return etree.parse(self.content.data, parser=etree.XMLParser())
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse input file', e)   

    def tryWritingDocx(self, html):
        try:
            writer = WordWriter(self.template)
            return writer.convert(html)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot write DOCX', e)

    def run(self, context):
        self.base_url = self.getAttribute('base-url', default='.')
        self.template = self.getElement('template', multiple=False, required=False)
        self.load()
        html = self.tryParsingXHTML()
        self.content.setData(self.tryWritingDocx(html))
        self.save()
