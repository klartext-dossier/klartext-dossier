from dm.tasks.Task import Task


class LoadTask(Task):

    """ The load task.

        Creates a document by loading a file.
    """

    def run(self, context):
        self.load()

