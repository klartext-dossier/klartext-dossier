from dm.exceptions import TaskException
from dm.tasks.Task import Task

from dm.markdown_parser import processMarkdown


class MarkdownTask(Task):

    """ The markdown-to-xhtml task.

        Converts a markdown document to an XHTML file according to the HTMLBook specification.
    """

    def tryConvertingMarkdown(self):
        try:
            md = self.content.data.getvalue().decode(self.content.encoding)
            if len(md.strip()) == 0:    
                md = '<!-- -->'
            return processMarkdown(md)
        except Exception as e:
            raise TaskException('{self.name} - cannot convert markdown to XHTML!', e)

    def run(self, context):
        self.load()
        html = self.tryConvertingMarkdown()
        self.content.setText(html)
        self.save()
