from dm.tasks.Task import Task


class DumpTask(Task):

    """ The dump task.

        This task allows displaying the content of a document.
    """

    def run(self, context):
        self.load()
        print(self.content.getText())
