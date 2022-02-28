from dm.tasks.Task import Task


class SaveTask(Task):

    """ The save task.

        Saves the output document to a file.
    """

    def run(self, context):
        self.save()
