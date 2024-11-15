from dm.exceptions import TaskException
from dm.tasks.Task import Task


class FileTask(Task):

    """ The file task.

        This task allows creating a document from the pipeline definition file.
    """

    def run(self, context):
        # get the text content of the element
        text = self.element.text
        if len(list(self.element)) > 0:
            text += list(self.element).pop().tail
        text = text.strip()
        
        # check that there is content
        if 0 == len(text):
            raise TaskException(f'{self.name} - missing text content')
        
        # set the content
        self.content.setText(text)

        self.save()
