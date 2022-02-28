import io
import MarkdownPP

from dm.exceptions import TaskException
from dm.tasks.Task import Task


class MarkdownIncludeTask(Task):

    """ The markdown-include task.

        Processes include directives in markdown (.mdpp) files.
    """

    def tryIncludingMarkdown(self):
        try:
            inp = io.StringIO(self.content.data.getvalue().decode(self.content.encoding))
            out = io.StringIO()
            MarkdownPP.MarkdownPP(input=inp, output=out, modules=list(MarkdownPP.modules))
            return out.getvalue()
        except Exception as e:
            raise TaskException('{self.name} - cannot process markdown includes!', e)

    def run(self, context):
        self.load()
        md = self.tryIncludingMarkdown()
        self.content.setText(md)
        self.save()
